"""
Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы.
Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
WARNING и выше — в warnings_errors.log.
"""
import json
import logging
import logging.config


CONFIG = '''
{
    "version": 1,
    "filters": {
        "info_and_below": {
            "()" : "__main__.filter_maker",
            "level": "INFO"
        }
    }
}
'''


def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level

    return filter


logging.config.dictConfig(json.loads(CONFIG))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_info_file_handler = logging.FileHandler(filename='debug_info.log', encoding='utf-8')
debug_info_file_handler.setLevel(logging.DEBUG)
debug_info_file_handler.addFilter(logging.Filter("warnings_and_below"))

warnings_errors_file_handler = logging.FileHandler(filename='warnings_errors.log', encoding='utf-8')
warnings_errors_file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debug_info_file_handler.setFormatter(formatter)
warnings_errors_file_handler.setFormatter(formatter)

logger.addHandler(debug_info_file_handler)
logger.addHandler(warnings_errors_file_handler)


if __name__ == "__main__":
    logger.info("This is info")
    logger.debug("This is debug")
    logger.warning("This is warning")
    logger.error("This is error")
    logger.critical("This is critical")