# -*- coding: utf-8 -*-
from logging import DEBUG, INFO, WARNING, ERROR, FATAL

# численные значения уровней логирования, устанавливает синонимы
logging_levels = {
    "DEBUG": DEBUG,  # 10
    "D": DEBUG,  # 10
    "T": DEBUG,  # 10
    "INFO": INFO,  # 20
    "I": INFO,  # 20
    "WARNING": WARNING,  # 30
    "WARN": WARNING,  # 30
    "W": WARNING,  # 30
    "ERROR": ERROR,  # 40
    "E": ERROR,  # 40
    "FATAL": FATAL,  # 50
    "F": FATAL,  # 50
    "CRITICAL": FATAL,  # 50
    "C": FATAL,  # 50
}

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

color = {
    0: '\x1b[0m',               # сброс цвета к системному
    DEBUG: '\x1b[38;21m',       # серый
    INFO: '\x1b[38;21m',        # серый
    WARNING: '\x1b[38;5;39m',   # голубой
    ERROR: '\x1b[31m',          # красный
    FATAL: '\x1b[31m'           # красный
}
