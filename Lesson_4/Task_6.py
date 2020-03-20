"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import cycle, count
start_number = input('Input first number\n')
start_number = int(start_number)
last_number = input('Input last number\n')
last_number = int(last_number)
step = input('Input step\n')
step = int(step)
val = []
for el in count(start_number, step):
    if el > last_number:
        break
    else:
        val.append(el)

print(val)

val_copy = [el for el in val]

print(val_copy)

# не понял, для чего нужно использовать cycle()