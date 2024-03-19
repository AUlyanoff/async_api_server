import logging

from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession
from sqlalchemy import select
from database.tables import users

logger = logging.getLogger(__name__)


async def get_users_list(conn: AsyncConnection):
    """Получить список зарегистрированных пользователей"""
    # result = None
    result = await conn.execute(select(users))

    return result.fetchall()


def serialize(table):
    """Сериализация таблицы в json"""
    list_dicts = list()
    if table is not None:
        for row in table:
            row_dict = row._asdict()
            row_dict.pop('avatar', None)
            row_dict.pop('psw', None)
            if row_dict.get('time'): row_dict['time'] = row_dict.get('time').strftime('%d-%m-%Y %H:%M:%S')
            list_dicts.append(row_dict)  # преобразование mapping-объектов Алхимии в словари
    return list_dicts
