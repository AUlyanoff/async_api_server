# -*- coding: utf-8 -*-
import sys
import logging
import yaml

from pydantic import BaseModel, ConfigDict, StrictStr, ValidationError
from typing import Literal, ClassVar

from utils.base_config.base_config import BaseAppConfig
from utils.paths import BASE_PATH

logger = logging.getLogger(__name__)


class Uvicorn(BaseModel):
    """ Описание параметра uvicorn в app[_dev].yml """
    model_config = ConfigDict(extra='forbid')  # неописанные параметры запрещены
    # все параметры необязательные, и если опущены, примут значения по умолчанию как здесь указано
    log: BaseAppConfig.LogTypes = 'error'
    workers: int = 1
    host: str | None = '0.0.0.0'
    port: int | None = 8000


class APPconfig(BaseModel):
    """ Дата-класс для проверки параметров конфига приложения """
    model_config = ConfigDict(extra='forbid')   # неописанные параметры запрещены
    LogTypes: ClassVar = Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL']

    # все параметры необязательные
    log: LogTypes = 'DEBUG'
    timing: LogTypes = 'CRITICAL'
    log_format: StrictStr = '%(levelname).1s: %(req_id)s: %(filename)s/%(funcName)s(%(lineno)s): %(message)s'
    uvicorn: Uvicorn = Uvicorn()                       # параметр конфига uvicorn - это словарь

    def __init__(self):
        """Инициализация класса конфига БД"""
        super().__init__(**self.load_app())

    @staticmethod
    def load_app() -> dict:
        """Чтение из файла настроек приложения
        При наличии конфига разработчика, продуктовый конфиг игнорируется
        """
        app_yaml_path = BASE_PATH.joinpath(f'config/app_dev.yml')
        if not app_yaml_path.is_file():
            app_yaml_path = BASE_PATH.joinpath(f'config/app.yml')
            if not app_yaml_path.is_file():
                sys.tracebacklimit = 0
                raise FileNotFoundError(f'APP config not found: {app_yaml_path}')
        logger.fatal(app_yaml_path.name + ' found and will be used for web-application')

        with open(app_yaml_path) as f:  # создаём конфиг-словарь приложения
            app_dict = yaml.safe_load(f).get('app')
            if app_dict is None:
                sys.tracebacklimit = 0
                raise ValueError(f'APP-config has no "app:" section: {app_yaml_path}')

        return app_dict


if __name__ == 'config.app':
    try:
        cfg = APPconfig()
    except ValidationError as e:
        ll = list()
        for error in e.errors():
            ll.append(f"\t\t\t- {str(error.get('type'))[:16]:<16} "
                      f"{': '.join(error.get('loc')):<20} = {str(error.get('input')):<12} {error.get('msg')}.")
        from warnings import warn_explicit
        warn_explicit("\n" + "\n".join(ll) + "\nError loading APP-config, fix it. Server stopped now...",
                      category=UserWarning, filename='', lineno=-1)
        exit(-2)
