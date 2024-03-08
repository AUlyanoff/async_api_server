# -*- coding: utf-8 -*-
import asyncpg

from database.parser.entities import Argument, Procedure

db_mapper = {
    'integer': 'int',
    'smallint': 'int',
    'bigint': 'int',

    'charactervarying': 'str',
    'text': 'str',

    'boolean': 'bool',

    'bytea': 'bytes',
    'jsonb': 'dict',
    'oid': 'str',
    'timestampwithouttimezone': 'datetime',

    'refcursor': 'str'
}


async def parse_db(connection: asyncpg.Connection) -> dict[str, Procedure]:
    """Парсит процедуры из БД в объекты Python
    :return: dict с ключем - имя процедуры, значение - объект процедуры
    """
    # noinspection SqlResolve
    result = await connection.fetch("""
        SELECT p.proname AS procedure_name,
               ns.nspname AS schema_name,
               pg_get_function_identity_arguments(p.oid) AS arguments,
               pg_get_function_result(p.oid) AS return_type
        FROM pg_proc p
        JOIN pg_namespace ns ON p.pronamespace = ns.oid
        WHERE proname ILIKE 'sp%imdm%'
        OR proname ILIKE '%get_last_ver%'
        OR proname ILIKE '%srv_event%'
        OR proname ILIKE '%loader_ldr_access%'
        OR proname ILIKE '%loader_ldr_auth%'
        OR proname ILIKE '%monitor_db_upd%'
        ;
        """)
    await connection.close()

    db_procedures = dict()

    for record in result:
        # Формирование сырого массива аргументов
        inout_args = [arg.strip().split(' ') for arg in record['arguments'].split(',')]

        # Формирование массива NamedTuple входных параметров + маппинг типов из словаря db_mapper
        in_args = [Argument(arg[0], db_mapper.get(''.join(arg[1:])), ''.join(arg[1:])) for arg in inout_args if
                   arg[0].startswith('i')]

        # Формирование массива NamedTuple выходных параметров + маппинг типов из словаря db_mapper
        out_args = [Argument(arg[1], db_mapper.get(''.join(arg[2:])), ''.join(arg[2:])) for arg in inout_args if
                    arg[0].startswith('OUT')]

        db_procedures[record['procedure_name']] = Procedure(
            name=record['procedure_name'],
            inargs=in_args,
            outargs=out_args
        )

    return db_procedures
