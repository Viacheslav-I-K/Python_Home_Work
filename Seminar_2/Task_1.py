
'''
1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0.56 -> 11
'''

valu = input("Введите вещественное число: ").replace("-", "")
res = 0
for i in valu:
    if i != ".":
        res += int(i)

print(f"Сумма цифр: {res}")