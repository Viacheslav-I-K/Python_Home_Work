
from random import randint
'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
'''

# СТАРОЕ РЕШЕНИЕ. Менять буду функцию completion()
'''
size = int(input("Введите размер списков: "))
min_el = int(input("Введите минимальное значение элемента списка: "))
max_el = int(input("Введите максимальное значение элемента списка: "))


def completion(size, min_el, max_el):# Заполняет список
    lst = []
    for i in range(0, size):
        num = randint(min_el, max_el)
        lst.append(num)
    return lst


def dict_repetitive(lst1, dictionary):# функция для создания словаря (ключи - значения элементов из списка, а значения - количество повторений)
    for i in lst1:
        dictionary[i] = dictionary.get(i, 0) + 1
    
    return dictionary


def non_repetitive(dictionary):# Проходим по словарю и сохраняем в список lst только те ключи, элементы которых = 1 (т.е. повторялись только единожды)
    lst = []
    for key in dictionary.items():
        if key[1] == 1:
            lst.append(key[0])
    if len(lst) != 0:
        print("Неповторяющиеся элементы: ", *lst)
    else:
        print("Неповторяющиеся элементы отсутствуют.")


lst1 = completion(size, min_el, max_el)
lst2 = completion(size, min_el, max_el)
print("Итоговый список №1: ", lst1)
print("Итоговый список №2: ", lst2)


dictionary = {}
dictionary = dict_repetitive(lst1, dictionary)
dictionary = dict_repetitive(lst2, dictionary)
print("Словарь значений двух списков: ", dictionary)

non_repetitive(dictionary)
'''

# НОВОЕ РЕШЕНИЕ. Поменял функцию completion()

size = int(input("Введите размер списков: "))
min_el = int(input("Введите минимальное значение элемента списка: "))
max_el = int(input("Введите максимальное значение элемента списка: "))


#def completion(size, min_el, max_el):# Заполняет список
    #lst = []
    #for i in range(0, size):
        #num = randint(min_el, max_el)
        #lst.append(num)
    #return lst


def dict_repetitive(lst1, dictionary):# функция для создания словаря (ключи - значения элементов из списка, а значения - количество повторений)
    for i in lst1:
        dictionary[i] = dictionary.get(i, 0) + 1
    
    return dictionary


def non_repetitive(dictionary):# Проходим по словарю и сохраняем в список lst только те ключи, элементы которых = 1 (т.е. повторялись только единожды)
    lst = []
    for key in dictionary.items():
        if key[1] == 1:
            lst.append(key[0])
    if len(lst) != 0:
        print("Неповторяющиеся элементы: ", *lst)
    else:
        print("Неповторяющиеся элементы отсутствуют.")


lst1 = [randint(min_el, max_el) for i in range(0, size)]
lst2 = [randint(min_el, max_el) for i in range(0, size)]
print("Итоговый список №1: ", lst1)
print("Итоговый список №2: ", lst2)


dictionary = {}
dictionary = dict_repetitive(lst1, dictionary)
dictionary = dict_repetitive(lst2, dictionary)
print("Словарь значений двух списков: ", dictionary)

non_repetitive(dictionary)
