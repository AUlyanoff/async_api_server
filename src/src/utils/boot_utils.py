# -*- coding: utf-8 -*-
import logging
import sys
from os import environ
from sys import exit

from config import config as cfg
from database import db

logger = logging.getLogger(__name__)  # свой собственный логер


async def get_components_versions(extend: dict = None):
    """Читает версии компонентов и БД и печатает их в лог
    :param extend: словарь расширения, использовать если нужно принудительно передать версию компонента, или что-то ещё
    :return:
    """

    if extend is None:
        extend = {}

    components = ('ARM_VERSION', 'SOCKET_SERVER_VERSION', 'SCEP_VERSION', 'WINMDM_VERSION',
                  'FCM_PUSH_SERVER_VERSION', 'MDM_SERVER_VERSION', 'REG_PORTAL_VERSION')
    versions = {component: environ.get(component, extend.get(component, None)) for component in components}
    for key in extend.keys() - versions.keys():
        versions[key] = extend[key]

    lggr_sp = logging.getLogger('__stored_proc__')  # выключим логер ХП
    lggr_sp.disabled = True

    async with db.get_connection_from_pool() as conn:
        try:
            out, = await db.sp_inst_schema_all_get_last_ver(conn)
            if out.o_rc == 0:
                versions['DB_VERSION'] = f'{out.o_version} (database info {out.o_ts})'
            else:
                versions['DB_VERSION'] = f'DB error rc={out.o_rc} err={out.o_err}'
        except Exception as e:
            versions['DB_VERSION'] = f'Unexpected DB error: {e}'
        finally:
            lggr_sp.disabled = False  # включим логирование ХП снова

    versions = {k: v for k, v in versions.items() if v is not None and v != ''}
    s = 'Component versions:'
    s += ''.join(sorted([f'\n\t{k:<16} \t= {v}' for k, v in versions.items()]))
    return s


async def check_application_version(shutdown=True) -> None:
    """
    Функция проверки совместимости приложения с базой данных
    :param shutdown: флаг завершения, если установлен, приложение будет принудительно завершено.
    :return: None
    """

    if cfg.db.type.lower() == 'mock':  # Если это тестирование, то совместимость не проверяется
        return

    async with db.get_connection_from_pool() as conn:
        lggr_sp = logging.getLogger('__stored_proc__')  # выключим логер ХП
        lggr_sp.disabled = True

        out, = await db.sp_components_imdm_version_check(conn)
        if out.o_rc != 0:                       # компонент и БД несовместимы
            logger.warning(f'{out.o_err} (DB code={out.o_rc})')
            if shutdown:                        # если мы в продакшене,
                sys.tracebacklimit = 0          # то подавим распечатку стека
                exit(out.o_rc)                  # и остановим сервер

        lggr_sp.disabled = False                # включим логирование ХП снова
