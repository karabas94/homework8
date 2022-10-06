"""
1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
а) Создать список и поместить туда имя самого молодого человека.
 Если возраст совпадает - поместить все имена самых молодых.
б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
в) Посчитать среднее количество лет всех людей из начального списка.
"""

user = [
    {"name": "Oleksandr", "age": 20},
    {"name": "Oleksandr", "age": 28},
    {"name": "Dmitriy", "age": 20},
    {"name": "Mykola", "age": 25},
]
print("List of dictionary: ", user)



# A
# add list with ages
ages = []
# add list with younger
young = []
# cycle for dictionaries in list user
for d in user:
    # ages appended to list "ages"
    ages.append(d["age"])
# list "ages" sorted
ages.sort()
# cycle for dictionaries in list user
for d in user:
    # if list ages with index 0 = age in dictionary
    if ages[0] == d["age"]:
        # name added to young list
        young.append(d["name"])
print("The youngest: ", young)



# B
# add list with names
name = []
# add list with longest name
long_name = []
# cycle for dictionaries in list user
for d in user:
    # len of name appended to list "name"
    name.append(len(d['name']))
# list "name" sorted
name.sort()
# cycle for dictionaries in list user
for d in user:
    # if list name with index -1 = len name in dictionary
    if len(d['name']) == name[-1]:
        # len of long name appended to list "long name"
        long_name.append(d['name'])
print("Longest name: ", long_name)



# C
import statistics

# add list with ages
age = []
# cycle for dictionaries in list user
for d in user:
    # ages appended to list "ages"
    age.append(d["age"])
# mean age for list age
mean_age = statistics.mean(age)
print("Mean age: ", mean_age)
