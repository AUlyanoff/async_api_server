# -*- coding: utf-8 -*-
from fastapi import APIRouter
from serv.endpoint_monitor import EPMonitor

v1 = APIRouter(route_class=EPMonitor)  # класс EPMonitor наблюдает за окончанием ендпойнта, это пред и пост обработка
