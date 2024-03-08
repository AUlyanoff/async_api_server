# -*- coding: utf-8 -*-
"""Место для пользовательских исключений приложения"""


class MtlsException(Exception):
    stat = None
    err = None
    proc = None

    def __init__(self, err, stat):
        self.stat = stat
        self.err = err
