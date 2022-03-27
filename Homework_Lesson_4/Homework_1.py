import requests
from datetime import datetime

def curent(CURRENT, result):
    if CURRENT == result[1656:1659]:
        print(f"1 {result[1656:1659]} = {result[1720:1725]} РУБ")
    elif CURRENT == result[1796:1799]:
        print(f"1 {result[1796:1799]} = {result[1854:1860]} РУБ")
    elif CURRENT == result[457:460]:
        print(f"1 {result[457:460]} = {result[551:557]} РУБ")
    else:
        print('Ошибка, такой валюты нет в нашей базе')


def currency_rates(CURRENT=None):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    result = requests.get(url)
    result = result.text
    if CURRENT.islower():
        CURRENT = CURRENT.upper()
        curent(CURRENT, result)
        data = datetime.now()
        print(data)
    else:
        curent(CURRENT, result)
        data = datetime.now()
        print(data)








