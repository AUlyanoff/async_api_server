# -*- coding: utf-8 -*-
import logging

from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.api.v1.routes import v1
from app.api.v1.education.serv import log_it
from utils.json_utils import tojson
from utils.log.utils import trunc_str

logger = logging.getLogger(__name__)


@v1.post("/apps/{app_uid}/icons/{app_id}")
async def get_icon(request: Request, app_uid: int, app_id: int):
    """Отладочный эндпойнт"""

    body = await request.body()
    api_path = request.url.path  # путь вызова API
    body = tojson(body)
    body = str(body).replace('\r', '').replace('\n', '').replace('  ', '') if body is None else body
    logger.info(f"\n\t=>\t\t{api_path} ({get_icon.__doc__}), education endpoint started...\n\tbody\t{body}")

    await log_it(app_uid, app_id)
    # out, rs = await db.sp_assignment_imdm_list_for_kit(conn, 102)

    resp, stat = {"error": "Icon not found, Иконка не найдена"}, 475
    _ll = f"\n\t<=\t\t{api_path}, HTTP={stat} ended" + \
          "\n\tresp\t" + trunc_str(str(resp), delimiter='\n\t\t\t')

    logger.info(_ll) if 200 <= stat < 300 else logger.error(_ll)

    return JSONResponse(resp, status_code=stat)
