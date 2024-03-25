# -*- coding: utf-8 -*-
import logging

from contextlib import asynccontextmanager
from os import path, environ
from sys import version as python_ver

from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import ProgrammingError, InterfaceError
from asyncpg.exceptions import InternalServerError
from fastapi import FastAPI, __version__ as fast_api_ver
from asyncpg.exceptions._base import PostgresError

from app.api.v1.routes import v1
from app.api.v2.routes import v2
from app.errorhandlers import pydantic, postgres, tabel_not_found, authentication, interface_err, all_err
from serv.req_duration import request_duration
from serv.req_id import generate_req_id
from serv.log_req_res import log_req_res
from serv.log_init import setup_log
from asyncpg import __version__ as asyncpg_ver
from database.core import db_init, db_closed

from app.app_ver import app_ver
from config.app_mdl import cfg


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Пред- и постобработчик запуска FastAPI"""
    await db_init()                                 # связываемся с базой
    setup_log(cfg.log_int, cfg.log_format)          # инициализация логирования
    boot.info("Server loaded successfully, waiting request...")

    # код до yield будет выполнен после создания объекта FastAPI, но перед его инициализацией
    yield
    # код после yield будет выполнен, когда FastAPI будет остановлен (когда запросы больше обрабатываться не будут)

    await db_closed()
    boot.info("... server finished")
# ----------------------------------------- начало загрузки сервиса ---------------------------------------------------
logger = logging.getLogger(__name__)
boot = logging.getLogger('boot')

# создание нашего приложения - объекта FastAPI
app = FastAPI(lifespan=lifespan, debug=cfg.debug)


# noinspection PydanticTypeChecker
app.add_exception_handler(Exception, all_err)
app.add_exception_handler(RequestValidationError, pydantic)
app.add_exception_handler(PostgresError, postgres)
app.add_exception_handler(ProgrammingError, tabel_not_found)
app.add_exception_handler(InternalServerError, authentication)
app.add_exception_handler(InterfaceError, interface_err)

# app.include_router(ios_router, tags=['iOS'])  # регистрация роутов iOS
app.include_router(v1, prefix="/api/v1", tags=["version_1"])  # регистрация роутов Android
app.include_router(v2, prefix="/api/v2", tags=["version_2"])  # регистрация роутов Android

app.middleware('http')(log_req_res)  # логирование запросов, не попавших в FastAPI
app.middleware('http')(request_duration)  # логирование длительности запроса
app.middleware('http')(generate_req_id)  # генерация асинхронного контекстного id запроса
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
