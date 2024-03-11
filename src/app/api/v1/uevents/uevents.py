#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging.handlers
import re
from typing import Optional

from dataclasses import dataclass

# from database import DBConnection, db
# from app.android.dependencies.check_kit_id import check_kit_id

# from app.android.api.v1.uevents.events_service import add_universal_event

"""
Универсальные события передаются в requestbody http-запроса.
Кодировка UTF-8.
Relative URL: /v1/events
Метод: POST
Headers запроса:
Content-Type: application/json;charset=UTF-8
X-MCC-ID: - идентификатор комплекта (long).
Обычно число из параметра safephone.common.mobile_id конфигурации приложения
(см. Общие системные настройки SDK Safepohone)
requestbody: Массив событий в формате json.
"""

# todo __name__
logger = logging.getLogger(__name__)


@dataclass
class GuardlinerData:
    """Целый класс для описания браслета"""
    model_name: str = "Guardliner"
    model_version: str = "1.0"
    serial_number: str = ""


def find_guardliner(user_agent) -> Optional[GuardlinerData]:
    """Извлекает из User-Agent: Guardliner/1.0 (ABCD002F)
    :param user_agent:
    :return: serial_number
    """
    if not user_agent:
        return None

    pattern = "Guardliner/(\\S+) [(]([a-zA-Z0-9]+)[)]"
    mo = re.match(pattern, user_agent)
    if not mo:
        pattern2 = "[S|s][A|a][F|f][E|e][L|l][I|i][F|f][E|e]/(\\S+) [(]([a-zA-Z0-9]+)[)]"
        mo = re.match(pattern2, user_agent)
        if not mo:
            return None

    result = GuardlinerData(model_name="SafeLife", model_version=mo.group(1), serial_number=mo.group(2))
    return result


# @v1.post("/events", dependencies=[
#     Depends(check_kit_id),                                                              # проверка номера комплекта
#     Depends(CheckJsonSchema(schema_path=json_schema_path.joinpath('v1_events.json'))),  # вызов Совы
#     Depends(check_mime),                                                                # проверка content-type
#     Depends(CheckMtlsSert(kit_id=None))                                                 # проверка сертификата комплекта
# ])
# async def register_events(request: Request, conn: DBConnection, events: List[EventDesc]):
#     """API приёма универсальных событий"""
#     api_path, resp, stat, ll = request.url.path, 'OK', 201, ' OK, events added'  # ll - строка лога (log line)
#     kit_id = int(request.headers.get("X-MCC-ID"))
#     utcnow = datetime.utcnow()
#
#     logger.info(f"\n\t=>\t\t{api_path} ({register_events.__doc__.strip()}), kit_id={kit_id} started")
#
#     # Изменение статуса активности клиента (connected, disconnected или long_been_disconnected)
#     await db.sp_monitor_db_upd_activity(conn, utcnow, kit_id, 'connected')
#
#     # Сначала обработаем браслет, для него есть отдельная ХП
#     guard_liner: Optional[GuardlinerData] = find_guardliner(request.headers.get("user-agent"))
#     if guard_liner:
#         try:
#             # Обновление статуса подключения устройства. Заполнение mobile_connection.
#             # Регистрация события <Подключение МСК>, если не было 15 минут активности до этого
#             await db.sp_event_imdm_add_connect(conn, utcnow, kit_id, utcnow, '', 'not_defined')
#
#             await set_mob_param(conn,  # Регистрация параметров устройства
#                                 kit_id=kit_id,
#                                 os_name=guard_liner.model_name + " " + guard_liner.model_version,
#                                 model_name=guard_liner.model_name + " " + guard_liner.model_version,
#                                 serial_num=guard_liner.serial_number)
#             ll += f"\n\t\t\tGuardliner = {guard_liner.__dict__}"
#         except Exception as e:
#             logger.exception(f"kit_id={kit_id}: Not save mob_param: {str(guard_liner)}", e)
#             raise
#
#     # Запишем события в БД (ts - это timestamp)
#     for event in events:
#         try:
#             content = event.model_dump().get("event")
#             ts_kit = event.model_dump().get('timestamp')
#             ts_kit = datetime.fromtimestamp(float(ts_kit) / 1000) if isinstance(ts_kit, int) else ts_kit
#             await add_universal_event(conn, ts_kit, kit_id, content)
#             ll += "\n\t\t\t" + trunc_str(f"event={content}, timestamp={ts_kit}")
#
#         except Exception as e:
#             logger.exception(f"\n\t\t\tkit_id {kit_id} Not save uevents\n\t\t\t{trunc_str(event)}", e)
#             raise
#
#     ll = f"\n\t<=\t\t{api_path}, kit_id={kit_id} ended" + ll
#     logger.info(ll) if 200 <= stat < 300 else logger.error(ll)
#
#     return PlainTextResponse(resp, status_code=stat)
#
# if __name__ == '__main__':
#     pass
