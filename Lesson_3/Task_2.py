
def my_func(**kwargs):
    return kwargs
print(my_func(name="Nikolay", surname="Shein", yaer_brth="1982", city="Moscow", email="4shein@gmail.com"))

# training
# mydict={
#     'name': ("name?", str),
#     'surname': ("surname?", str),
#     'year_brth': ("year birthday?", str),
#     'city': ("city?", str),
#     'phone': ("phone?", str),
#     'email': ("email?", str),
# }
# user_data = {}
# for key, value in mydict.items():
#     user_data_tmp = {}
#     while True:
#         user_value = input(f'{value[0]}\n')
#         user_data_tmp[key] = user_value
#         user_data.update(user_data_tmp)
#         break
# print(user_data)