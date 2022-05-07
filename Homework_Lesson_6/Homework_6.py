
def add_info(text):
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
     f.write(f'{text}\n')


def wach_info(froms):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        str_list = []
        for i in f:
            str_list.append(i.strip())
        gen_1 = (i for i in str_list[int(froms) - 1:])
        for i in gen_1:
            print(i)


def limited_reading(num_str_from, num_str_to):

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        str_list = []
        for i in f:
            str_list.append(i.strip())
        gen_1 = (i for i in str_list[int(num_str_from) - 1:int(num_str_to)])
        for i in gen_1:
            print(i)








