import random, time

print("Реши правильно 10 примеров")
while True:

    max_number = input('Введи максимальное число ')
    operation = input('Выбери действие с числами сложение или вычитание ( + или - ) ')
    if max_number.isdigit() and (operation == "+" or operation == "-"):
        max_number = int(max_number)
        task_number = 10
        if operation == '+':
            i = 0
            mistakes = 0
            time_start = time.time()
            while i < task_number:
                a = random.randrange(3, max_number)
                b = random.randrange(3, max_number)
                answer = a + b
                user_answer = input(f"{a} + {b} = ")
                try:
                    int(user_answer)
                except:
                    print('Введены неверные данные')
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
                    print(f'Ошибка!\nОсталось решить {task_number - i} прим.')
                    mistakes += 1

                else:
                    print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Молодец! Ты решил все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Ты допустил всего одну ошибку за {time_min} мин. {time_sec} сек. Будь внимательнее!")
            elif mistakes <= 4:
                print(f"Неплохо! Ты допустил {mistakes} ошибки за {time_min} мин. {time_sec} сек. Тебе нужно потренироваться")
            else:
                print(f"Ты совершил {mistakes} ошибок за {time_min} мин. {time_sec} сек. Хочешь быть дворником?")

        elif operation == '-':
            i = 0
            mistakes = 0
            time_start = time.time()
            while i < task_number:
                a = random.randrange(3, max_number)
                b = random.randrange(3, max_number)
                answer = a - b
                if answer >= 0:
                    user_answer = input(f"{a} - {b} = ")
                    try:
                        int(user_answer)
                    except:
                        print('Введены неверные данные')
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
                        print(f'Ошибка!\nОсталось решить {task_number - i} прим.')
                        mistakes += 1

                    else:
                        print('Сломал программу')

            time_stop = time.time()
            user_time = time_stop - time_start
            time_min = round(user_time // 60)
            time_sec = round(user_time % 60)

            if mistakes == 0:
                print(f"Молодец! Ты решил все примеры без ошибок за {time_min} мин. {time_sec} сек.")
            elif mistakes == 1:
                print(f"Хорошо! Ты допустил всего одну ошибку за {time_min} мин. {time_sec} сек. Будь внимательнее!")
            elif mistakes <= 4:
                print(f"Неплохо! Ты допустил {mistakes} ошибки за {time_min} мин. {time_sec} сек. Тебе нужно потренироваться")
            else:
                print(f"Ты совершил {mistakes} ошибок за {time_min} мин. {time_sec} сек. Хочешь быть дворником?")

        user_continue = input('Нажми Enter, чтобы продожить или любой символ для выхода из программы ')
        if user_continue != "":
            break


