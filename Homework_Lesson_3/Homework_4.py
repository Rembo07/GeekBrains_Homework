

def thesaurus_adv(*NameSurname):
    name = {}
    for ns in NameSurname:
        nsx = list(ns)
        name_rev = ' '.join(ns.split(' ')[::-1])
        idx = list(name_rev)

        if idx[0] == 'С':
            if nsx[0] == 'И':
                name.setdefault(idx[0], {}).setdefault(nsx[0], []).append(ns)
            elif nsx[0] == 'А':
                name.setdefault(idx[0], {}).setdefault(nsx[0], []).append(ns)
            else:
                print('Excepted')
        elif idx[0] == 'А':
            if  nsx[0] == 'П':
                name.setdefault(idx[0], {}).setdefault(nsx[0], []).append(ns)
            else:
                print('Excepted')
        elif idx[0] == 'И':
            if nsx[0] == 'И':
                name.setdefault(idx[0], {}).setdefault(nsx[0], []).append(ns)
            else:
                print('Excepted')
        else:
            print('Excepted')
    print(name)
    sorted_dict = {x: name[x] for x in sorted(name)}
    print(sorted_dict)



thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")