"""
Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
"""

from datetime import datetime, timedelta

if __name__ == "__main__":
    num_of_days = int(input("Введите количество дней: "))
    dt = timedelta(days=num_of_days)
    t = datetime.now()
    t += dt
    print(t.strftime('%Y-%m-%d'))
