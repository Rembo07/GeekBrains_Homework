def name_hobby():
    with open('users.csv', 'w', encoding= 'utf-8') as f:
        f.write('Иванов,Иван,Иванович\nПетров,Петр,Петрович')

    with open('hobby.csv', 'w', encoding='utf-8') as f:
        f.write('скалолазание,охота\nгорные лыжи')
    name_list = []
    hobby_list = []
    result = {}
    with open('users.csv', 'r', encoding='utf-8') as names:
        for fio in names:
            name = str(fio).replace(',', ' ').strip() #
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




