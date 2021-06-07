class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self.position} с доходом в {self._income["wage"] + self._income["bonus"]}')


if __name__ == '__main__':
    income_dict = {'wage': 100000, 'bonus': 200000}
    man = Position('Вася', 'Пупкин', 'Чесатель пяток', income_dict)
    man.get_full_name()
    man.get_total_income()
