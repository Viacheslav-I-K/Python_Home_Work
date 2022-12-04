from random import randint
'''
Задана натуральная степень k. Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

k = int(input("Введите натуральную степень: "))

def quantity_el(k):
    if k > 0 and k < 4:
        quant = randint(k, k + 1)
    elif k > 3 and k < 7:
        quant = randint(4, 6)
    else:
        quant = randint(6, 7)
    return quant


def degrees(k, quant):# Определение степеней и сортировка от от большей к меньшей
    degrees = []
    while quant > len(degrees):
        num = randint(0, k)
        if num not in degrees:
            degrees.append(num)
        
    degrees.sort(reverse=True)
    return degrees
    

def equantions(k, degree):
    equant = []
    elem = ''
    chr_first_el = randint(0, 1)
    if chr_first_el == 0:
        chr_first_el = '+'
    else:
        chr_first_el = '-'
    elem = chr_first_el
    for i in range(len(degree)):
        num = randint(0, 100)
        chr = randint(0, 1)
        
        if chr == 0:
            chr = '+'
        else:
            chr = '-'

        if i != len(degree) - 1:
            elem += f'{num} * X**{degree[i]} {chr} '
        else:
            elem += f'{num} * X**{degree[i]} = 0'
    equant.append(elem)
    return equant

    
quant = quantity_el(k)

degree1 = degrees(k, quant)
degree2 = degrees(k, quant)
print(degree1)
print(degree2)

equant1 = equantions(k, degree1)
equant2 = equantions(k, degree2)
print("Первое уравнение: ", equant1)
print("Второе уравнение: ", equant2)

with open('equantions1.txt', 'w', encoding='utf-8') as f:
    f.write(*equant1)

with open('equantions2.txt', 'w', encoding='utf-8') as f:
    f.write(*equant2)
