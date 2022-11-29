
'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
from random import randint

N = int(input("Введите количество элементов в списке: "))
lst = []

for i in range(N):
    num = randint(1, 20)
    lst.append(num)

print(lst)

size = len(lst) - 1
count = 0
lst_new = []
while count <= size:
    lst_new.append(lst[count] * lst[size])
    count += 1
    size -= 1

print(f"Произведение парных элементов списка: {lst_new}")
