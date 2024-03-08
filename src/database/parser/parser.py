# -*- coding: utf-8 -*-
import asyncio
import logging
import pickle

import asyncpg
from jinja2 import Environment, FileSystemLoader

from config import config
from database import db
from database.parser.entities import Procedure
from database.parser.parse_database import parse_db
from database.parser.parse_dbapi import parse_dbapi
from utils.paths import SRC_PATH

logger = logging.getLogger(__name__)

env = Environment(
    loader=FileSystemLoader("/")
)

ProcedurePath = SRC_PATH / 'database' / 'procedures'


async def update_procedures():
    """Обновляет список процедур в файлах
    src/database/procedures/__init__.py
    src/database/procedures/procedure_list.py
    """
    logger.info('Updating procedure list')
    db.set_config(config.db)
    connection = await db.get_connection()
    db_procedures = await parse_db(connection)
    api_procedures = parse_dbapi()

    # if db_procedures.keys() == api_procedures.keys():
    #     return

    logger.warning('Present in DB, missing in DbAPI:')
    logger.warning(set(db_procedures.keys()).difference(set(api_procedures.keys())))
    logger.warning('Present in DbAPI, missing in DB:')
    logger.warning(set(api_procedures.keys()).difference(set(db_procedures.keys())))

    united_procedures = []
    for name in db_procedures.keys() & api_procedures.keys():
        united_procedures.append(Procedure(
            name=name,
            inargs=db_procedures[name].inargs,
            outargs=db_procedures[name].outargs,
            cursors=api_procedures[name].cursors,
            cursor_annotations=', '.join('list[{}]'.format(cur.class_name) for cur in api_procedures[name].cursors),
            file_name=api_procedures[name].file_name,
            description=api_procedures[name].description
        ))

    proc_template = env.get_template(str(ProcedurePath.joinpath('procedure_list.jinja2')))
    init_template = env.get_template(str(ProcedurePath.joinpath('__init__.jinja2')))

    with open(ProcedurePath.joinpath('procedure_list.py'), "w") as file:
        file.write(proc_template.render(procedures=sorted(united_procedures)))

    with open(ProcedurePath.joinpath('__init__.py'), "w") as file:
        file.write(init_template.render(procedures=sorted(united_procedures)))

    with open(ProcedurePath.joinpath('proc_signature.pickle'), 'wb') as file:
        pickle.dump({proc.name: proc for proc in united_procedures}, file)


# noinspection PyBroadException
async def check_database(connection: asyncpg.Connection):
    """Запускается на старте FastApi, проверяет соответствие сигнатур хп в БД сигнатурам сохранённых ХП
    :param connection: соединение с БД asyncpg
    """
    _ll = 'Check database procedures started'
    try:
        if not SRC_PATH.joinpath('proc_signature.pickle').is_file():
            _ll += '\nproc_signature.pickle file not found, check skipped'
            logger.warning(_ll)
            return

        db_procedures = await parse_db(connection)

        with open(SRC_PATH.joinpath('proc_signature.pickle'), 'rb') as file:
            cached_procedures = pickle.loads(file.read())

        if cached_procedures != db_procedures:
            logger.warning('Present in DbAPI, missing in DB:')
            logger.warning(set(db_procedures.keys()).difference(set(cached_procedures.keys())))
            logger.warning('Present in code, missing in DB:')
            logger.warning(set(cached_procedures.keys()).difference(set(db_procedures.keys())))

    except BaseException as exc:
        _ll += f'\nError checking database procedures: {exc}'
        logger.warning(_ll)


if __name__ == '__main__':
    asyncio.run(update_procedures())
