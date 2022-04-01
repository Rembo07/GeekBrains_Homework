def thesaurus(*names):
    name = {}
    for i in names:
        name_list = list(i)
        name.setdefault(name_list[0], []).append(i)
    return name

print(thesaurus('Patrick', 'Amanda', 'Panda', 'Artur'))