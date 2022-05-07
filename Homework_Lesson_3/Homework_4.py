def thesaurus_adv(*name_surname):
    result_dict = {}
    for ns in name_surname:
        name_list = list(ns)
        surname_first = ' '.join(ns.split(' ')[::-1])
        surname_list = list(surname_first)
        result_dict.setdefault(surname_list[0], {}).setdefault(name_list[0], []).append(ns)
    print(result_dict)




thesaurus_adv('Artem Bobrov', 'Vladimir Burcev', 'Gomorov Roman', )



