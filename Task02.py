"""
Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году.
"""

from datetime import datetime
import locale


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
    current_time = datetime.now()
    print(current_time.strftime('%Y-%m-%d %H:%M:%S, %A, неделя %W'))