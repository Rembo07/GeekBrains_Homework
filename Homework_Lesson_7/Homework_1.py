import os

contents = {'my_project' : ['settings', 'mainapp', 'adminapp', 'autapp']}

for rooted, folders in contents.items():
    if os.path.exists(rooted):
        print(f'{rooted}, данная папка уже существует')
    else:
        for folder in folders:
            road = os.path.join(rooted, folder)
            os.makedirs(road)
