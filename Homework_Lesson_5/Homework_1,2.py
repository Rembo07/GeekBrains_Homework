def num_generator_yield(num):
    for i in range(1, num + 1, 2):
        yield i

print(*num_generator_yield(5))


def num_generator_noyield(num):
    nums = (i for i in range(1, num + 1, 2))
    print(*nums)
num_generator_noyield(5)
