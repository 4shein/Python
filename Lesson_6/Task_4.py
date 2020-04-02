"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random
class Car():
    speed: float = None
    color: str = None
    name: str = None
    is_police: bool = None

    def go(self):
        print('The car is going')

    def stop(self):
        print('The car is standing')

    def turn(self):
        print(random.choice([
            'The car is turned North',
            'The car is turned South',
            'The car is turned East',
            'The car is terned West',
        ]))

    def showspeed(self, speed):
        print(f'Car is driving with speed {speed}')

class TownCar(Car):
    def showspeed(self, speed):
        if speed > 60:
            print(f'Alarm! Overspeed Vehicle - {speed}')
    print(Car.name)
    print(Car.color)
    Car.is_police = False
    print(Car.is_police)

class WorkCar(Car):
    def showspeed(self, speed):
        if speed > 40:
            print(f'Alarm! Overspeed Vehicle - {speed}')
    print(Car.name)
    print(Car.color)
    Car.is_police = False
    print(Car.is_police)

class SportCar(Car):
    print(Car.name)
    print(Car.color)
    Car.is_police = False
    print(Car.is_police)


class PoliceCar(Car):
    print(Car.name)
    print(Car.color)
    Car.is_police = True
    print(Car.is_police)

a = Car()
print(1)