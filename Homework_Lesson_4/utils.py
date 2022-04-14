from Homework_2 import currency_rates
import sys

try:
    command = sys.argv[1]
except IndexError:
    print('Введите верное название команды')
else:
    if command == 'curs':
        try:
            valute = sys.argv[2]
        except IndexError:
            print('Введите верное название валюты')
        else:
            currency_rates(valute)



