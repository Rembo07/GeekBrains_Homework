def get_sign(x):
    if x[0] in '+-':
        return x[0]


my_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_text)
i = 0
while i < len(my_text):
    sign = get_sign(my_text[i])
    if my_text[i].isdigit() or (sign and my_text[i][1:].isdigit()):
        if sign:
            my_text[i] = sign + my_text[i][1:].zfill(2)
        else:
            my_text[i] = my_text[i].zfill(2)

        my_text.insert(i, '"')
        my_text.insert(i + 2, '"')
        i += 1
    i += 1

print(my_text)





