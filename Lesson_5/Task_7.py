"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
i = 0
average_profit = 0
my_dict = dict()
my_list = list()

with open('data_task7.txt', 'r') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0].split(':')[0]
        owership = tmp[1].split(':')[0]
        income = tmp[2].split(':')[0]
        expenses = tmp[3].split(':')[0]

        if int(income) > int(expenses):
            profit = int(income) - int(expenses)
            # print(profit)
            average_profit = average_profit + profit
            i += 1
            my_dict[name] = profit
        else:
            profit = int(income) - int(expenses)
            # print(profit)
            my_dict[name] = profit

    average_profit = average_profit / i
    # print(average_profit)
    # print(my_dict)
    my_list.append(my_dict)
    my_list.append({'average profit': average_profit})
    print(my_list)


with open('data_task7.json', 'w') as file:
    file.write(json.dumps(my_list))




