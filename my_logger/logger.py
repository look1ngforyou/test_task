import logging
from logging import StreamHandler, Formatter
from my_logger.logger_configuration import LoggerConfig
import sys


class Logger:
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGGER_LEVEL)
    __handler = StreamHandler(stream=sys.stdout)
    __handler.setFormatter(Formatter(fmt=LoggerConfig.FORMAT))
    __logger.addHandler(__handler)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(msg=message)
