
'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
num = int(input("Введите число для перевода его в двоичную систему: "))
lst = []
while num > 0:
    res = num % 2
    lst.append(res)
    print(res)
    print(lst)
    num = int(num / 2)
    print("num =", num)

lst.reverse()
print(lst)
