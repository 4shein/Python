import random, time
task_number = 10
error_value = 'Введены неверные данные!'
print("Решите правильно 10 примеров")


while True:

    while True:

        max_number = input('Введите максимальное число ')

        try:
            max_number = int(max_number)
            #break

        except:
            print(error_value)
            continue

        #while True:

        print('\nВозможные действия с числами:')
        operation = input(f'сложение (нажмите "+", затем Enter)\n'
                      'вычитание (нажмите "-", затем Enter)\n'
                      'умножение (нажмите "*", затем Enter)\n'
                      'деление (нажмите "/", затем Enter)\n'
                      'комбинированные действия (нажмите "=", затем Enter)\n'
                      '\nВыберите действие с числами '
                      )
        try:
            operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == '='

        except:
            print(error_value)
            continue

        if operation == '+':
            while True:
                number_terms = input('Введите количество слагаемых чисел ')
                try:
                    int(number_terms)
                except:
                    print(error_value)
                    continue

                if int(number_terms) <=1:
                    print(error_value)
                    continue

                break
            number_terms = int(number_terms)
            i = 0
            mistakes = 0
            time_start = time.time()
            while i < task_number:
                k = 1
                list_sum = []
                while k <= number_terms:
                    list_sum.append(random.randrange(1, max_number))
                    k += 1
                answer = sum(list_sum)
                list_sum_str = []
                for item in list_sum:
                    list_sum_str.append(str(item))
                str_sum = ' + '.join(list_sum_str)
                user_answer = input(str_sum + ' = ')

                try:
                    int(user_answer)
                except:
                    print(error_value)
                    mistakes += 1
                    continue

                user_answer = int(user_answer)
                if user_answer == answer and (task_number - i) > 1:
                    print (f'Правильно!\nОсталось решить {task_number - i -1} прим.')
                    i += 1

                elif user_answer == answer and (task_number - i) == 1:
                    print('Правильно!')
                    i += 1

                elif user_answer != answer and (task_number - i) >= 1:
                    print(f'Ошибка! Правильный ответ = {answer}\nОсталось решить {task_number - i} прим.')
                    mistakes += 1

                else:
                    print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Круто! Вы решили все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Вы допустили всего одну ошибку за {time_min} мин. {time_sec} сек. Будьте внимательнее!")
            elif mistakes <= 4:
                print(f"Неплохо! Вы допустили {mistakes} ошибки за {time_min} мин. {time_sec} сек. Вам нужно потренироваться")
            else:
                print(f"Вы совершили {mistakes} ошибок за {time_min} мин. {time_sec} сек. Выполните это задание еще три раза")

        elif operation == '-':

            while True:
                number_diff = input('Введите количество вычитаемых чисел ')
                try:
                    int(number_diff)
                except:
                    print(error_value)
                    continue
                break
            number_diff = int(number_diff)

            i = 0
            mistakes = 0
            time_start = time.time()
            while i < task_number:
                k = 1
                list_diff = []

                while k <= number_diff:
                    list_diff.insert(k, random.randrange(2, max_number))
                    k += 1
                list_diff.insert(0, random.randrange(4, max_number) + sum(list_diff))
                answer = list_diff[0] - sum(list_diff[1:])

                list_diff_str = []
                for item in list_diff:
                    list_diff_str.append(str(item))
                str_diff = ' - '.join(list_diff_str)
                user_answer = input(str_diff + ' = ')

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

                else:
                    print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Круто! Вы решили все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Вы допустили всего одну ошибку за {time_min} мин. {time_sec} сек. Будьте внимательнее!")
            elif mistakes <= 4:
                print(f"Неплохо! Вы допустили {mistakes} ошибки за {time_min} мин. {time_sec} сек. Вам нужно потренироваться")
            else:
                print(f"Вы совершили {mistakes} ошибок за {time_min} мин. {time_sec} сек. Выполните это задание еще три раза")

        elif operation == '*':
            while True:
                number_factors = input('Введите количество множителей ')
                try:
                    int(number_factors)
                except:
                    print(error_value)
                    continue

                if int(number_factors) <=1:
                    print(error_value)
                    continue
                break
            number_factors = int(number_factors)
            i = 0
            mistakes = 0
            time_start = time.time()

            while i < task_number:
                k = 1
                list_product = []
                while k <= number_factors:
                    list_product.append(random.randrange(2, max_number))
                    k += 1

                answer = 1
                for item in list_product:
                    answer = item * answer

                list_product_str = []
                for item in list_product:
                    list_product_str.append(str(item))
                str_product = ' * '.join(list_product_str)

                user_answer = input(str_product + ' = ')

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

                else:
                    print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Круто! Вы решили все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Вы допустили всего одну ошибку за {time_min} мин. {time_sec} сек. Будьте внимательнее!")
            elif mistakes <= 4:
                print(f"Неплохо! Вы допустили {mistakes} ошибки за {time_min} мин. {time_sec} сек. Вам нужно потренироваться")
            else:
                print(f"Вы совершили {mistakes} ошибок за {time_min} мин. {time_sec} сек. Выполните это задание еще три раза")

        elif operation == '/':

            while True:
                number_divisors = input('Введите количество делителей ')
                try:
                    int(number_divisors)
                except:
                    print(error_value)
                    continue
                break
            number_divisors = int(number_divisors)

            i = 0
            mistakes = 0
            time_start = time.time()


            while i < task_number:
                k = 1
                list_division = []

                while k <= number_divisors:
                    list_division.insert(k, random.randrange(2, max_number))
                    k += 1

                tmp_division = 1
                for item in list_division:
                    tmp_division = tmp_division * item

                answer = random.randrange(2, max_number)

                list_division.insert(0, answer * tmp_division)

                list_division_str = []
                for item in list_division:
                    list_division_str.append(str(item))
                str_division = ' / '.join(list_division_str)
                user_answer = input(str_division + ' = ')

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

                else:
                    print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Круто! Вы решили все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Вы допустили всего одну ошибку за {time_min} мин. {time_sec} сек. Будьте внимательнее!")
            elif mistakes <= 4:
                print(
                    f"Неплохо! Вы допустили {mistakes} ошибки за {time_min} мин. {time_sec} сек. Вам нужно потренироваться")
            else:
                print(f"Вы совершили {mistakes} ошибок за {time_min} мин. {time_sec} сек. Выполните это задание еще три раза")

        if operation == '=':

            while True:
                number_actions = input('Введите количество действий ')
                try:
                    int(number_actions)
                except:
                    print(error_value)
                    continue
                break

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

                list_actions.pop(len(list_actions) - 1)
                list_actions_str = []

                for item in list_actions:
                    list_actions_str.append(str(item))
                str_tmp = ' '.join(list_actions_str)
                answer = eval(str_tmp)

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
            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Круто! Вы решили все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(
                    f"Хорошо! Вы допустили всего одну ошибку за {time_min} мин. {time_sec} сек. Будьте внимательнее!")
            elif mistakes <= 4:
                print(
                    f"Неплохо! Вы допустили {mistakes} ошибки за {time_min} мин. {time_sec} сек. Вам нужно потренироваться")
            else:
                print(
                    f"Вы совершили {mistakes} ошибок за {time_min} мин. {time_sec} сек. Выполните это задание еще три раза")

        break

    user_continue = input('Нажмите Enter, чтобы продожить или любой символ для выхода из программы ')
    if user_continue != "":
        break
