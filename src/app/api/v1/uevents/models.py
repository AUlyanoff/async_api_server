#!/usr/bin/env python
from typing import Literal
from pydantic import BaseModel, PositiveInt


class EventDesc(BaseModel):
    """Минимальное описание внешних атрибутов события: источник, время, само событие"""
    timestamp: PositiveInt
    channel: Literal['MDM'] = 'MDM'
    event: dict     # делает невозможным частичную обработку пакета событий (аналог break в цикле перебора событий)
