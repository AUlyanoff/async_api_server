# -*- coding: utf-8 -*-

import json
from typing import NamedTuple

import database
from config import config
from test.conftest import DefaultOut


class KitMock(NamedTuple):
    mob_id: int


def test_sowa_not_json_body(client):
    config.sowa = True
    database.db.sp_kit_imdm_get.return_value = DefaultOut(0, ''), [KitMock(mob_id=102)]
    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '102', 'Content-Type': 'application/json'},
        content='nkejbrgjerbg'
    )
    config.sowa = False
    assert response.status_code == 400
    # assert response.content == b'{"error":"Request must be empty list [] or correct json"}'
    assert response.content == b'Bad request. Invalid json'


def test_sowa_incorrect_body(client):
    config.sowa = True
    database.db.sp_kit_imdm_get.return_value = DefaultOut(0, ''), [KitMock(mob_id=102)]
    # неправильный первый ключ
    event_example = {
        "channel": "MDM",
        "event": {"dsfgneodrgnerg": "EventIpAddress", "event_format_version": 1, "event_code": 89,
                  "event_uuid": "1eb37572-9c2f-4557-aaee-3daa9e9bb974", "network_type": "wifi",
                  "ip_address": "10.17.15.142"}, "timestamp": 1704800085633
    }

    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '102'},
        content=json.dumps([event_example])
    )
    config.sowa = False
    assert response.status_code == 400
    assert response.content == b'{"error":"Invalid request. Validation by JSON schema completed unsuccessfully"}'


def test_sowa_correct_body(client):
    config.sowa = True
    database.db.sp_kit_imdm_get.return_value = DefaultOut(0, ''), [KitMock(mob_id=102)]
    database.db.sp_certificate_imdm_authentication.return_value = DefaultOut(0, ''),
    event_example = {
        "channel": "MDM",
        "event": {"serializedType": "EventIpAddress", "event_format_version": 1, "event_code": 89,
                  "event_uuid": "1eb37572-9c2f-4557-aaee-3daa9e9bb974", "network_type": "wifi",
                  "ip_address": "10.17.15.142"}, "timestamp": 1704800085633
    }
    database.db.sp_event_imdm_add_json.return_value = DefaultOut(0, ''),

    response = client.post(
        "/api/v1/events",
        headers={'X-MCC-ID': '102', 'Content-Type': 'application/json'},
        content=json.dumps([event_example])
    )
    config.sowa = False
    assert response.status_code == 201
    assert response.content.decode() == 'OK'
