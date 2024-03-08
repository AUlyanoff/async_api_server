#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from fastapi import Request, HTTPException

import database
# from utils.exceptions import MtlsException

logger = logging.getLogger(__name__)


def check_mtls_cert(request: Request, kit_id: int) -> None:
    """Проверка отпечатка сертификата mTLS в X-Client-Certificate-Sha1"""

    cert_sha1 = request.headers.get('X-Client-Certificate-Sha1', '')  # отпечаток сертификата
    api_path = request.base_url[request.base_url.find('api', 1):]  # путь вызова API
    logger.debug(f"\n\t~>\tcheck_mtls_cert ({check_mtls_cert.__doc__}) for API {api_path} kit_id={kit_id} started"
                 f"\n\t\tX-Client-Certificate-Sha1='{cert_sha1}'")
    stat, err, res, err4log = None, None, None, None  # чтобы функция не упала от логирования

    if str(cert_sha1).strip() == '':
        # если заголовка нет или в нём пусто, то это или legacy-комплект, или ошибка Монитора, или ошибка nginx-а
        logger.info(f"HTTP header 'X-Client-Certificate-Sha1' not found or empty"
                    f" - This is either a legacy kit={kit_id}, or a Monitor error, or an nginx error")

    res, err4log = authentication(kit_id, cert_sha1)
    if res != 0:
        stat, err = 401, "Authentication error"
        if res == -20012:
            err4log = f"Certificate does not match this kit ({err4log})"
        elif res == -20001:
            err4log = f"Certificate not found ({err4log})"
        elif res == -20013:
            err4log = f"Certificate has expired or the expiration has not started ({err4log})"
        elif res == -20011:
            err4log = f"This kit isn't legacy, must have certificate ({err4log})"
        else:
            err4log = f"Unexpected db error ({err4log})"

    if stat is not None:
        logger.error(f"\n\t<~\tcheck_mtls_cert, error for API {api_path}, HTTP={stat}, ended"
                     f"\n\t\tfor {check_mtls_cert.__name__} ({str(check_mtls_cert.__doc__).strip()}),\n"
                     f"{err} ({res} {err4log})"
                     f"\n\t\tkit_id={kit_id}, cert_sha1={cert_sha1}")
        raise HTTPException(detail=err, status_code=stat)
    else:
        logger.debug(f"\n\t<~\tcheck_mtls_cert for API {api_path}, kit_id={kit_id}, sha1={cert_sha1}, ok, ended")


def authentication(kit_id, cert_sha1) -> tuple[int, str]:
    """Проверка соответствия kit_id и сертификата устройства"""
    with database.get_connection() as dbo:
        res = database.objects.certificate.sp_imdm_authentication(
            dbo, kit_id, cert_sha1, check_rc_handler=database.check_rc_handler_any_data
        )
        if res.out.rc == 0:
            dbo.commit()
    return res.out.rc, res.out.err
