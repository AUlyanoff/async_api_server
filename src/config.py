# -*- coding: utf-8 -*-
from utils.base_config.base_config import BaseAppConfig


class MdmServerConfig(BaseAppConfig):
    class Uvicorn(BaseAppConfig.ServerParams):
        """Uvicorn setting impl"""
        log: BaseAppConfig.LogTypes = 'error'
        workers: int = 1
        host: str | None = None
        port: int | None = None

    uvicorn: Uvicorn = Uvicorn()


config = MdmServerConfig('mdm')
