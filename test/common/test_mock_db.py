# -*- coding: utf-8 -*-
import json

from fastapi.testclient import TestClient

from app.app_init import app



def off_test_correct_kit():
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/events",
            headers={'X-MCC-ID': '102', 'Content-Type': 'application/json'},
            content=json.dumps([])
        )
        assert response.status_code == 201
        assert response.content == b'"OK"'
