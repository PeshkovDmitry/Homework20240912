"""
Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить
дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать,
сколько раз повторить строку в выводе.
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Парсер аргументов командной строки")
    parser.add_argument('number', metavar='N', type=float, nargs=1, help='Число из командной строки')
    parser.add_argument('string', metavar='S', type=str, nargs=1, help='Строка из командной строки')
    parser.add_argument('--verbose', default=False, action="store_true",
                        help="При установке этого флага выводится дополнительная информация о процессе")
    parser.add_argument('--repeat', default=1, type=int, help="Количество повторов указанной строки в выводе")
    args = parser.parse_args()
    if args.verbose:
        print("Какая-то важная информация о процессе...")
    for _ in range(args.repeat):
        print(f"В командной строке передано число {args.number[0]} и строка {args.string[0]}")
