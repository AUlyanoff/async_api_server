# -*- coding: utf-8 -*-
import sys
import logging
from sqlalchemy import URL, inspect, MetaData, create_engine
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker
from asyncpg.exceptions import InternalServerError

from config.db import db_cfg


boot = logging.getLogger('boot')
boot.info('Database initialization started')

db_url = URL.create('postgresql+asyncpg',
                    database=db_cfg.name,
                    username=db_cfg.user,
                    password=db_cfg.password,
                    host=db_cfg.host,
                    port=db_cfg.port,
                    )
async_engine = create_async_engine(db_url, echo=False)
Base = declarative_base()
async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def db_init():
    """Пытаемся связаться с базой и залогировать параметры успешной попытки"""
    def get_table_names(conn):
        """Читаем список всех таблиц"""
        inspector = inspect(conn)
        return inspector.get_table_names()

    async def sync_async(request):
        """ Inspector асинхронно не работает, см. https://docs.sqlalchemy.org/en/20/errors.html#no-inspection-available
            Поэтому вызываем синхронную сущность из асинхронного коннекта синхронным методом .run_sync
        """
        async with async_engine.connect() as conn:
            result = await conn.run_sync(request)
            # await conn.run_sync(Base.metadata.reflect(async_engine))
            # await conn.run_sync(Base.metadata.drop_all)
        return result

    try:
        table_names = await sync_async(get_table_names)
    except InternalServerError as e:
        if e.sqlstate == 'XX000':
            if 'password authentication failed' in getattr(e, "message", ""):
                boot.info('Check host, user or password...')
                sys.tracebacklimit = 0  # страусов не пугать, пол бетонный
            elif 'database ' + db_cfg.name + ' does not exist' in getattr(e, "message", "").replace('"', ''):
                boot.info('Check DB name...')
                sys.tracebacklimit = 0
        raise
    except TimeoutError as e:
        boot.info(f'Timeout with DB-connecting, check db_url={db_url} {e}')
        sys.tracebacklimit = 0
        raise

    # красивое логирование параметров базы
    _dict = db_url._asdict()
    _dict.pop('query', None)
    _dict.update(
        password=len(_dict['password']) * '*',
        driver=async_engine.driver,
        dialect=async_engine.dialect.name,
        total_tables_found=f'{len(table_names)} ({", ".join(table_names[:5])}...)'
    )
    boot.info(f'Database initialized successfully: ' + ''.join([f'\n\t{k:<16} \t= {v}' for k, v in _dict.items()]))

    return None


