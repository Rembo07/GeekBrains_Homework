
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} is going!')
    def stop(self):
        print(f'{self.name} is stopped')
    def turn(self, direction):
        print(f'{self.name} turn in {direction}')

    def show_spped(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):
    """Is town mashine"""
    def show_speed(self):
        super().show_spped()
        if self.speed > 60:
            print('Warning! Exceeding speed!')


class SportCar(Car):
    """Sport mashine"""
    pass


class WorkCar(Car):
    """Work mashine"""
    def show_speed(self):
        super().show_spped()
        if self.speed > 40:
            print('Warning! Exceeding speed!')

class PoliceCar(Car):
    """Police mashine"""
    pass