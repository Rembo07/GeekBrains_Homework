def add_write_file(name_file):
    if name_file == 'users.csv':
        with open('users.csv', 'w', encoding= 'utf-8') as f:
            f.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович')
    elif name_file == 'hobby.csv':
        with open('hobby.csv', 'w', encoding='utf-8') as f:
            f.write('скалолазание,охота\nгорные лыжи')

def open_parsing_file(command_or_open):
    name_list = []
    hobby_list = []
    result = {}
    if command_or_open == 'users.csv':
        with open('users.csv', 'r', encoding='utf-8') as names:
            for fio in names:
                name = str(fio).replace(',', ' ').strip()  #
                name_list.append(name)
        print(name_list)
    elif command_or_open == 'hobby.csv':
        with open('hobby.csv', 'r', encoding='utf-8') as hobbys:
            for hobby in hobbys:
                hoby = str(hobby).strip()
                hobby_list.append(hoby)
        print(hobby_list)
    elif command_or_open == 'all':
        with open('users.csv', 'r', encoding='utf-8') as names:
            for fio in names:
                name = str(fio).replace(',', ' ').strip()  #
                name_list.append(name)

        with open('hobby.csv', 'r', encoding='utf-8') as hobbys:
            for hobby in hobbys:
                hoby = str(hobby).strip()
                hobby_list.append(hoby)

        for names_hobbys in zip(name_list, hobby_list):
            result.setdefault(names_hobbys[0], []).append(names_hobbys[1])
        if len(name_list) > len(hobby_list):
            result.setdefault(None)
        else:
            print('Code <1>')
        print(result)
