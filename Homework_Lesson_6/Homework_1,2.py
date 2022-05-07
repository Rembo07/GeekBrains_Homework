from collections import Counter
from requests import get

url = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(url)

with open('nginx_logs.txt') as f:
    ip_list = []
    for line in f:
        ip = line[line.find(line[0]) : line.find('-',line.find(line[0]) )] #обрезаем только айпи
        ip_list.append(ip)
        get_k = line[line.find('"', line.find(line[0])) + 1 : line.find('/', line.find('GET'))] #обрезаем гет
        product = line[line.find('T') + 1: line.find('H', line.find('T'))] #обрезаем скачаный продукт
        result = tuple(f'{ip} {get_k} {product}'.split())
        print(result)
ip_max = str(Counter(ip_list)) #вычисляем при помощи словаря и новой библиотеки частоповторяющийся айпи и колличество его запросов
ip_spammer = ip_max[ip_max.find("'", ip_max.find('Counter')) + 1 : ip_max.find("':", ip_max.find('Counter'))] # обрезвем из словаря айпи
interaction =ip_max[ip_max.find(':', ip_max.find('Counter'))  + 2: ip_max.find("'", ip_max.find('2350')) - 2] #обрезаем из словаря кол-во запросов
informations = f'IP SPAMMER: {ip_spammer}\nNUMBER OF INTERACTIONS: {interaction}'

print(informations)

