# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
import json

from app.app_init import app


@pytest.mark.asyncio
async def test_async_logging():
    """Асинхронный тест для проверки уникальности номера запроса в контексте разных экземпляров корутины"""
    app_uid = 100
    app_id = 500

    async with AsyncClient(app=app, base_url="http://test") as ac:
        bodies = [{"appsDevice": [{"uid": "Русское поле", "versionName": "1.5", "enabled": True}], "appsContainer": []},
                  {"appsDevice": [{"title": "ru.niisokb.safestore", "versionCode": "1010"}], "appsContainer": []},
                  {"appsDevice": [{"uid": "НИИ СОКБ", "versionCode": "1001005", "enabled": True}]},
                  {"appsDevice": [{"title": "SafeStore", "enabled": True}], "appsContainer": []},
                  {"appsDevice": [{"uid": "Супер-пупер", "versionCode": "16", "enabled": False}]}
                  ]
        for body in bodies:
            body = json.dumps(body, ensure_ascii=False)
            response = await ac.post(url=f"api/v1/apps/{app_uid}/icons/{app_id}", content=body)
