# -*- coding: utf-8 -*-
import json
import logging
import sys
from datetime import datetime
from typing import Dict, Optional

from database import DBConnection, db
from utils.log.utils import trunc_str

logger = logging.getLogger("logger_universal_event")


async def add_universal_event(conn: DBConnection, ts_kit: Optional[datetime], kit_id: int, content: Dict):
    """Регистрация события МСК (json)"""
    """В случае ошибки записи в БД, ошибка только логируется, API пытается продолжить выполнение
    """
    logger.debug(f"\n\t~>\t\tAdd universal event ({add_universal_event.__doc__}), kit_id={kit_id} started")
    resp = 'ended ok'
    event = json.dumps(content, ensure_ascii=False).encode("utf-8")
    ts_kit = datetime.utcnow() if not ts_kit else ts_kit
    try:
        ll = f"\n\t<~\t\tAdd universal event kit_id={kit_id}, "

        out, = await db.sp_event_imdm_add_json(conn, datetime.utcnow(), kit_id, ts_kit, event)
        if out.o_rc == -3303:
            resp = "failed\n\t\t\tDevice params not registered: Device not found"
        elif out.o_rc != 0:
            resp = f"failed\n\t\t\tDevice params not registered: Unexpected o_rc={out.o_rc} ({out.o_err})"

        ll += resp + f"\n\tdata\t{trunc_str(content)}"
        logger.debug(ll) if out.o_rc == 0 else logger.error(ll)
    except Exception as e:  # not use PEP 8, Oracle driver create DatabaseError not by Exception-super
        error = sys.exc_info()[1]
        logger.exception(f"sp_event_imdm_add_json: {error}\n", e)

    return None
