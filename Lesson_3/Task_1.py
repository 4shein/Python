def my_f(a, b):
    if b == 0:
        print('Error. Division by zero.')
    else:
        return a / b

user_value_a = input(f'Input A\n')
user_value_a = int (user_value_a)
user_value_b = input(f'Input B\n')
user_value_b = int (user_value_b)
print(my_f(user_value_a, user_value_b))