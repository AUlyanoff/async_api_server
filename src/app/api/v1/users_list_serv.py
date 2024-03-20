import logging

from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy import select
from database.tables import users
from sqlalchemy.exc import InterfaceError

logger = logging.getLogger(__name__)


async def get_users_list(conn: AsyncConnection):
    """Получить список зарегистрированных пользователей"""
    result = None
    try:
        result = await conn.execute(select(users))
    except InterfaceError as e:
        logger.error(f'\nInterfaceError {e.code}, {e.orig.args[0].split(">: ")[-1]}\n{70 * "="}\n{e}')
        raise
    except Exception as e:
        logger.error(f'\n{80*"-"}\n{e}')  # e.code == 'rvf5', e.orig.args[0].split('>: ')[-1] == 'connection is closed'
        raise

    return result.fetchall()


def serialize(table):
    """Сериализация таблицы в json"""
    list_dicts = list()
    if table is not None:
        for row in table:
            row_dict = row._asdict()    # преобразование mapping-объектов Алхимии в словари
            row_dict.pop('avatar', None)
            row_dict.pop('psw', None)
            if row_dict.get('time'): row_dict['time'] = row_dict.get('time').isoformat()[:-3]+'Z'
            list_dicts.append(row_dict)
    return list_dicts
