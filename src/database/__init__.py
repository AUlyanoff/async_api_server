# -*- coding: utf-8 -*-
from typing import Annotated

from asyncpg import Connection
from fastapi import Depends

from database.core import Database

db: Database = Database()

# Dependency для FastApi
DBConnection = Annotated[Connection, Depends(db.connection_pool_dependency)]
