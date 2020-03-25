user_data = input("Input data with space\n")
new_list = []
temp_sum = 0
if user_data.isdigit():
    while True:
        tmp = user_data.split(" ")
        for el in tmp:
            if el.isdigit():
                new_list.append(int(el))
        # print(tmp)
        print(sum(new_list))
        break
elif user_data == "q":
    print(sum(new_list)+temp_sum)
else:
    temp_sum = sum(new_list) + temp_sum