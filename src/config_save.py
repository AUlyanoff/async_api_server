# -*- coding: utf-8 -*-
import logging
import yaml

from pydantic import BaseModel, Field, PositiveInt, IPvAnyAddress, ConfigDict, FilePath, StrictStr, AnyUrl, SecretStr
from typing import Literal, ClassVar, Any, Union
from typing_extensions import Annotated

from utils.base_config.base_config import BaseAppConfig
from utils.paths import SRC_PATH

logger = logging.getLogger(__name__)


class DBconfig(BaseModel):
    """ Дата-класс для проверки значений параметров конфига базы """
    # разрешим приведение типов numbers -> str и запретим неописанные параметры
    model_config = ConfigDict(coerce_numbers_to_str=True, extra='forbid')

    # обязательные параметры
    db_schema: StrictStr                                    # строгая строка - запретим приведение типов numeric -> str
    user: StrictStr
    password: Union[SecretStr, int]
    host: Union[IPvAnyAddress, AnyUrl, StrictStr]           # IP-адрес v4/v6, или любой url, или нецифровая строка
    port: PositiveInt                                       # натуральное число
    name: StrictStr

    # необязательные параметры, могут отсутствовать
    type: Literal['postgresql', 'PostgreSQL', 'Mock', 'mock'] = 'postgresql'  # перечень возможных значений
    minconn: Annotated[int, Field(ge=1, le=1999)] = 5       # натуральное число с ограничением сверху
    maxconn: Annotated[int, Field(ge=2, le=2000)] = 40
    sslmode: Literal['disable', 'allow', 'prefer', 'require', 'verify-ca', 'verify-full'] = 'disable'
    sslrootcert: FilePath = ''                              # путь существует и является файлом
    sslcert: FilePath = ''
    sslkey: FilePath = ''

    def __init__(self):
        """Инициализация класса конфига БД"""
        _db = self.fs_load_db()
        super().__init__(db=_db)

    @staticmethod
    def fs_load_db():
        """Чтение из файла настроек базы
        При наличии конфига разработчика, продуктовый конфиг игнорируется
        """
        db_yaml_path = SRC_PATH.joinpath('config/db_dev.yml')
        if not db_yaml_path.is_file():
            db_yaml_path = SRC_PATH.joinpath('config/db.yml')
            if not db_yaml_path.is_file():
                raise FileNotFoundError(f'DB config not found: {db_yaml_path}')

        logger.fatal(db_yaml_path.name + ' found and will be used for database connect')

        with open(db_yaml_path) as f:  # создаём конфиг-словарь базы
            db_dict = yaml.safe_load(f).get('db')
            if db_dict is None:
                raise ValueError(f'DB dictionary is empty: {db_yaml_path}')

        return db_dict

class Uvicorn(BaseModel):
    """ Описание параметра uvicorn в app[_dev].yml """
    # все параметры необязательные
    log: BaseAppConfig.LogTypes = 'error'
    workers: int = 1
    host: str | None = None
    port: int | None = None


# class MdmServerConfig(BaseAppConfig):
#     class Uvicorn(BaseAppConfig.ServerParams):
#         """Uvicorn setting impl"""
#         log: BaseAppConfig.LogTypes = 'error'
#         workers: int = 1
#         host: str | None = None
#         port: int | None = None
#
#     uvicorn: Uvicorn = Uvicorn()
#
#
# config = MdmServerConfig('mdm')

class APPconfig(BaseModel):
    """ Для проверки параметров приложения """
    model_config = ConfigDict(extra='forbid')   # неописанные параметры запрещены
    LogTypes: ClassVar = Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL']

    # все параметры необязательные
    loglevel: LogTypes = 'DEBUG'
    timing: LogTypes = 'CRITICAL'
    flask_debug: bool = False
    log_format: StrictStr = ''                  # строгое StrictStr вместо str - чтобы избежать приведения типов
    reload_settings_period: Annotated[int, Field(ge=0, le=3600)] = None
    uvicorn: Uvicorn = None                       # параметр конфига server - это словарь


config = APPconfig()
