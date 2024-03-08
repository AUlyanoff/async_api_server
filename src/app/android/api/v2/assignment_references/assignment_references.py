# -*- coding: utf-8 -*-
import logging

from fastapi.responses import JSONResponse
from fastapi import Depends
from starlette.requests import Request

from app.android.api.v2.routes import v2
from app.android.dependencies.check_kit_id import check_kit_id

from database import DBConnection
from utils.log.utils import trunc_str

logger = logging.getLogger(__name__)


@v2.get("/assignment_references", dependencies=[Depends(check_kit_id), ])  # проверка номера комплекта
async def assignment_references(request: Request, conn: DBConnection, kit_id: int = None):
    """Запрос списка назначений"""
    api_path = request.url.path  # путь вызова API
    logger.info(f"\n\t=>\t\t{api_path} ({assignment_references.__doc__}) kit_id={kit_id}, endpoint started...")

    resp, stat = {"data": "Список назначений"}, 200
    _ll = f"\n\t<=\t\t{api_path}, HTTP={stat} ended" + "\n\tresp\t" + trunc_str(str(resp))

    # _ll += f"\n\tdberr\t" + trunc_str(str(db_errs), delimiter='\n\t\t\t') if db_errs else ' '

    logger.info(_ll) if 200 <= stat < 300 else logger.error(_ll)

    return JSONResponse(resp, status_code=stat)
