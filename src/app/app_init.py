# -*- coding: utf-8 -*-
import logging

from contextlib import asynccontextmanager
from os import path, environ
from sys import version as python_ver

from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, __version__ as fast_api_ver
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.routes import v1
from app.api.v2.routes import v2
from app.errorhandlers import pydantic_exception_handler, check_mtls_exception_handler
from app.exceptions import MtlsException
from utils.log.req_duration import request_duration
from utils.log.req_id import generate_req_id
from asyncpg import __version__ as asyncpg_ver
from database.init import db_init

from app.app_ver import app_ver
from config.db import db_cfg
from config.app import cfg


# noinspection PyUnusedLocal
@asynccontextmanager
async def lifespan(application: FastAPI):
    """Пред- и постобработчик запуска FastAPI"""
    # код до yield будет выполнен после создания приложения - объекта FastAPI, но перед его инициализацией

    await db_init()  # связываемся с базой
    # await db.make_connection_pool()  # создаём пул коннектов
    # components = await get_components_versions({"MDM_VERSION": app_ver})
    # logger.fatal(components)
    # setup_log(config.log_int, config.timing_int, config.log_format)  # инициализация логирования
    logger.debug("Server loaded successfully\n")

    # await check_database(await db.get_connection_from_pool())  # сверка сохранённых процедур и процедур в DB

    yield
    # код после yield будет выполнен, когда FastAPI будет остановлен (когда запросы больше обрабатываться не будут)

# ----------------------------------------- начало загрузки сервиса ---------------------------------------------------
logger = logging.getLogger(__name__)
boot = logging.getLogger('boot')

# создание приложения - объекта FastAPI
app = FastAPI(lifespan=lifespan, debug=True)

app.middleware('http')(request_duration)  # логирование длительности запроса
app.middleware('http')(generate_req_id)  # генерация асинх контекстного id запроса

# noinspection PydanticTypeChecker
app.add_exception_handler(RequestValidationError, pydantic_exception_handler)
app.add_exception_handler(MtlsException, check_mtls_exception_handler)

# app.include_router(ios_router, tags=['iOS'])  # регистрация роутов iOS
app.include_router(v1, prefix="/api/v1", tags=["version_1"])  # регистрация роутов Android
app.include_router(v2, prefix="/api/v2", tags=["version_2"])  # регистрация роутов Android


# --------------------------------------------- логирование итогов загрузки -------------------------------------------
v1_routes = v1.routes.__len__()
v2_routes = v2.routes.__len__()

routes = app.routes.__len__()
summary = dict(
    log_level=f"timing {cfg.timing_int}, logging {cfg.log_int} ({logging.getLevelName(cfg.log_int)})",
    python=str(python_ver),
    engine=f'FastAPI {fast_api_ver} (debug {app.debug}), asyncpg {asyncpg_ver}',
    config_path=path.join(environ.get('CONF_DIR')),
    routes_quantity=f'{routes} (include system={routes - v1_routes - v2_routes}, v1={v1_routes}, v2={v2_routes})',
    version=app_ver,
)
boot.info('Main parameters:' + ''.join([f'\n\t{k:<16} \t= {v}' for k, v in summary.items()]))


# ----------------------------------------- обработчики ---------------------------------------------------------------
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    """Перехват исключений HTTP и возврат описания ошибки в словаре"""
    return JSONResponse(exc.detail, status_code=exc.status_code)
