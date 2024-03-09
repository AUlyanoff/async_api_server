# -*- coding: utf-8 -*-
import logging

from fastapi import Request, APIRouter

from database import db, DBConnection
from utils.log.req_resp_log import LogReqRes

ios_router = APIRouter(route_class=LogReqRes)

logger = logging.getLogger(__name__)


@ios_router.put("/mdm")
async def mdm(request: Request, conn: DBConnection):
    """Тестовый роут"""
    res, rc = await db.sp_kit_imdm_get_next_command_for_ios(conn, 102)
    res, = await db.sp_monitor_imdm_get_device_token(conn, 102)
    res, ws, uids, policy = await db.sp_profile_imdm_get_ios_monitor_profile(conn, 102)
    return ''
