# -*- coding: utf-8 -*-
import logging
import time

from starlette.requests import Request

from contextvars import ContextVar

ctx_req_id = ContextVar('req_id')
logger = logging.getLogger()


async def generate_req_id(request: Request, call_next):
    """Генерация уникального номера запроса. Номер храним в контексте корутины.
    Используем позже, при логировании, для идентификации нисходящих вызовов (какому запросу они принадлежат).
    Функция зарегистрирована при загрузке сервера как middleware.
    """
    # номер запроса - это системное время, усечённое справа до сотых секунды, а слева до миллиона секунд (почти год)
    req_id = str(int(time.time() * 100)).zfill(12)[3:]
    req_id = f'{req_id[0:6]}-{req_id[6:]}'
    ctx_req_id.set(req_id)

    response = await call_next(request)
    return response
