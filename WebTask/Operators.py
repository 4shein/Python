# st = 'Sam Print only the words that start with s in this sentence'
#
# for word in st.split():
#     if word[0].lower == 's':
#         print(word)

# a = list(range(0, 11, 2))
# print(a)

# list comprehensions
# b = [num for num in range(1, 51) if num % 3 == 0]
# print(b)

# st = 'Print every word in this sentence that has an even number of letter'
#
# for word in st.split():
#     if len(word) % 2 == 0:
#         print(word)

# a = list(range(1,101))
# for num in a:
#     if num % 3 == 0 and num % 5 == 0:
#         print(f'{num} FizzBuzz')
#     elif num % 3 == 0:
#         print(f'{num} Fizz')
#     elif num % 5 == 0 :
#         print(f'{num} Buzz')
#     else:
#         print(num)

# st = 'Creat a list of the first letter of every words in this string'
#
# mylist = [letter[0] for letter in st.split()]
# print(mylist)

# while i < task_number:
import random
number_diff = 3
max_number = 10
k = 1
list_diff = []
while k <= number_diff:
    list_diff.insert(k, random.randrange(2, max_number))
    k += 1
list_diff.insert(0, random.randrange(4, max_number) + sum(list_diff))

print(list_diff)
list_diff_str = []
for item in list_diff:
    list_diff_str.append(str(item))
str_diff = ' - '.join(list_diff_str)
user_answer = input(str_diff + ' = ')

print(str_diff)

