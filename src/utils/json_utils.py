#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from json import loads


def isjson(verifiable):
    """Проверка json на корректность"""
    """Возвращает True при успехе и False, если json некорректный.
    """
    try:
        _ = loads(verifiable)
        result = True
    except ValueError:
        result = False
    except TypeError as e:
        print(f"({isjson.__doc__}) - Неверный тип аргумента, ожидались строка, байты или массив байт {verifiable}\n{e}")
        raise
    except Exception as e:
        result = False
        print(f"({isjson.__doc__}) - Неожиданная ошибка при разборе json {verifiable}\n{e}")

    return result


def tojson(verifiable: str | bytes | bytearray) -> list | dict | None:
    """Попытка загрузить json"""
    """Возвращает json при успехе или None, если json некорректный.
    """
    try:
        result = loads(verifiable)
    except ValueError:
        result = None
    except TypeError as e:
        print(f"({isjson.__doc__}) - Неверный тип аргумента, ожидались строка, байты или массив байт {verifiable}\n{e}")
        raise
    except Exception as e:
        result = None
        print(f"({tojson.__doc__}) - Неожиданная ошибка при разборе json {verifiable}\n{e}")

    return result
