# -*- coding: utf-8 -*-
import logging

from fastapi import Request
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from asyncpg.exceptions import InternalServerError
from asyncpg.exceptions._base import PostgresError
# from database.exceptions import DatabaseException, ResultCheckException

from utils.log.utils import format_flatten_dict, trunc_str
from utils.consts import db_errs

logger = logging.getLogger(__name__)


async def pydantic(request: Request, exc: RequestValidationError):
    """Обработчик исключений от Pydantic"""
    """FastApi вызывает Pydantic
       - съедает исключение Pydantic-а ValidationError,
       - добавляет свои обработки и
       - перевозбуждает исключение под именем RequestValidationError
    """
    ll = f'\n\t<~\t\tPydantic validation error: {request.url.path}, {request.scope["endpoint"].__name__}'

    ls = list()
    if 'pydantic' in str(exc.errors()).lower():
        stat = 400
        response = PlainTextResponse(content='Bad request. Wrong body', status_code=stat)
        for error in exc.errors():
            ls.append(f"\t\t\t- {str(error.get('type'))[:16]:<16} "
                      f"{(': ').join(error.get('loc')):<20} = {str(error.get('input')):<12} {error.get('msg')}.")
    elif 'json_invalid' in str(exc.errors()).lower():
        stat = 400
        response = PlainTextResponse(content='Bad request. Invalid json', status_code=stat)
    else:
        # todo накопить опыт и обработать другие случаи здесь, а пока http=500
        stat = 500
        response = PlainTextResponse(content='Unexpected RequestValidationError', status_code=stat)

    ll += '\n'.join(ls)
    ll += f"\n\t<≡\t\t{request.method} {request.url.path} processing request HTTP={stat} ended"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))  # заголовки ответа
    ll += "\n\tdata\t" + trunc_str(response.body.decode())  # тело ответа

    logger.error(ll)

    return response


# async def database_exception_handler(request: Request, exc: DatabaseException):
#     """Обработчик исключения базы данных"""
#     response = PlainTextResponse(content='DatabaseError', status_code=500)
#     ll = f"\n\t<≡\t\t{request.method} {request.url.path} processing request ended, HTTP={response.status_code}"
#     ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))
#     ll += "\n\tdata\t" + trunc_str(response.body.decode())
#     sqlstate = getattr(exc.exception, 'sqlstate', None)
#     detail = getattr(exc.exception, 'detail', None)
#
#     ll += f"\n\t\t\tError executing SP {exc.proc_name}" \
#           f"\n\t\t\t{db_errs.get(sqlstate, 'Unexpected database error')} " \
#           f"asyncpg: {sqlstate}, {exc.exception.__repr__()}, detail: {detail}"
#
#     logger.error(ll)
#
#     return response


async def postgres(request: Request, exc: PostgresError) -> PlainTextResponse:
    """Обработчик исключения неверного кода возврата"""
    if isinstance(exc, InternalServerError):
        pass
    response = PlainTextResponse(content='DatabaseError', status_code=500)

    ll = f'\n\tError checking ResultCode for SP: {exc.proc_name}: rc={exc.rc}, err={exc.err}'
    ll += f"\n\t<≡\t\t{request.method} {request.url.path} processing request ended"
    ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))    # заголовки ответа
    ll += "\n\tdata\t" + trunc_str(response.body.decode())              # тело ответа

    logger.error(ll)
    return response
