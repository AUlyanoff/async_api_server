# -*- coding: utf-8 -*-
import logging
import pickle
from functools import cache
from typing import Tuple

from asyncpg import Connection
from asyncpg.exceptions import PostgresError

from database.exceptions import DatabaseException, ResultCheckException
from database.parser.entities import Procedure
from utils.paths import SRC_PATH
from utils.log.utils import trunc_str

logger = logging.getLogger('__stored_proc__')


@cache
def read_procedures() -> dict[str, Procedure]:
    """Читает процедуры из файла и кладёт в структуру данных
    Функция кеширована, делает это один раз
    """
    path = SRC_PATH / 'database' / 'procedures' / 'proc_signature.pickle'

    with open(path.resolve(), 'rb') as file:
        cached_procedures = pickle.loads(file.read())

    return cached_procedures


class BaseProcedure:

    def __init__(self):
        self.cached_procedures = read_procedures()

    async def __call__(self, connection: Connection, name: str, *args, check_rc: bool = False) -> Tuple:
        """
        Вызов хранимой процедуры
        :param connection: соединение с БД
        :param name: наименование хранимой процедуры
        :param args: аргументы в порядке, указанном в процедуре
        :return: объект Record с out args процедуры, list[Record] с данными курсора (при наличии)
        """
        proc_info = self.cached_procedures.get(name)
        async with connection.transaction():
            try:
                _ll = f"\n\t->\t\t{name} ({proc_info.description}) [{proc_info.file_name}] started"
                # параметры для строки sql по числу переданных args: %1, %2, %3 ...
                params = ', '.join([f"${num}" for num in range(1, len(args) + 1)])

                in_args = list()  # логирование входных параметров
                for i, value in enumerate(args):
                    value = value.decode() if hasattr(value, 'decode') else value
                    in_args.append(f'{proc_info.inargs[i].db_type} {proc_info.inargs[i].name}={value}')
                _ll += f'\n\tin\t\t{trunc_str(", ".join(in_args))}'

                query = f'SELECT * FROM {name}({params})'           # формирование запроса к базе
                result = await connection.fetchrow(query, *args)    # выполнение и получение однострочного результата
                # from asyncpg.exceptions import TooManyConnectionsError -- отладочное исключение
                # if name == 'sp_kit_imdm_get': raise TooManyConnectionsError -- отладочное исключение

                # формирование имён курсоров формата <o_rs*> - формат по соглашению с БД
                cursor_names = [rs for rs in result.keys() if rs.find('o_rs') != -1]

                # логирование выходных параметров
                _ll += f'\n\tout\t\trc={result.o_rc}, err={result.o_err}, cursors={cursor_names}'

                if check_rc and result.o_rc != 0:
                    raise ResultCheckException(proc_name=name, rc=result.o_rc, err=result.o_err)

                # читаем и формируем результат - список курсоров cursor_results, в каждом курсоре список строк
                cursor_results = []
                for i, cursor_name in enumerate(cursor_names):
                    # если курсор пустой - пишем в качестве его результата пустой list
                    if not result[cursor_name]:
                        cursor_results.append([])
                        continue

                    fetch_query = f'FETCH ALL IN "{result[cursor_name]}";'  # формирование запроса на чтение курсора
                    cursor_value = await connection.fetch(fetch_query)      # чтение курсора
                    cursor_results.append(cursor_value)                     # складываем курсоры в список

                    items = 0   # логирование курсора: строки поштучно, поля накопительным итогом для всего курсора
                    for row in cursor_value:
                        items += len(row)
                    _ll += f'\n\t{"cursor" if i == 0 else "      "}\t' \
                           f'{str(cursor_name)+":":<{14 if len(cursor_names) > 1 else 0}} ' \
                           f'rows={len(cursor_value)}, items={items}'

                return result, *cursor_results

            except PostgresError as e:
                raise DatabaseException(proc_name=name, exc=e)
            finally:
                logger.debug(_ll)
