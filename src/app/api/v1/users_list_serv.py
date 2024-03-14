import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.tables import users

logger = logging.getLogger(__name__)


async def get_users_list(session: AsyncSession):
    """Получить список зарегистрированных пользователей"""
    # result = None
    result = await session.execute(select(users))

    return result


def serialize(table):
    """Сериализация таблицы в json"""
    list_dicts = list()
#     if table is not None:
#         for row in table:
#             list_dicts.append(dict(row))  # преобразование mapping-объектов Алхимии в словари
    return list_dicts
