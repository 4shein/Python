"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    name: str = None
    surname: str = None
    position: str = None
    _income = {'wage': None,
                    'bonus': None,
                    }

    def __init__(self, name, surname, salary, bonus):
        self.name = name,
        self.surname = surname,
        self._income[wage] = wage
        self._income[bonus] = bonus

# не знаю, как обраатиться к словарю

class Position(Worker):

    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        return name + surname


    def get_total_income(self, wage, bonus):
        self._income = wage
        self._income = bonus
        return sum(self._income.values())


if __name__ == '__main__':
    tmp = Worker('Менеджер', 'Анатолий', 'Дукалис', 12000, 1000)
