import random, time

print("Реши правильно 20 примеров")
i = 0
mistakes = 0
while i < 20:
    a = random.randrange (1, 10)
    b = random.randrange (1, 10)
    answer = a + b
    user_answer = input (f"{a} + {b} = ")
    user_answer = int(user_answer)
    if user_answer == answer:
        print ('Правильно!')
        i += 1
    else:
        print('Ошибка! Попробуй еще раз')
        mistakes += 1
if mistakes == 0:
    print("Молодец! Ты решил все примеры без ошибок!")
elif mistakes == 1:
    print(f"Хорошо! Ты допустил всего одну ошибку. Будь внимательнее!")
elif mistakes <= 4:
    print(f"Неплохо! Ты допустил {mistakes} ошибки. Тебе нужно потренироваться")
else:
    print(f"Ты совершил {mistakes} ошибок. Хочешь быть дворником?")