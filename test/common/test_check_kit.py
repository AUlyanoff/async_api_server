# -*- coding: utf-8 -*-
import json
from typing import NamedTuple

import database
from test.conftest import DefaultOut


class KitMock(NamedTuple):
    mob_id: int


def test_correct_kit(client):
    database.db.sp_kit_imdm_get.return_value = DefaultOut(0, ''), [KitMock(mob_id=102)]
    database.db.sp_certificate_imdm_authentication.return_value = DefaultOut(0, ''),
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '102', 'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 201
    assert response.content == b'OK'


def test_missing_kit_header(client):
    response = client.post(
        "/api/v1/events",
        headers={'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 400
    assert response.content == b'{"error":"HTTP header \'X-MCC-ID\' not found in req"}'


def test_empty_kit_header(client):
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '', 'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 412
    assert response.content == b'{"error":"HTTP header \'X-MCC-ID\' contains an empty string"}'


def test_wrong_kit_header(client):
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': 'sdf', 'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 412
    assert response.content == b'{"error":"Kit_id=\'sdf\' is not a positive integer"}'


def test_zero_kit_header(client):
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '0', 'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 412
    assert response.content == b'{"error":"kit_id is zero"}'


def test_db_missing_kit_header(client):
    database.db.sp_kit_imdm_get.return_value = DefaultOut(0, ''), []
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '123123', 'Content-Type': 'application/json'},
        content=json.dumps([])
    )
    assert response.status_code == 475
    assert response.content == b'{"error":"kit_id=123123 not found in database"}'
