"""
2)Даны два словаря my_dict_1 и my_dict_2.
а) Создать список из ключей, которые есть в обоих словарях.
б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
г) Объединить эти два словаря в новый словарь по правилу:
если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
если ключ есть в двух словарях -
поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

{1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
"""
my_dict_1 = {1: 1, 2: 2, 3: 3}
my_dict_2 = {11: 11, 2: 22, 3: 33}
print(f'My first dictionary: {my_dict_1}', f'My second dictionary: {my_dict_2}', sep="\n")

# A
# add new_list_1
my_list_1 = []
# cycle for key in both dictionary
for key in my_dict_1.keys() & my_dict_2.keys():
    # key appended to new_list_1
    my_list_1.append(key)
print("Keys in both dictionary: ", my_list_1)

#  B
# create list_2 with keys in first dictionary, but not in second dictionary
new_list_2 = list(my_dict_1.keys() - my_dict_2.keys())
print("Keys in first dictionary, but not in second dictionary: ", new_list_2)

# C
# add new_dict
new_dict = {}
# cycle for keys in first dictionary, but not in second dictionary
for key in my_dict_1.keys() - my_dict_2.keys():
    # add key and value to new_dict
    new_dict[key] = my_dict_1[key]
print("New dictionary with key/value in first dictionary, but not in second dictionary:", new_dict)

# D
# # add new_dict
new_dict_1 = {}
# cycle for key for both dictionary
for key in my_dict_1.keys() | my_dict_2.keys():
    # if same keys in both dictionary, combinate value
    if key in my_dict_1.keys() & my_dict_2.keys():
        new_dict_1[key] = [my_dict_1[key], my_dict_2[key]]
    # if keys only in first dictionary, add key and value to new_dict
    elif key in my_dict_1.keys() - my_dict_2.keys():
        new_dict_1[key] = my_dict_1[key]
    # if keys only in second dictionary, add key and value to new_dict
    elif key in my_dict_2.keys() - my_dict_1.keys():
        new_dict_1[key] = my_dict_2[key]
print("New dictionary combinate from both dictionary: ", new_dict_1)
