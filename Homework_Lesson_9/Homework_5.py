class Stationery:
    def __init__(self, title):
        self.title = title
        print(f'Name class {self.title}')
    def draw(self):
        print('Отрисовка')
class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Карандаш')
class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Ручка')
class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Маркер')