"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_f = open("TfT_2.txt", "r")
words_tmp = 0
string_num = 0
words_num = 1

for line in my_f:
    string_num += 1
    words_num += words_tmp
    words_tmp = 1

    for letter in line:

        if letter != ' ' and ',':
            continue
        else:
            words_tmp += 1

    if words_tmp == 1:
        print(f'Only one word in string {string_num}')
    else:
        print(f'Words in string {string_num} - {words_tmp}')
words_num = words_num + words_tmp - 1
print(f'String number = {string_num}')
print(f'Words number - {words_num}')

my_f.close()

"""
Программу легко обмануть, если ставить после слов несколько пробелов
"""