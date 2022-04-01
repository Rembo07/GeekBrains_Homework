src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for num in range(len(src) - 1):
    first = src[num]
    num += 1
    second = src[num]
    if second > first:
        result.append(second)

print(result)

