
def thesaurus(*arg):
    name = {}
    for i in arg:

        name_list = list(i)
        if name_list[0] == "И":
            name.setdefault(name_list[0], []).append(i)
        elif name_list[0] == "М":
            name.setdefault(name_list[0], []).append(i)
        elif name_list[0] == "П":
            name.setdefault(name_list[0], []).append(i)
        else:
            print('Extented')
        sorted(name)
    print(name)


thesaurus("Иван", "Мария", "Петр", "Илья" )