import sys
from Homework_5 import add_write_file, open_parsing_file

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать существуюшую команду или воспользоваться функцией - help')
else:
    if command == 'write':
        try:
            name = sys.argv[2]
        except:
            print('Нехватает имени  папки')
        else:
            add_write_file(name)
    elif command == 'open':
        try:
            name = sys.argv[2]
        except:
            print('Нехватает имени папки')
        else:
            open_parsing_file(name)
    elif command == 'help':
        print('Возможные комманды:  write + file name\nopen + file name')
