# -*- coding: utf-8 -*-
from sys import exc_info
from datetime import datetime
from logging import getLogger

from database import db

logger = getLogger(__name__)


async def set_mob_param(conn, kit_id, os_name, model_name=None, imei=None, udid=None, serial_num=None):
    """Регистрация параметров устройства
       В случае ошибки записи в БД, ошибка только логируется, API пытается продолжить выполнение
    """
    try:
        out, = await db.sp_monitor_imdm_set_mob_param(conn,
                                                      datetime.utcnow(),    # время на сервере
                                                      kit_id,
                                                      datetime.utcnow(),    # время на МСК todo это правильно? SM-322
                                                      os_name,
                                                      model_name,
                                                      imei,
                                                      udid,
                                                      serial_num)
        if out.o_rc == -3303:
            logger.error("Device params not registered: Device not found")
        elif out.o_rc == -11901:
            logger.error("Device params not registered: Operation system platform not found")
        elif out.o_rc != 0:
            logger.error(f"Device params not registered: Unexpected o_rc={out.o_rc} ({out.o_err})")

    except Exception:
        ex_type, ex_value = exc_info()[0], exc_info()[1]
        logger.exception("Device params not registered: Unexpected error\n\t", ex_type, '\n\t', ex_value)

    return None
