


#Тут выводится ошибка KeyError 1000 line 20 сидел разбирался в чем проблема, менял переменные так и непонял((((


import os
import json
roads = []

for root, directiry, file in os.walk('../'):
    for f in file:
        path_road = os.path.join(root, f)
        roads.append((path_road.split('.')[-1], os.stat(path_road).st_size))

max_size = max(roads, key=lambda x: x[1])[1]

i = 1
result_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    result_dict[i] = (0, [])

for file in roads:
    print(len(str(file)))
    nums, result = result_dict[10 ** len(str(file[1]))]
    result.append(file[0])
    result = list(set(result))
    result_dict[10 ** len(str(file[1]))] += (nums + 1, result)
print(result_dict)

with open(os.path.basename(os.getcwd()) + 'sum.jason', 'w') as f:
    json.dump(result_dict, f)