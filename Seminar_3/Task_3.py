
'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

import random

N = int(input("Введите количество элементов в списке: "))
lst = []

for i in range(N):
    num = round(random.uniform(1, 10), 2)
    lst.append(num)

print(lst)

min = round(lst[0] % 1, 2)
max = round(lst[0] % 1, 2)
for i in lst:
    if (i % 1) > max:
        max = round(i % 1, 2)
    else:
        if (i % 1) < min:
            min = round(i % 1, 2)

print(f"Разница между максимальным ({max}) и минимальным ({min}) значением дробной части элементов списка = {round(max - min, 2)}")
