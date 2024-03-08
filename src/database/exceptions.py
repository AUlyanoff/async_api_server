# -*- coding: utf-8 -*-
class DatabaseException(Exception):

    def __init__(self, exc: Exception, proc_name: str = ''):
        self.exception = exc
        self.proc_name = proc_name
        super().__init__()


class ResultCheckException(Exception):
    """Исключение, вызываемое при проверке RC вызова хранимой процедуры"""

    def __init__(self, proc_name: str, rc: int, err: str):
        """
        :param proc_name: имя процедуры
        :param rc: код ошибки
        :param err: описание ошибки
        """
        self.proc_name = proc_name
        self.rc = rc
        self.err = err
        super().__init__()
