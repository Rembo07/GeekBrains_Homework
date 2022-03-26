def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10             #ф-ция для перебора последовательности и ее суммирования по средством отброса сначала десятков потом единиц
        value //= 10

    return res


arr = [i**3 for i in range(1, 1001, 2)]    #сам цикл

res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr)) #если не делится на7
res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr)) #если делится на 7

print(res1)
print(res2)
print(sum_digits(25))