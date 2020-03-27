"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
import time

class Trafficlight:
    _color = ()

    def running(self):
        print('Trafficlight is working')
        while True:
            trafficlight_color = 'red'
            print(trafficlight_color)
            time.sleep(7)
            trafficlight_color = 'yellow'
            print(trafficlight_color)
            time.sleep(2)
            trafficlight_color = 'green'
            print(trafficlight_color)
            time.sleep(5)
            trafficlight_color = 'blank'
            print(trafficlight_color)
            time.sleep(1)
            trafficlight_color = 'green'
            print(trafficlight_color)
            time.sleep(1)
            trafficlight_color = 'blank'
            print(trafficlight_color)
            time.sleep(1)
            trafficlight_color = 'green'
            print(trafficlight_color)
            time.sleep(1)
            trafficlight_color = 'blank'
            print(trafficlight_color)
            time.sleep(1)


a = Trafficlight()
a.running()