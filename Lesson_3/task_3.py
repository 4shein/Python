# var 1

# def my_func(a, b, c):
#     if min(a, b, c) == c:
#         return a + b
#     elif min(a, b, c) == b:
#         return a + c
#     else:
#         return b + c
# print(my_func(2,4,6))

# var 2
def my_func(a, b, c):
    d = min (a, b, c)
    return a + b + c - d
print(my_func(8,4,6))