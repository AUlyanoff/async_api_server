# -*- coding: utf-8 -*-
import logging

# Базовые url для API
BASE_URL_STORE = "/store"
BASE_URL_API_V1 = "/api/v1"
BASE_URL_API_V2 = "/api/v2"
BASE_URL_API_V3 = "/api/v3"
BASE_URL_API_V4 = "/api/v4"
JWT_COOKIE = "jwt_cookie"

APPLICATION_JSON = "application/json"

# численные значения уровней логирования, устанавливает синонимы
logging_levels = {
    "DEBUG": logging.DEBUG,         # 10
    "D": logging.DEBUG,             # 10
    "T": logging.DEBUG,             # 10
    "INFO": logging.INFO,           # 20
    "I": logging.INFO,              # 20
    "WARNING": logging.WARNING,     # 30
    "WARN": logging.WARNING,        # 30
    "W": logging.WARNING,           # 30
    "ERROR": logging.ERROR,         # 40
    "E": logging.ERROR,             # 40
    "FATAL": logging.FATAL,         # 50
    "F": logging.FATAL,             # 50
    "CRITICAL": logging.FATAL,      # 50
    "C": logging.FATAL,             # 50
}

# Наименования конфигурационных файлов
IOSMDM = "iosmdm"
REGPORTAL = 'regportal'

# Константы JWT сессии
SESSION_USER_ID = "auth_provider_user_id"
SESSION_MONITOR_UID = "monitor_uid"
SESSION_KIT_ID = "kit_id"
SESSION_OWNERSHIP = "ownership"
SESSION_ACCESS_TOKEN = "AuthCode-access-token"
SESSION_KEY_USER_AGREEMENT = "SESSION_KEY_USER_AGREEMENT"
SESSION_TYPE = "session_type"

# Судя по всему не используется, но оставлю пока
KNOX_KEY = "34AA6EFC5855F6E95117838285E73C42" \
           "BCDCAB0DD37179A0B5B00BE4B590D63A" \
           "F0A7DF2AA066DC0F3DA9C01E9E296D15" \
           "94390DC03E3769969F37117E2E95C70B"

db_errs = {
    '08001': "SQL-client unable to establish SQL-connection.",
    '08003': "Connection does not exist.",
    '08004': "SQL-server rejected establishment of SQL-connection.",
    '08006': "Connection failure.",
    '08007': "Transaction resolution unknown.",
    '08P01': "Protocol violation.",
    '57P01': "Operator Intervention. Admin shutdown.",
    '57014': "Operator Intervention. Query canceled.",
    '57P02': "Operator Intervention. Crash shutdown.",
    '57P03': "Operator Intervention. Cannot connect now.",
    '57P04': "Operator Intervention. Database dropped.",
    '25P03': "Operator Intervention. Idle session timeout.",
    '53100': "Insufficient Resources. Disk full.",
    '53200': "Insufficient Resources. Out of memory.",
    '53300': "Insufficient Resources. Too many connection.",
    '53400': "Insufficient Resources. Configuration limit exceeded."
}
