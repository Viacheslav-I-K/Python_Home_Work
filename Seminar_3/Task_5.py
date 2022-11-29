
'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

num = int(input("Введите число: "))
lst = [0, 1]
lst_new = [1,]
res1 = 0
res2 = 1
res1_new = 0
res2_new = (-1)

for i in range(1, num):
    res = res1 + res2
    res_new = res1_new + res2_new
    lst.append(res)
    res1 = res2
    res2 = res
    res1_new = res2_new
    res2_new = res_new

    if i % 2 == 0:
        res_new = (-res_new)

    lst_new.append(res_new)

lst_new.reverse()
lst_new.extend(lst)
print(lst_new)


