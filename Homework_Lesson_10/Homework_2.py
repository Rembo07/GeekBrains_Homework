from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parm):
        self.parm = parm
    @abstractmethod
    def calcult(self):
        pass

class Coat(Clothes):
    @property
    def calcult(self):
        return round((self.parm / 6.5) + 0.5)

class Suit(Clothes):
    @property
    def calcult(self):
        return round((2 * self.parm) + 0.3)

clothes = Clothes
coat = Coat(55)
suit = Suit(55)
print(suit.calcult)