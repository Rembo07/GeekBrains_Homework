seconds = int(input('Введите количество секунд: '))

minutes = seconds // 60
remainder_minutes = seconds % 60


hours = minutes // 60
remainder_hours = minutes % 60


day = hours // 24
remainder_day = hours % 24


print('{} дн   {} час {} мин {} сек'.format(day, remainder_day, remainder_hours, remainder_minutes))
