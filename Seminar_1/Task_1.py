
'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
num = input("Введите число обозначающее день недели: ")

def day_week(n):
    if n == "6" or n == "7": print("да")
    elif 1 < int(n) < 6: print("нет")
    else: print("Вы ввели что то не то!")

day_week(num)