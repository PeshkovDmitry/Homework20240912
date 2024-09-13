"""
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.

Задание сделано через JSON конфигурацию, т.к. необходимо настраивать фильтр, чтобы
в файл debug_info.log попадали только сообщения уровня не выше INFO и DEBUG
"""

import json
import logging
import logging.config

CONFIG = '''
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(levelname)-8s - %(message)s"
        }
    },
    "filters": {
        "info_and_below": {
            "()" : "__main__.filter_maker",
            "level": "INFO"
        }
    },
    "handlers": {
        "warnings_errors_file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "warnings_errors.log",
            "encoding": "utf-8",
            "mode": "w",
            "level": "WARNING"
        },
        "debug_info_file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "debug_info.log",
            "encoding": "utf-8",
            "mode": "w",
            "level": "DEBUG",
            "filters": ["info_and_below"]
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "warnings_errors_file",
            "debug_info_file"
        ]
    }
}
'''


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


if __name__ == "__main__":
    logging.config.dictConfig(json.loads(CONFIG))
    logger = logging.getLogger(__name__)
    logger.debug('Сообщение уровня DEBUG')
    logger.info('Сообщение уровня  INFO')
    logger.warning('Сообщение уровня WARNING')
    logger.error('Сообщение уровня ERROR')
    logger.critical('Сообщение уровня CRITICAL')