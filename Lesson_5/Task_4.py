"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""

with open('data_task4.txt', 'r') as file:
    data = []

    for line in file:
        key, value = line.split(' - ')

        if key == 'One':
            key = 'Один'
        elif key == 'Two':
            key = 'Два'
        elif key == 'Three':
            key = 'Три'
        elif key == 'Four':
            key = 'Четыре'
        else:
            key = 'Новое число'

        data = (key + ' - ' + value)

        with open('data_task4_2.txt', 'a') as new_data:
            print(data, file=new_data, end='')





