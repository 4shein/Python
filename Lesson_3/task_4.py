# var 1

def my_func(x, y):
    y = abs(y)
    return x**y

# var 2

# def my_func(x, y):
#     i = 1
#     y = abs(y)
#     while i < y:
#         x = x+x
#         i += 1
#     return x

user_value_x  = int(input("Input X\n"))
user_value_y = int(input("Input Y\n"))
print(my_func(user_value_x, user_value_y))

