# -*- coding: utf-8 -*-
from fastapi import APIRouter
from services.req_resp_log import LogReqRes

v1 = APIRouter(route_class=LogReqRes)     # класс LogReqRes добавляет логирование запроса и ответа
