# -*- coding: utf-8 -*-
import logging
from copy import deepcopy
import re

from starlette.requests import Request
from contextvars import ContextVar
from contextlib import suppress

from serv.log_utils import format_flatten_dict, trunc_str, log_resp

ctx_req_id = ContextVar('req_id')
logger = logging.getLogger()


# Middleware
async def log_all_req(req: Request, call_next):
    """Логирование запросов/ответов, КОТОРЫЕ НЕ ОБРАБАТЫВАЕТ FastAPI
       например 404, 405 обрабатывает httpx
       Функция зарегистрирована при загрузке сервера как middleware.
    """

    if logger.getEffectiveLevel() <= logging.INFO:    # только для INFO и DEBUG
        with suppress(Exception):
            ll = f"\n\t≡>\t\t{req.method} {req.url} processing request started..."
            ll += f"\n\thead\t{format_flatten_dict(dict(req.headers))}"

            body = await req.body()
            if body:
                _body = deepcopy(body)
                _body = _body.decode() if hasattr(_body, 'decode') else _body
                _body = re.sub(r"\s+", " ", _body)
                ll += f"\n\tbody \t{trunc_str(_body)}"

            logger.info(ll)

    resp = await call_next(req)

    if resp.headers.get('x-frame-options') is None:     # log_resp ещё не получал управления
        await log_resp(req, resp)     # логирование ответа

    return resp
