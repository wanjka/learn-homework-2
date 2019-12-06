"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    yesterday = dt_now - timedelta(days=1)
    print('Вчера: {}'.format(yesterday.strftime('%d.%m.%Y')))
    print('Сегодня: {}'.format(dt_now.strftime('%d.%m.%Y')))

    month_ago = dt_now - relativedelta(months=1)
    print('Месяц назад: {}'.format(month_ago.strftime('%d.%m.%Y')))


def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == '__main__':
    print_days()
    print(str_2_datetime('01/01/17 12:10:03.234567'))
