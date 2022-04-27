class Worker:
    def __init__(self,name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']



class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus

pos = Position('Ivan', 'Kirov', 'director', {"wage": 50000, "bonus": 34000})
print(pos.get_full_name())



