# -*- coding: utf-8 -*-
from fastapi import APIRouter
from utils.log.req_resp_log import LogReqRes

v2 = APIRouter(route_class=LogReqRes)     # класс LogReqRes добавляет логирование запроса и ответа
