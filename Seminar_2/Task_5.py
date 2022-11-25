from random import randint
'''
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint
'''

N = int(input("Введите количество элементов в списке: "))

lst = []
for i in range(N):
    lst.append(randint(0, 100))
print(lst)

# Самы простой способ перемешать список - включить его в множество))). Но ниже будет второй вариант реализации без множества). Но тут
# Есть минус - повторяющиеся элементы не распечатываются) 
'''
print(lst)
mixed = set()
mixed.update(lst)
print(mixed)
'''

# Второй вариант решения
new_lst = []
size = len(lst)
for i in range(size):
    n = randint(0, size - 1)
    new_lst.append(lst[n])
    lst.pop(n)
    size -= 1
print(new_lst)