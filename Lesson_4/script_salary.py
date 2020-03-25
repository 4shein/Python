from sys import argv

dummy, user_rate, user_working, user_bonus = argv

print('Rate: ', user_rate)
print('Working hours: ', user_working)
print('Bonus: ', user_bonus)
user_working = int(user_working)
user_rate = int(user_rate)
user_bonus = int(user_bonus)
user_salary = user_rate * user_working + user_bonus
print('Salary :', user_salary)