# -*- coding: utf-8 -*-
import logging
import ssl
from typing import Tuple

from asyncpg import Pool, Connection, Record, create_pool, connect

from database.exceptions import DatabaseException
from database.procedures import ProcedureList
from utils.base_config.base_config import DatabaseConfig

logger = logging.getLogger(__name__)


class TRecord(Record):
    """Делает объект Record TupleLike"""

    def __getattr__(self, item):
        """
        Метод получения атрибута
        Намеренно не используется .get(),
        так как при попытке получить несуществующее поле
        должна вылетать ошибка а не отдаваться None
        """
        return self[item]


class Database(ProcedureList):
    """Реализует объект драйвера базы данных"""

    def __init__(self):
        self.cfg: DatabaseConfig | None = None
        self.pool: Pool | None = None
        super().__init__()

    def _log_connection(self):
        """Логирование параметров соединения"""
        _ll = (
            f'Database connection. Trying to make connection pool with:'
            f'\n\t{"database":<20}= {self.cfg.type}'
            f"\n\t{'host':<20}= {self.cfg.host}"
            f"\n\t{'port':<20}= {self.cfg.port}"
            f"\n\t{'dbname':<20}= {self.cfg.name}"
            f"\n\t{'user':<20}= {self.cfg.user}"
            f"\n\t{'app_name':<20}= {self.cfg.app_name}"
            f"\n\t{'SSL_mode':<20}= {self.cfg.sslmode}"
        )

        if self.cfg.sslmode in {'allow', 'prefer', 'require', 'verify-ca', 'verify-full'}:
            _ll += (
                f"\n\tSSL-cert \t= {self.cfg.sslcert}"
                f"\n\tSSL-key \t= {self.cfg.sslkey}"
                f"\n\tSSL-ca \t\t= {self.cfg.sslcert}"
            )

        logger.fatal(_ll)

    def _make_connection_context(self) -> Tuple[str, ssl.SSLContext]:
        """Создаёт объекты строки подключения и ssl контекста для реализации mTLS с БД"""
        if not self.cfg:
            raise DatabaseException("Database config is empty. Perform `db.set_config(config.db)` before connecting")

        cfg = self.cfg
        if cfg.sslmode in {'require', 'verify-ca', 'verify-full'}:
            sslctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cfg.sslrootcert)
            if cfg.sslcert and cfg.sslkey:
                sslctx.load_cert_chain(certfile=cfg.sslcert, keyfile=cfg.sslkey)
        else:
            sslctx = None

        dsn = '{type}://{user}:{password}@{host}:{port}/{database}?application_name={app_name}'.format(
            type=cfg.type,
            user=cfg.user,
            password=cfg.password,
            host=cfg.host,
            port=cfg.port,
            database=cfg.name,
            app_name=cfg.app_name,
        )

        return dsn, sslctx

    def set_config(self, db_config: DatabaseConfig):
        """Установка объекта конфигурации"""
        self.cfg: DatabaseConfig = db_config

    async def make_connection_pool(self):
        """Инициализация пула соединений с БД"""
        dsn, sslctx = self._make_connection_context()
        self._log_connection()

        try:
            self.pool = await create_pool(
                dsn=dsn, min_size=self.cfg.minconn, max_size=self.cfg.maxconn,
                command_timeout=60, max_inactive_connection_lifetime=1,
                ssl=sslctx or False, record_class=TRecord
            )
        except ssl.SSLCertVerificationError as e:
            logger.error(e)

        except TimeoutError:
            raise DatabaseException('Timeout error while connecting to database')

        logger.debug('Pool created')

    async def connection_pool_dependency(self) -> Connection:
        """Зависимость для FastAPI, забирающая соединение из пула и возвращающая его через yield
        Таким образом после завершения работы с соединением оно автоматически вернётся в пул
        Подробнее: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield
        :return: объект соединения
        """
        try:
            async with self.get_connection_from_pool() as connection:
                yield connection
        except AttributeError:  # не установлено соединение с БД
            raise DatabaseException("Database connection is not established")

    def get_connection_from_pool(self) -> Connection:
        """Забирает соединение из пула
        Требует использования контекстного менеджера
        :return: объект соединения
        """
        try:
            return self.pool.acquire()
        except AttributeError:  # не установлено соединение с БД
            raise DatabaseException("Database connection is not established")

    async def get_connection(self) -> Connection:
        """Подключается к БД и возвращает объект подключения
        !!! Данный метод не использует пул подключений и используется для parser чтобы однократно забрать что-то из БД
        :return: объект подключения к БД
        """
        dsn, sslctx = self._make_connection_context()
        connection: Connection = await connect(dsn=dsn, ssl=sslctx)
        return connection
