class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return "{0} {1}".format(self.name, self.surname)

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


emp = Position('Вася', 'Пупкин', 'грузчик', 12500, 3000)
# print(emp.name)
# print(emp.surname)
# print(emp._income)
print(emp.get_full_name())
print(emp.get_total_income())