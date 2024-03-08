# -*- coding: utf-8 -*-
import logging

from fastapi import Request
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from database.exceptions import DatabaseException, ResultCheckException
from app.exceptions import MtlsException

from utils.log.utils import format_flatten_dict, trunc_str
from utils.consts import db_errs

logger = logging.getLogger(__name__)


async def pydantic_exception_handler(request: Request, exc: RequestValidationError):
    """Обработчик исключений от Pydantic"""
    """FastApi вызывает Pydantic
       - съедает исключение Pydantic-а ValidationError,
       - добавляет свои обработки и
       - перевозбуждает исключение под именем RequestValidationError
    """
    if 'pydantic' in str(exc.errors()).lower():
        stat = 400
        response = PlainTextResponse(content='Bad request. Wrong body', status_code=stat)
    elif 'json_invalid' in str(exc.errors()).lower():
        stat = 400
        response = PlainTextResponse(content='Bad request. Invalid json', status_code=stat)
    else:
        # todo накопить опыт и обработать другие случаи здесь, а пока http=500
        stat = 500
        response = PlainTextResponse(content='Unexpected RequestValidationError', status_code=stat)

    ll = f'\n\t<~\t\tPydantic validation error: {request.url.path}, {request.scope["endpoint"].__name__}'
    ll += f'\n\tbody\terror {trunc_str(exc.errors())}'
    ll += f"\n\t<≡\t\t{request.method} {request.url.path} processing request HTTP={stat} ended"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))  # заголовки ответа
    ll += "\n\tdata\t" + trunc_str(response.body.decode())  # тело ответа

    logger.error(ll)

    return response


async def database_exception_handler(request: Request, exc: DatabaseException):
    """Обработчик исключения базы данных"""
    response = PlainTextResponse(content='DatabaseError', status_code=500)
    ll = f"\n\t<≡\t\t{request.method} {request.url.path} processing request ended, HTTP={response.status_code}"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))
    ll += "\n\tdata\t" + trunc_str(response.body.decode())
    sqlstate = getattr(exc.exception, 'sqlstate', None)
    detail = getattr(exc.exception, 'detail', None)

    ll += f"\n\t\t\tError executing SP {exc.proc_name}" \
          f"\n\t\t\t{db_errs.get(sqlstate, 'Unexpected database error')} " \
          f"asyncpg: {sqlstate}, {exc.exception.__repr__()}, detail: {detail}"

    logger.error(ll)

    return response


async def check_rc_exception_handler(request: Request, exc: ResultCheckException) -> PlainTextResponse:
    """Обработчик исключения неверного кода возврата"""
    response = PlainTextResponse(content='DatabaseRCError', status_code=500)

    ll = f'\n\tError checking ResultCode for SP: {exc.proc_name}: rc={exc.rc}, err={exc.err}'
    ll += f"\n\t<≡\t\t{request.method} {request.url.path} processing request ended"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))    # заголовки ответа
    ll += "\n\tdata\t" + trunc_str(response.body.decode())              # тело ответа

    logger.error(ll)
    return response


async def check_mtls_exception_handler(request: Request, exc: MtlsException):
    """Обработчик неверного сертификата mTLS устройства"""
    response = JSONResponse({"error": exc.err}, exc.stat)

    ll = f"\n\t<≡\t\t{request.method} {request.url.path} processing request ended, HTTP={exc.stat}, {exc.err}"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))    # заголовки ответа
    ll += "\n\tdata\t" + trunc_str(response.body.decode())              # тело ответа

    logger.error(ll)
    return response
