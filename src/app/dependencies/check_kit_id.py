# -*- coding: utf-8 -*-
import logging
from fastapi import Request, HTTPException

# from database import DBConnection, db

logger = logging.getLogger(__name__)


# async def check_kit_id(req: Request, conn: DBConnection) -> None:
#     """
#     Проверка наличия заголовка X-MCC-ID и валидного kit в нём
#     :param req: запрос (передаёт FastApi)
#     :param conn: подключение к базе (зависимость FastApi)
#     :return: None, если kit_id неверен, API не вызывается
#     """
#     kit_id = req.headers.get("X-MCC-ID", None)
#     api_path = req.url.path  # путь вызова API
#     _ll = f"\n\t~>\t\tcheck_kit_id for API {api_path}, kit_id={kit_id} started"
#     status, err = None, None  # текст ошибки и код HTTP ответа
#
#     if kit_id is None:
#         status, err = 400, "HTTP header 'X-MCC-ID' not found in req"
#     elif kit_id == '':
#         status, err = 412, "HTTP header 'X-MCC-ID' contains an empty string"
#     elif not kit_id.isdigit():
#         status, err = 412, f"Kit_id='{kit_id}' is not a positive integer"
#     elif int(kit_id) == 0:
#         status, err = 412, "kit_id is zero"
#     else:
#         out, rs = await db.sp_kit_imdm_get(conn, int(kit_id))
#         if out.o_rc != 0 or not rs:
#             status, err = 475, f"kit_id={kit_id} not found in database"
#
#     if status:
#         logger.error(f"\n\t<~\t\tcheck_kit_id, error for endpoint {api_path}, HTTP={status}, ended:"
#                      f"\n\t\t\t{err}")
#         raise HTTPException(status_code=status, detail={"error": err})
#
#     _ll += f"\n\t<~\t\tcheck_kit_id for API {api_path}, kit_id={kit_id} ok, ended"
#     logger.debug(_ll)
#
#     return None
