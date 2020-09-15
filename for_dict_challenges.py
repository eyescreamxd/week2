# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# for i in students:
#     print(f'{i.values()[0]} {students.count(i)}')

names = []
for j in students:
    for i in j.keys():
        names.append(j[i])

# print(names)
for i in set(names):
    print(f"{i}: {', '.join(names).count(i)}")

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('***********************************************************************************')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = []
for j in students:
    for i in j.keys():
        names.append(j[i])
# print(names)
count_names = {}
for i in set(names):
    count_names[i] = ', '.join(names).count(i)
# u = 0
# for k in count_names:
#     if u < count_names[k]:
#         u = count_names[k]
# print(count_names)
print(max(count_names, key=lambda k: count_names[k]))

# Пример вывода:
# Самое частое имя среди учеников: Маша
print('***********************************************************************************')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
names = []
for j in school_students:
    for a in j:
        for i in a.keys():
            names.append(a[i])

# print(names)
count_names = {}
for i in set(names):
    count_names[i] = ', '.join(names).count(i)
# print(count_names)
count_names.pop(min(count_names, key=lambda k: count_names[k]))
print(count_names)

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('***********************************************************************************')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for iteration in school:
    m = 0
    f = 0
    for list in iteration['students']:
        if is_male[list['first_name']]:
            m += 1
        else:
            f += 1
    print(f"В классе {iteration['class']} {m} мальчика и {f} девочки")

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print('***********************************************************************************')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '666',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
count = {'female': {'classname': None, 'count': 0},
         'male': {'classname': None, 'count': 0}}  # {'female': 'classname', 'male': 'classname'}
for iteration in school:
    m = 0
    f = 0
    for list in iteration['students']:
        if is_male[list['first_name']]:
            m += 1
        else:
            f += 1
    if m > f and count['male']['count'] < m:
        count['male']['classname'] = iteration['class']
        count['male']['count'] = m
    elif f > m and count['male']['count'] < f:
        count['female']['classname'] = iteration['class']
        count['female']['count'] = f

print(
    f"Больше всего мальчиков в классе {count['male']['classname']}\
    \nБольше всего девочек в классе {count['female']['classname']}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
