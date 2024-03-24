# -*- coding: utf-8 -*-
from fastapi import APIRouter
from serv.log_req_fastapi import LogReqRes

v1 = APIRouter(route_class=LogReqRes)     # класс LogReqRes добавляет логирование запроса и ответа
