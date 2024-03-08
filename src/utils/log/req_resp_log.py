#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re
from contextlib import suppress
from copy import deepcopy
from typing import Callable

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from utils.log.utils import trunc_str, format_flatten_dict

logger = logging.getLogger(__name__)


class LogReqRes(APIRoute):
    """
    Логирует запрос и ответ, включая тело body.
    Использование: добавлять этот класс в те роуты, запросы по которым хотим логировать.
    Например, router = APIRouter(route_class=LogReqRes)
    """

    def get_route_handler(self) -> Callable:
        """Переопределение оригинального route_handler с интеграцией логирования"""
        original_route_handler = super().get_route_handler()    # сохраним текущий обработчик маршрута

        async def request_response_logger(req: Request) -> Response:
            """Логирование запроса и ответа, принимает запрос, возвращает ответ"""

            # ------------------------------------------- логирование запроса -----------------------------------------
            if logger.getEffectiveLevel() <= logging.INFO:      # только для INFO и DEBUG
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

            # ------------------------------------------- вызов эндпойнта ---------------------------------------------
            try:
                response: Response = await original_route_handler(req)
            except RequestValidationError as e:
                logger.error(f"(After calling endpoint): {req.url} error passing parameters to endpoint:\n\t{e}")
                raise
            except Exception:   # todo накопить опыт, какие будут ошибки, и обработать их здесь
                raise
            else:               # можно удалить ветку else после завершения накопления ошибок
                logger.debug(f'endpoint {req.url.path} ended without internal errors')

            # ------------------------------------------- логирование ответа ------------------------------------------
            response.headers['X-Frame-Options'] = 'DENY'  # запрет на отображение во фреймах [#22896]

            with suppress(Exception):
                ll = f"\n\t<≡\t\t{req.method} {req.url.path} processing request HTTP={response.status_code} ended"
                ll += "\n\thead\t" + format_flatten_dict(dict(response.headers))       # заголовки ответа
                ll += "\n\tbody\t" + trunc_str(response.body.decode())                 # тело ответа

                # ошибку логируем обязательно, а успех в зависимости от установленного уровня логирования
                if 200 <= response.status_code <= 299 or response.status_code == 302 or response.status_code == 475:
                    logger.info(ll)
                else:
                    logger.error(ll)
            # ---------------------------------------------------------------------------------------------------------

            return response

        return request_response_logger
