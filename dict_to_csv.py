"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    big_data = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 28, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Миша', 'age': 35, 'job': 'Driver'}, 
    ]
    with open('export.csv', 'w', encoding='utf-8', newline='') as outfile:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(outfile, fields, delimiter=';')
        for user in big_data:
            writer.writerow(user)

if __name__ == '__main__':
    main()