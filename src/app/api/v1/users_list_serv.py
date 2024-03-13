# import logging
#
# import psycopg2
# from sqlalchemy import select
#
# from app.app_init import Session
# from database.tables import users
#
# logger = logging.getLogger(__name__)
#
#
def get_users_list():
    """Получить список зарегистрированных пользователей"""
    result = None
#     query = select(users.c.name, users.c.email)
#     try:
#         with Session() as session:
#             result = session.execute(query).mappings().all()
#     except psycopg2.OperationalError as e:
#         logger.error(f"\n\tUnsuccessful attempt database reading.\n\t{e}")
#     except Exception as e:
#         logger.error(f"\n\tUnexpected database error.\n\t{e}")
    return result


def serialize(table):
    """Сериализация таблицы в json"""
    list_dicts = list()
#     if table is not None:
#         for row in table:
#             list_dicts.append(dict(row))  # преобразование mapping-объектов Алхимии в словари
    return list_dicts
