"""import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "12345678")

"""
import time, random, numbers
task_number = 10
max_number = 9
error_value = 'ERROR'
operation = 'z'

number_actions = '3'
number_actions = int(number_actions)

i = 0
mistakes = 0
time_start = time.time()
action = ['+', '-', '*', '/']


while i < task_number:
    k = 0
    list_actions = []

    while k <= number_actions * 2:
        action_tmp = random.choice(action)
        list_actions.insert(k, random.randrange(2, max_number))
        k += 1
        list_actions.insert(k, action_tmp)
        k += 1

    list_actions.pop(len(list_actions)-1)
    list_actions_str = []

    for item in list_actions:
        list_actions_str.append(str(item))
    str_tmp = ' '.join(list_actions_str)
    answer = eval(str_tmp)
    print(answer)

    if answer > 0 and answer == int(answer):
        answer = int(answer)
        user_answer = input(str_tmp + ' = ')

        try:
            int(user_answer)
        except:
            print(error_value)
            mistakes += 1
            continue

        user_answer = int(user_answer)
        if user_answer == answer and (task_number - i) > 1:
            print(f'Правильно!\nОсталось решить {task_number - i - 1} прим.')
            i += 1

        elif user_answer == answer and (task_number - i) == 1:
            print('Правильно!')
            i += 1

        elif user_answer != answer and (task_number - i) >= 1:
            print(f'Ошибка! Правильный ответ = {answer}\nОсталось решить {task_number - i} прим.')
            mistakes += 1
