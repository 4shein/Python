"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.name = name,
        self.surname = surname,
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

class Position(Worker):


    def __init__(self, position_name, name, surname, wage: float, bonus: float):
        self.position_name = position_name
        super().__init__(name, surname, wage, bonus)


if __name__ == '__main__':
    tmp = Position('Менеджер', 'Анатолий', 'Дукалис', 12000, 2000)

print(1)