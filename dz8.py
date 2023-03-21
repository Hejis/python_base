
# Напишите функцию read_last(lines, file), 
# которая будет открывать определенный файл 
# file и выводить на печать построчно последние
# строки в количестве lines (на всякий случай проверим, что задано 
#                            положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Количество строк может быть только целым положительным')
 
 
# Тесты
read_last(3, 'article.txt')
read_last(-5, 'article.txt')