import sys
from Homework_6 import*


command = sys.argv[1]


if command == 'add':
    try:
        text = sys.argv[2]
    except:
        print('Напишите что вы хотите добавить')
    else:
        add_info(text)
elif command == 'wach_all':
    try:
        froms = sys.argv[2]
    except:
        print('Напишите с какой строки вы хотите начать просмотр')
    else:
        wach_info(froms)
elif command == 'limit_read':

    try:
        froms = sys.argv[2]
        tos = sys.argv[3]

    except:
        print('Напишите с какой строки и по какую строки хотите читать')
    else:
        limited_reading(froms, tos)
else:
    print('add + - добавить + содержимое в файл\nwach_all + - смотреми файл полностью + с какой строки\nlimit_read + +- смотреть файл по строкам + от и + до')

