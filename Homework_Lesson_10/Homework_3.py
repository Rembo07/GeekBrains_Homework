class Cell:
    def __init__(self, num):
        self.num = num
    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.num // rows)]) \
                         + '\n' + '*' * (self.num % rows)
    def __str__(self):
        return str(self.num)
    def __add__(self, other):

        return 'summ of cell...' + str(self.num + other.num)
    def __sub__(self, other):
        return self.num - other if self.num - other.num> 0 else 'In firs cell less than in the second cell'
    def __mul__(self, other):
        return 'Myltiply of cells is' + str(self.num * other.num)
    def __truediv__(self, other):
        return 'Truediv of cells' + str(round(self.num / other.num))
#cell_1 = Cell(25)
#cell_2 = Cell(11)
#print()