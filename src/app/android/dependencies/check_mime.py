# -*- coding: utf-8 -*-
import logging

from starlette.requests import Request
from fastapi import HTTPException
from re import split as re_split

logger = logging.getLogger(__name__)


async def check_mime(request: Request):
    """Проверка Content-Type"""
    """Если Content-Type не содержит application/json, то API не вызывается"""

    api_path, endpoint = request.url.path, request.scope['endpoint']  # путь вызова API и объект эндпойнта
    content_type = request.headers.get("Content-Type", None)
    logger.debug(f"\n\t~>\t\tcheck_mime ({check_mime.__doc__}) for API {api_path}, started..."
                 f"\n\t\t\tfor {endpoint.__name__} ({str(endpoint.__doc__).strip()}), Content-Type={content_type}")

    status, err = None, None  # текст ошибки и код HTTP ответа

    # Реализация требований Сбера АТ-19, тест-кейс 3.5, TS-32974
    if content_type is None:
        err, status = "HTTP header Content-Type is missing. Request failed.", 400
    elif content_type.strip() == '':
        err, status = "Empty Content-Type. Request failed.", 412
    elif 'application/json' not in re_split('[ ;]', content_type):
        err, status = f"Wrong Content-Type='{content_type}', 'application/json' required.", 412

    if status is not None:
        logger.error(f"\n\t<~\t\tcheck_mime, error for API {api_path}, HTTP={status} failed, ended"
                     f"\n\t\t\tfor {endpoint.__name__} ({str(endpoint.__doc__).strip()}), {err}")
        raise HTTPException(status_code=status, detail={"error": err})

    logger.debug(f"\n\t<~\t\tcheck_mime for API {api_path}, Content-Type={content_type} ok, ended")

    return None
