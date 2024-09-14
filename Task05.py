"""
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога,
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import argparse
import os
from collections import namedtuple
import logging


logging.basicConfig(level=logging.NOTSET, filename='dirinfo.txt', encoding='utf-8')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser("Получение данных о заданном каталоге")
parser.add_argument('string', metavar='S', type=str, nargs=1, default="", help='Путь к каталогу')
args = parser.parse_args()
directory = args.string[0]

if not os.path.isdir(directory):
    raise ValueError("Указанный путь не является директорией")

Info = namedtuple("Info", "path extension is_directory parent")
for home_dir, cur_dir, cur_file in os.walk(directory):
    for d in cur_dir:
        info = Info(path=d, extension="", is_directory=True, parent=home_dir)
        logger.info(info)
    for f in cur_file:
        file_data = os.path.splitext(f)
        if len(file_data) == 2:
            info = Info(path=file_data[0], extension=file_data[1], is_directory=False, parent=home_dir)
        else:
            info = Info(path=f, extension="", is_directory=False, parent=home_dir)
        logger.info(info)


