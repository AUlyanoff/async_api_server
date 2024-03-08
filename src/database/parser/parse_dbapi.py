# -*- coding: utf-8 -*-
import json
import os

from database.parser.entities import Procedure, Argument, to_camel, Cursor
from utils.paths import json_path

api_mapper = {
    '$BLOB_TYPE': 'dict',
    '$BOOL_TYPE': 'bool',
    '$CLOB_TYPE': 'dict',
    '$ID_TYPE': 'int',
    '$INT': 'int',
    '$NUM_10': 'float',
    '$STR_1024': 'str',
    '$STR_2048': 'str',
    '$STR_BASE': 'str',
    '$STR_LONG': 'str',
    '$STR_NAME': 'str',
    '$TS_TYPE': 'datetime'

}


def parse_dbapi() -> dict[str, Procedure]:
    """
    Сканирует DbAPI, получает названия процедур, их входные/выходные параметры,
    названия курсоров и состав их полей (при наличии)
    :return: словарь типа имя процедуры: объект процедуры
    """
    api_procedures = dict()
    types_set = set()
    for address, dirs, files in os.walk(json_path):
        for name in [file for file in files if file.find('sp_') != -1]:
            with open(os.path.join(address, name), 'r') as file:
                data = json.loads(file.read())

            proc_name = f"sp_{data['package']}_{data['component']}_{data['name']}"

            in_args = list()
            out_args = list()

            # Парсинг входных аргументов
            for arg in data.get('args', {}).get('in', []):
                if isinstance(arg, str):
                    in_args.append(Argument(arg, None, None))
                elif isinstance(arg, dict):
                    in_args.append(Argument(arg['name'], None, None))

            # Парсинг выходных аргументов
            for arg in data.get('args', {}).get('out', []):
                if isinstance(arg, str):
                    out_args.append(Argument(arg, None, None))
                elif isinstance(arg, dict):
                    out_args.append(Argument(arg['name'], None, None))

            # Парсинг курсоров
            refcursors = data.get('resultSet', [])
            if isinstance(refcursors, dict):
                refcursors = [refcursors]

            parsed_cursors = []
            for cur in refcursors:
                arg_list = []
                for arg in cur.get('objects', []):
                    if isinstance(arg, str):
                        arg_list.append(Argument(arg.replace('$', ''), 'Any'))
                    elif isinstance(arg, dict):
                        types_set.add(arg.get('type'))
                        arg_list.append(Argument(arg['name'].replace('$', ''), api_mapper.get(arg.get('type'), 'Any')))

                parsed_cursors.append(Cursor(cur['name'], to_camel(cur['name']) + 'RS', cur['name'] + '_rs', arg_list))

            api_procedures[proc_name] = Procedure(
                name=proc_name,
                inargs=in_args,
                outargs=out_args,
                cursors=parsed_cursors,
                file_name=name,
                description=data.get('desc', '')
            )

    return api_procedures
