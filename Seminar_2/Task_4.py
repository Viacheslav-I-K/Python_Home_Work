
'''
4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
Позиции вводятся с клавиатуры.
'''
N = abs(int(input("Введите число N: ")))
num_1 = int(input("Введите индекс 1 числа для вычисления произведения со 2 числом: "))
num_2 = int(input("Введите индекс 2 числа для вычисления произведения с 1 числом: "))

if 0 <= num_1 <= (N * 2) and 0 <= num_2 <= (N * 2):
    lst = []
    for num in range((-N), N + 1):
        lst.append(num)
    print(f"Список из элементов от -N до N: {lst}")
    print(f"Произведение двух элементов списка = {lst[num_1] * lst[num_2]}")
else:
    print("Введеный диапазон чисел для расчета произведения не верный!")
    
