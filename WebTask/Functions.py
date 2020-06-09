# def myfunc(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     if a % 2 != 0 or b % 2 != 0:
#         return max(a, b)
#
# print(myfunc(8, 5))

#
# import random
# i = 1
# mylist = []
# n = int(input("n= "))
#
# while i <= n:
#
#     mylist.append(random.randrange(1, 10))
#     i += 1
#
# print(mylist)
# mylist_str = []
# for item in mylist:
#     mylist_str.append((str(item)))
# print(sum(mylist))
# print(mylist_str)
#
# mystr = (' + '.join(mylist_str) + ' = ')
# print(mystr)
# c = 5
# b = [num for num in range(1, 51) if len(b) < 5]
# print(b)

while True:
    a = input('Input number')
    try:
        a = int(a)
        break

    except:
        print('Error')
        print('1')
print('2')
