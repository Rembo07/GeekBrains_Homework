price = [44.1, 21.4, 14.6, 23.18, 18.86, 78.0, 67.24, 87.91, 12.9, 80.76, 18.21, 56.9, 46.3, 89.1, 21.7]
new_price = []
for i in price:
    start_cent = i * 100
    ruble = int(start_cent // 100)
    cent = int(start_cent % 100)
    if cent % 10 == 0:
        cent = cent // 10
    cent = str(cent)
    cent = cent.zfill(2)
    result = f'{ruble} руб  {cent} коп'
    new_price.append(result)
print(new_price)
print(id(new_price))


new_price.sort()
print(new_price)
print(id(new_price))


new_price.reverse()
print(new_price[:5])