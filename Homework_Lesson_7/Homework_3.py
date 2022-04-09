import os
import shutil

#новая директория
new_dir = 'home3'
#проверка
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

#папка из которой вытаскиваем
base_falder = 'my_project'
roads = []

#вытаскиваем из папки корневую, остальные папки и файлы
for root, directory, file in os.walk(base_falder):
    #перебираем файлы
    for f in file:
        #если файл с расширением или оканчивается
        if '.html' in f:
            roads.append(os.path.join(root, f))

#из списка путей
for road in roads:
    #формируем новый путь из своей новой директории + имя директории в которой файл с расширением
    new_road = os.path.join(new_dir, os.path.dirname(road))
    #если нового путя еще нету
    if not os.path.exists(new_road):
        os.mkdir(new_road)
    #сохраненный путь из новой деректории и крайнего файла из списка путей
    save_road = os.path.join(new_road, os.path.basename(road))
    #копируем из путей в новый путь к новой директории
    shutil.copy(road, save_road)