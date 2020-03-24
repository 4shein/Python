while True:
    user_data = input('Input data\n')
    if user_data != '':
        user_file = open('test.txt', 'a')
        user_file.write(user_data)
        user_file.write('\n')
        user_file.close()
    else:
        break
user_file = open('test.txt', 'r')
print(user_file.read())
