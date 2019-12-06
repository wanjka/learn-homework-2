"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
def word_cnt(text):
    delimiters = '.,!?()'
    for i in range(len(delimiters)):
        if text[i] in delimiters:
            text[i] = ' '
    return len(text.split()) - 1

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    content = ''
    with open('referat.txt', 'r', encoding='utf-8') as infile:
        content = infile.read()
    print('Длина строки:', len(content))
    print('Слов в файле:', word_cnt(content))
    content = content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(content)

if __name__ == '__main__':
    main()