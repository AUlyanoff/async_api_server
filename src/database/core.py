# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession
from init import async_session


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
