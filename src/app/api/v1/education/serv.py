#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from asyncio import sleep


logger = logging.getLogger(__name__)


async def log_it(app_uid, app_id):
    """Вызов второго уровня"""
    """Тестовая функция, вызывает slow(), будет удалена"""
    logger.info(f"\n\t~>\t\t({log_it.__doc__}), education function started...")
    await sleep(0)  # возврат в цикл управления
    await slow()
    logger.info(f"\n\t<~\t\t({log_it.__doc__}), education function ended")

    return


async def slow():
    """Вызов третьего уровня"""
    """Тестовая функция, ждёт секунду, будет удалена"""
    logger.info(f"\n\t~>\t\t({slow.__doc__}), education function started...")
    await sleep(0)  # возврат в цикл управления и после этого ждём секунду
    logger.info(f"\n\t<~\t\t({slow.__doc__}), education function ended")

    return
