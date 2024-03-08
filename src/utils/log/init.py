# -*- coding: utf-8 -*-
import logging
import sys
import platform

from utils.log.req_id import ctx_req_id
from utils.consts import logging_levels

logger = logging.getLogger("log_logger")


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, coloring only the first letter of each log message."""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[31m'
    reset = '\x1b[0m'

    def __init__(self, fmt, datefmt):
        super().__init__(fmt, datefmt)

    def format(self, record):
        """Форматирует строку логирования"""
        formatted_record = super().format(record)  # стандартный формат
        colored_record = self._colorize_first_letter(formatted_record, record.levelno)  # красит первую букву

        return colored_record

    def _colorize_first_letter(self, formatted_record, level):
        """Красит в цвет первую букву строки логирования"""
        color_mapping = {
            logging.DEBUG: self.grey,
            logging.INFO: self.grey,
            logging.WARNING: self.blue,
            logging.ERROR: self.red,
            logging.CRITICAL: self.red
        }
        color_code = color_mapping.get(level, '')
        pos = 20 if 0 < self._fmt.find('asctime') < 5 else 0    # включено или отключено логирование времени
        colored_first_letter = color_code + formatted_record[pos] + self.reset
        colored_record = formatted_record[:pos] + colored_first_letter + formatted_record[pos+1:]
        return colored_record


class InjectingReqID(logging.Filter):
    """Фильтр, добавляющий номер запроса из переменной контекста в строки логов"""
    def filter(self, record) -> bool:
        """record - объект строки логирования"""
        try:
            record.req_id = ctx_req_id.get()  # этот номер сгенерирован во время асинхронного старта обработки запроса
        except LookupError:
            record.req_id = "000000-000"
        return True


def setup_log(logging_level: int, timing_level: int, log_format: str) -> None:
    """Установка общих параметров логирования"""

    # Установка потокового обработчика handler для стандартного вывода stderr
    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(CustomFormatter(log_format, "%Y-%m-%d %H:%M:%S"))

    # Добавление фильтра, который ничего не фильтрует, но актуализирует req_id из контекста
    add_req_id = InjectingReqID()
    stdout_handler.addFilter(add_req_id)

    # ВАЖНО! если это вдруг не первая установка конфигурации логирования, то нужно передать keyword force=True
    logging.basicConfig(level=logging_level, handlers=[stdout_handler], force=True)


def set_logger_levels(exclusions):
    """
    Устанавливает исключения из общего логирования, полученные для некоторых логеров из iosmdm.yml из секции loggers
    exclusions - список словарей вида [{'name': [<имена логеров>], 'level': <новый уровень логирования>}]
    """
    if exclusions:                                      # исключения из конфига
        count_exclusions = 0
        for exclusion in exclusions:
            loggers_cfg: str = exclusion.get("name")    # строка из конфига - список имён логеров из словаря исключений
            if "," in loggers_cfg:                      # строку со списком преобразуем в настоящий список Питона
                loggers = loggers_cfg.split(",")        # разделитель запятая
            elif " " in loggers_cfg:                    # или пробел
                loggers = loggers_cfg.split(" ")
            else:
                loggers = [loggers_cfg]                 # или список был из одного элемента

            loggers = list(set([_l.strip() for _l in loggers if _l]))   # убираем окружающие пробелы и дубликаты
            logger_level = str(exclusion.get("level")).upper()     # берём уровень логирования из текущего исключения
            logger_to_file: bool = bool(exclusion.get("to_file"))  # выясняем, надо ли писать логеру в отдельный файл

            for loger in loggers:                      # идём по списку логеров
                if loger and logger_level:             # если в исключении был уровень логирования
                    lggr = logging.getLogger(loger)    # то берём (при необходимости создаём) логер
                    lggr.level = logging_levels.get(logger_level, 10)  # и УСТАНАВЛИВАЕМ ему УРОВЕНЬ из исключения
                    count_exclusions += 1
                    if logger_to_file:                  # если надо, этот логер будет писать в файл
                        handler = logging.StreamHandler(sys.stderr)
                        lggr.addHandler(handler)
        if count_exclusions:
            logger.info(f"Logging level exceptions set for {count_exclusions} loggers.")


def log_loggers():
    """Логирование логеров, перечисление их количества"""
    log_logger_var = logging.getLogger("log_logger")
    # получим список всех логеров в системе
    ar = sorted(list(set([logger_name for logger_name in logging.Logger.manager.loggerDict.keys()])))
    log_logger_var.info(f"{len(ar)} RegPortal-server loggers created")


def log_file_system():
    """Логирование файловой системы"""
    log_cache = logging.getLogger("log_cache")
    os_platform = platform.system()
    if os_platform == "Windows":
        log_cache.debug(f"OS {os_platform}, fcntl_win used (files descriptor control system)")
    else:
        log_cache.debug(f"OS {os_platform}, fcntl used (files descriptor control system)")
