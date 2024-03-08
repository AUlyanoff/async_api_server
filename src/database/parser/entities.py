# -*- coding: utf-8 -*-
from typing import NamedTuple


class Argument(NamedTuple):
    name: str
    type: str | None
    db_type: str | None = None

    def __eq__(self, other):
        return self.name == other.name

    @property
    def nametype(self):
        """Имя и тип в python стиле"""
        return f'{self.name}: {self.type}'


class Cursor(NamedTuple):
    name: str
    class_name: str
    var_name: str
    args: list[Argument]


class Procedure(NamedTuple):
    name: str
    inargs: list[Argument]
    outargs: list[Argument]
    cursors: list[Cursor] = None
    cursor_annotations: str = None
    file_name: str = None
    description: str = None

    @property
    def upper_name(self):
        """Имя в верхнем регистре"""
        return self.name.upper()

    def __eq__(self, other):
        return set(self.inargs) == set(other.inargs) and set(self.outargs) == set(other.outargs)


def to_camel(field_name: str) -> str:
    """Конвертация snake_case в CamelCase"""
    return ''.join(word.capitalize() for word in field_name.split('_'))
