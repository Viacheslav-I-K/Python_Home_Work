from math import sin
from math import radians
from math import pi
'''
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
# Высчитывать число Пи будем с использованием ограничения (x * sin(180 / x))

d = float(input("Введите предел погрешности вычислений числа Пи (в задании d = 0.001): "))


def value_pi(d):
    count = 0
    n = 100
    res = radians(n * sin(180 / n))
    while (d + d * 0.05) < (pi - res) > (d - d * 0.05):
        n += 100
        res = radians(n * sin(180 / n))
        count += 1
    print(f"Число Пи, которое мы вычислили = {res}")
    print(f"Число Пи через модуль math = {pi}")
    print("Погрешность измерений d = ", pi - res)
    print("Количество итераций: ", count)


value_pi(d)
