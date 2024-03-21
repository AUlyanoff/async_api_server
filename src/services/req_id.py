# -*- coding: utf-8 -*-
import logging
import time

from starlette.requests import Request
from contextvars import ContextVar
from contextlib import suppress
from services.consts import http400

from services.log_utils import format_flatten_dict, trunc_str

ctx_req_id = ContextVar('req_id')
logger = logging.getLogger()


# Middleware
async def generate_req_id(req: Request, call_next):
    """Генерация уникального номера запроса. Номер храним в контексте корутины.
    Используем позже, при логировании, для идентификации нисходящих вызовов (какому запросу они принадлежат).
    Функция зарегистрирована при загрузке сервера как middleware.
    """
    # номер запроса - это системное время, усечённое справа до сотых секунды, а слева до миллиона секунд (почти год)
    req_id = str(int(time.time() * 100)).zfill(12)[3:]
    req_id = f'{req_id[0:6]}-{req_id[6:]}'
    ctx_req_id.set(req_id)

    if logger.getEffectiveLevel() <= logging.INFO:  # только для INFO и DEBUG
        with suppress(Exception):
            ll = f"\n\t≡>\t\t{req.method} {req.url} processing request started..."
            ll += f"\n\thead\t{format_flatten_dict(dict(req.headers))}"
            logger.info(ll)

    resp = await call_next(req)

    # ------------------------------------------- логирование ответа ------------------------------------------
    if resp.status_code in (404, 405):
        resp.headers['X-Frame-Options'] = 'DENY'  # запрет на отображение во фреймах [#22896]

        with suppress(Exception):
            expl = http400.get(resp.status_code, 'Unknown').upper()
            ll = f"\n\t<≡\t\t{req.method} {req.url.path} processing request HTTP={resp.status_code} {expl} failed"
            ll += "\n\thead\t" + format_flatten_dict(dict(resp.headers))  # заголовки ответа
            ll += "\n\tbody\t" + trunc_str(getattr(resp, 'body', b'None').decode())  # тело ответа

            # ошибку логируем обязательно, а успех в зависимости от установленного уровня логирования
            if 200 <= resp.status_code <= 299 or resp.status_code == 302 or resp.status_code == 475:
                logger.info(ll)
            else:
                logger.error(ll)
    # ---------------------------------------------------------------------------------------------------------

    return resp
