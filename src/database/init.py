# -*- coding: utf-8 -*-
import logging
from sqlalchemy import URL, inspect
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

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
    async def get_tables():
        """Читаем список всех таблиц"""
        async with async_engine.connect() as conn:
            # асинхронно не работает, см. https://docs.sqlalchemy.org/en/20/errors.html#no-inspection-available
            tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_table_names())
        return tables

    db_tables = await get_tables()

    # красивое логирование параметров базы
    db_conf_dict = db_url._asdict()
    db_conf_dict.pop('query', None)
    db_conf_dict['password'] = len(db_conf_dict['password']) * '*'
    db_conf_dict['driver'] = async_engine.driver
    db_conf_dict['dialect'] = async_engine.dialect.name
    db_conf_dict['total tables found'] = f'{len(db_tables)} ({", ".join(db_tables[:5])}...)'
    _ll = ''.join([f'\n\t{k:<25} \t= {v}' for k, v in db_conf_dict.items()])
    boot.info(f'Database initialized successfully: {_ll}')

    return None


