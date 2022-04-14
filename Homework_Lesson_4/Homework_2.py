from requests import get

def currency_rates(value):
    value = str(value).upper()
    url = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    val = url[url.find(value, url.find('>')): url.find('<', url.find(value))]
    curr = url[url.find('Value>', url.find(val)) + 6: url.find('</Value>', url.find(val))]
    data_time = url[url.find('Date="', url.find('Date')) + 6: url.find('name', url.find('Date')) - 2]
    print( f'Валюта: {val}\nКурс по отношению к рублю: {curr}\nДата: {data_time}')

    
