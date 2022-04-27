class Road:
    def __init__(self, leng, width):
        self.leng = leng
        self.width = width
    def calcul_mass(self):
        massa = self.leng * self.width * 25 * 5 / 1000
        return massa
road = Road(10, 10)
print(road.calcul_mass())




