#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import logging
from pathlib import Path
from textwrap import fill

from cryptography import x509
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger(__name__)


def validate_cert(cert_data: str | Path | bytes, *_) -> (str | Path | bytes | None, str | None):
    """Проверка валидности x509 сертификата
    Проверяет следующее:
    1. Наличие сертификата по переданному пути, наличие доступа, валидность файла
    2. Время жизни сертификата
    Возвращает сам сертификат (путь или байты) и строку ошибки (если есть)
    Такое поведение нужно чтобы была возможность использовать эту функцию в валидаторе Pydantic
    """

    match cert_data:
        case str() | Path():
            logger.fatal(f'Checking certificate on {cert_data}...')
            try:
                with open(cert_data, 'rb') as cert_file:
                    cert = x509.load_pem_x509_certificate(cert_file.read())
            except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
                return None, f'Error opening certificate file: {e}'
            except ValueError as e:
                return None, f'Error parsing certificate on {cert_data}: {e}'

        case bytes():
            logger.debug(f'Checking certificate with bytes: {fill(cert_data.decode())}')
            try:
                cert = x509.load_pem_x509_certificate(cert_data)
            except ValueError as e:
                return None, f'Error parsing certificate: {e}'

        case None:
            return None, 'Cert data is empty'
        case _:
            return None, 'Wrong parameters for validate_cert function'

    fingerprint = cert.fingerprint(hashes.SHA1()).hex()
    logger.debug(f'Сertificate {fingerprint} was read successfully')

    if cert.not_valid_before < datetime.datetime.now() < cert.not_valid_after:
        logger.debug(f'Сertificate {fingerprint} is valid from {cert.not_valid_before} to {cert.not_valid_after}')
    else:
        return None, f'Сertificate {fingerprint} has expired at {cert.not_valid_after}'

    return cert_data, None
