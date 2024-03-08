# -*- coding: utf-8 -*-
import logging
import re
import time
from random import choices
from string import ascii_letters
from typing import Literal, Optional, ClassVar

import yaml
from pydantic import BaseModel, Field, PositiveInt, ConfigDict, FilePath, model_validator, computed_field
from typing_extensions import Annotated

from ..certificate_utils import validate_cert
from ..consts import logging_levels
from ..paths import config_path

logger = logging.getLogger('PreInitLogger')


class DatabaseConfig(BaseModel):
    """Класс конфигурации базы данных"""
    # разрешение приведения типов number -> str
    model_config = ConfigDict(coerce_numbers_to_str=True)

    # ============================== обязательные параметры ============================================
    type: Literal['postgresql', 'PostgreSQL', 'Mock', 'mock']  # перечень возможных значений
    user: str
    password: str
    host: str  # может быть ip адрес или hostname
    port: PositiveInt  # натуральное число
    name: str

    # ============================== необязательные параметры ==========================================
    checkversion: bool = True
    sslmode: Literal['disable', 'allow', 'prefer', 'require', 'verify-ca', 'verify-full'] = 'disable'
    sslrootcert: Optional[FilePath] = None
    sslcert: Optional[FilePath] = None
    sslkey: Optional[FilePath] = None

    # validation_alias = '' отключает чтение параметров из db.yml
    minconn: Annotated[int, Field(validation_alias=None)] = 5
    maxconn: Annotated[int, Field(validation_alias=None)] = 40

    # ============================== динамические параметры ============================================
    app_name: Annotated[str, Field(max_length=256)] = ''  # формируются
    settings_hash: Annotated[str, Field(max_length=256)] = ''  # динамически

    # ============================== дополнительная валидация ==========================================
    @model_validator(mode='after')
    def mtls_db_validator(self) -> 'DatabaseConfig':
        """Валидация сертификатов базы данных"""
        if self.sslmode in {'require', 'verify-ca', 'verify-full'}:
            logger.debug('Validating mtls-db sslrootcert')
            res, err = validate_cert(self.sslrootcert)
            if not res:
                logger.debug('sslrootcert missing')

            logger.debug('Validating mtls-db sslcert')
            res, err = validate_cert(self.sslcert)
            if not res:
                raise ValueError('Validation failed for sslcert field')

            if not self.sslkey:
                raise ValueError('Validation failed for sslkey field')

        return self


class BaseAppConfig(BaseModel):
    """Класс базового конфига приложения"""
    db: DatabaseConfig

    # ============================== Базовые классы конфига приложений =================================
    class ServerParams(BaseModel):
        numthreads: Annotated[int, Field(ge=1)] = 19

    class DbPool(BaseModel):
        minconn: Annotated[int, Field(ge=0)] = 5  # натуральное число с ограничением сверху
        maxconn: Annotated[int, Field(ge=1)] = 40

        @model_validator(mode='after')
        def validate_min_max_conn(self):
            """Валидация количества подключений к БД"""
            if self.maxconn < self.minconn:
                raise ValueError('minconn is greater than maxconn')

            return self

    LogTypes: ClassVar = Literal[
        'd', 't', 'debug', 'i', 'info', 'e', 'error', 'c', 'critical', 'f', 'fatal', 'w', 'warning', 'warn',
        'D', 'T', 'DEBUG', 'I', 'INFO', 'E', 'ERROR', 'C', 'CRITICAL', 'F', 'FATAL', 'W', 'WARNING', 'WARN',
    ]

    # ============================== Базовые параметры конфига приложений ==============================
    log: LogTypes = 'D'
    timing: LogTypes = 'C'

    log_format: str = ('%(asctime)s %(levelname).1s: %(req_id)s: '
                       '%(filename)s/%(funcName)s(%(lineno)s): %(message)s')
    db_pool: DbPool = DbPool()
    server: ServerParams = ServerParams()

    sowa: bool = False

    # ============================== Вычисляемые параметры конфига приложений ==========================
    @computed_field
    @property
    def log_int(self) -> int:
        """Преобразует уровень логирования log из строки в IntEnum"""
        return logging_levels.get(self.log.upper(), logging.DEBUG)

    @computed_field
    @property
    def timing_int(self) -> int:
        """Преобразует уровень логирования timing из строки в IntEnum"""
        return logging_levels.get(self.timing.upper(), logging.FATAL)

    # ============================== Параметры обратной совместимости ==================================
    udp_log: str = None  # используется в android_monitor_settings_service, зачем - неизвестно

    def __init__(self, file_name: str):
        """Инициализация базового класса конфигурации
        :param file_name: наименование файла конфигурации (без расширения)
        """
        _db = self.fs_load_db()
        data = self.fs_load_app(file_name)

        super().__init__(db=_db, **data)

        # проброс параметров minconn, maxconn в self.db
        self.db.minconn = self.db_pool.minconn
        self.db.maxconn = self.db_pool.maxconn

    @staticmethod
    def fs_load_db():
        """Чтение из файла настроек базы
        При наличии конфига разработчика, продуктовый конфиг игнорируется
        """
        db_yaml_path = config_path.joinpath('db_dev.yml')
        if not db_yaml_path.is_file():
            db_yaml_path = config_path.joinpath('db.yml')
            if not db_yaml_path.is_file():
                raise FileNotFoundError(f'DB config not found: {db_yaml_path}')

        logger.fatal(db_yaml_path.name + ' found and will be used for database connect')

        with open(db_yaml_path) as f:  # создаём конфиг-словарь базы
            db_dict = yaml.safe_load(f).get('db')
            if db_dict is None:
                raise ValueError(f'DB dictionary is empty: {db_yaml_path}')

        return db_dict

    @staticmethod
    def fs_load_app(file_name):
        """Чтение из файла настроек приложения
        При наличии конфига разработчика, продуктовый конфиг игнорируется
        """
        app_yaml_path = config_path.joinpath(f'{file_name}_dev.yml')
        if not app_yaml_path.is_file():
            app_yaml_path = config_path.joinpath(f'{file_name}.yml')
            if not app_yaml_path.is_file():
                raise FileNotFoundError(f'APP config not found: {app_yaml_path}')
        logger.fatal(app_yaml_path.name + ' found and will be used for web-application')

        with open(app_yaml_path) as f:  # создаём конфиг-словарь приложения
            app_dict = yaml.safe_load(f).get(file_name)
            if app_dict is None:
                raise ValueError(f'APP dictionary is empty: {app_yaml_path}')

        return app_dict

    def add_app_name(self, application_name: str, version: str) -> None:
        """
        Формирует строку "application_name" для записи её в подключение к БД
        ВАЖНО: для одного application функцию вызывать 1 раз
        :param application_name: наименование компонента
        :param version: версия компонента в формате строки
        :return: строку application_name
        """
        version_match = re.search(r'^\d+(\.\d+)*-\d+-\w+', version)
        if not version_match:
            logger.warning(f'Wrong version format: {version}')
            version_str = version
        else:
            version_str = version_match.group()

        self.db.app_name = 'SM {app} {ver} {instance_id} {timestamp}'.format(
            app=application_name,
            ver=version_str,
            instance_id=''.join(choices(ascii_letters, k=8)),
            timestamp=int(time.time())
        )

    def update(self, **sets) -> None:
        """Обновить значения параметров словарём sets (загрузить из этого словаря)"""
        for k, v in sets.items():
            setattr(self, k, v)
