"""
 Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу:
 (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт
 с параметрами.
"""
from sys import argv

dummy, user_rate, user_working, user_bonus = argv

# без dummy не работает, не знаю почему

print('Rate: ', user_rate)
print('Working hours: ', user_working)
print('Bonus: ', user_bonus)
user_working = int(user_working)
user_rate = int(user_rate)
user_bonus = int(user_bonus)
user_salary = user_rate * user_working + user_bonus
print('Salary :', user_salary)