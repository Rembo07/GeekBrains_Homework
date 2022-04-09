import yaml
import os

file_yaml = {'my_project' : [{'settings' : ['__init__.py', 'dev.py', 'prod.py']},
            [{'mainapp' : ['__init.py__', 'models.py', 'vievs.py',
            {'templates' : [
            {'mainapp' : ['base.html', 'index.html']}]}]}],
            {'autapp' : ['__init.py__', 'models.py', 'vievs.py',
            {'templates' : [
            {'autapp' : ['base.html', 'index.html']}]}]}]}

#просто создаем файл с расширением
with open('config.yaml', 'w') as f:
    f.write(yaml.dump(file_yaml))

#открываем его и выкачиваем от туда инфу
with open('config.yaml') as f:
    loaders = yaml.safe_load(f)

def creators(name):
    for folders, files in name.items():
        #проверяем
        if not os.path.exists(folders):
            os.mkdir(folders)
        os.chdir(folders)
        for file in files:
            #проверка если файл словарь
            if isinstance(file, dict):
                creators(file)
            else:
                #проверка
                if not os.path.exists(file):
                    #если в файл с расширением зацепились за точку тут
                    if '.' in file:
                        #создаем посредством открытия и записи пробела
                        with open(file, 'w') as f:
                            f.write('')
    else:
        #иначе перемещаемся на директорию выше
        os.chdir('../')
