# Task 1

my_list = ('word', 23, -13, [3, 5], {"cd":5} , False, 3.14, None)

print(my_list)
for el in my_list:
    print(el, "-", type(el))

# Task_2
user_list = []
while True:
    user_input = input(f"Input data. Press Q to exit.\n")
    if user_input == ("Q") or user_input == ("q"):
        break
    else:
        user_list.append(user_input)
temp_circle = 0
print(user_list)
user_list_length = len(user_list)
# print(user_list_length)

while user_list_length - 1 > temp_circle and user_list_length % 2 >= 0:
    temp_value = user_list[temp_circle]
    user_list[temp_circle] = user_list[temp_circle + 1]
    user_list[temp_circle + 1] = temp_value
    temp_circle = temp_circle + 2
    # print(temp_circle)
    # print(user_list_length % 2)
print("Thinking...")
# print(user_list_length % 2)
print(user_list)

# Task 3 my var.
my_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer",\
     7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
user_month = input(f"Input month by number from 1 to 12\n")
user_month = int(user_month)
print(my_dict.get(user_month))

# Task 3 SR var

seasons = ("Winter",
           "Spring",
           "Summer",
           "Autumn",
           )
user_month = input(f"Input month by number from 1 to 12\n")
user_month = int(user_month)
seasons_idx = user_month // 3 % 4
print(seasons_idx)
print(seasons[seasons_idx])

# Task 4

user_words = input("Input words\n")
for idx, word in enumerate(user_words.split(" "),1):
    user_words.split(" ")
    print(f"{idx} : {word[:10]}")

# Task 5

my_list = [7, 5, 3, 3, 2]
user_raining = input("Input new rating by number from 1 to 10\n")
user_raining = int(user_raining)
my_list.append(user_raining)
my_list.sort()
print(my_list)

# Task 6

product_template = {
    'name': ("name", str),
    'price': ("price", int),
    'amount': ("amount", int),
    'unit': ("unit", str),
}

next_enter = True
auto_inc = 1
product_list = []

while next_enter:
    product = {}
    for key, value in product_template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\nWrong value")
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc += 1

    while True:
        next_add = input("Add next product? Yes/No\n")
        if next_add.lower() in ('yes', 'no'):
            next_enter = next_add.lower() == 'yes'
            break
        else:
            print('Wrong value, repeat please')
print (product_list)
product_analytics = {}
for key in product_template:
    result = []
    for itm in product_list:
        result.append(itm[1][key])
        product_analytics[key] = result

    product_analytics[key] = [itm[1][key] for itm in product_list]

print(product_analytics)