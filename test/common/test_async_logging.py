# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient

from app.app_init import app


@pytest.mark.asyncio
async def off_test_root():
    """Асинхронный тест логирования"""
    app_uid = 'test_app_uid'   # replace with a test app_uid
    app_id = 'test_app_id'     # replace with a test app_id
    async with AsyncClient(app=app, base_url="http://test") as ac:
        for _ in range(5):
            response = await ac.get(f"api/v1/apps/{app_uid}/icons/{app_id}")
