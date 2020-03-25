"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
i = 0
salary_sum = 0

with open('data_task3.txt', 'r') as file:
    workers = {}

    for line in file:
        surname, salary = line.split()
        workers[surname] = salary
        i += 1
        salary_sum = salary_sum + int(salary)

        if int(salary) < 20000:
            print(f"Salary less than 20000 rub at {surname}. He have only {salary} rub")

print(f'Average salary - {salary_sum / i}')
