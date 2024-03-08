#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from fastapi import Request

from database import db
from app.exceptions import MtlsException

logger = logging.getLogger(__name__)


class CheckMtlsSert:
    """ Зависимость проверки сертификата mtls"""
    """ Использовать в массиве dependencies: dependencies=[Depends(CheckMtlsSert(kit_id=kit_id), )]
    """
    def __init__(self, kit_id: int | None = None):
        """Передача параметров в зависимость (или в метод)
        :param kit_id: номер комплекта
        """
        self.kit_id = kit_id

    async def __call__(self, request: Request) -> None:
        """Проверка отпечатка сертификата mTLS в X-Client-Certificate-Sha1"""

        # если kit_id не указан, то считаем это вызовом для Андроида
        self.kit_id = int(request.headers.get("X-MCC-ID")) if self.kit_id is None else self.kit_id

        cert_sha1 = request.headers.get('X-Client-Certificate-Sha1', '')  # отпечаток сертификата
        api_path = request.url.path  # путь вызова API
        logger.debug(f"\n\t~>\tcheck_mtls_cert ({CheckMtlsSert.__doc__}) for {api_path} kit_id={self.kit_id} started"
                     f"\n\t\tX-Client-Certificate-Sha1='{cert_sha1}'")
        stat, err, err4log = None, None, None  # чтобы функция не упала от логирования

        if str(cert_sha1).strip() == '':
            # если заголовка нет или в нём пусто, то это или legacy-комплект, или ошибка Монитора, или ошибка nginx-а
            logger.info(f"HTTP header 'X-Client-Certificate-Sha1' not found or empty"
                        f" - This is either a legacy kit={self.kit_id}, or a Monitor error, or an nginx error")

        async with db.get_connection_from_pool() as conn:
            out, = await db.sp_certificate_imdm_authentication(conn, self.kit_id, cert_sha1)

            if out.o_rc != 0:
                stat, err = 401, "Authentication error"
                if out.o_rc == -20012:
                    err4log = f"Certificate does not match this kit ({out.o_err})"
                elif out.o_rc == -20001:
                    err4log = f"Certificate not found ({out.o_err})"
                elif out.o_rc == -20013:
                    err4log = f"Certificate has expired or the expiration has not started ({out.o_err})"
                elif out.o_rc == -20011:
                    err4log = f"This kit isn't legacy, must have certificate ({out.o_err})"
                else:
                    err4log = f"Unexpected db error ({out.o_err})"

        if stat is not None:
            logger.error(f"\n\t<~\tcheck_mtls_cert, error for API {api_path}, HTTP={stat}, ended"
                         f"\n\t\tfor {CheckMtlsSert.__name__} ({str(CheckMtlsSert.__doc__).strip()}), "
                         f"kit_id={self.kit_id}, cert_sha1={cert_sha1}"
                         f"\n\t\t{err} ({out.o_rc} {err4log})")
            raise MtlsException(err=err, stat=stat)
        else:
            logger.debug(f"\n\t<~\tcheck_mtls_cert for API {api_path}, kit_id={self.kit_id}, sha1={cert_sha1} ended ok")
