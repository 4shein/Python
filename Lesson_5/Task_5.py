"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

with open('Data_task5.txt', 'w+') as file:
    user_number = random.randint(2, 5)
    user_number = int(user_number)
    i = 0


    while i < user_number:
        i += 1
        print(random.randint(1, 9), file=file, end=' ')


number_sum = 0

with open('data_task5.txt', 'r') as file:


    for line in file:


        for number in line:

            
            if number.isdigit():
                number = int(number)
                print(number, end=' ')
                number_sum = number_sum + number


        print(f'\nNumber sum = {number_sum}')