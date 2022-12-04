
'''
Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
'''

num = int(input("Введите натуральное число для разложения его на простые множители: "))

def prime_factors(num):
    prime_fact = []
    count = 2
    while num >= 2:
        if num % count == 0:
            prime_fact.append(count)
            num /= count
        else:
            count +=1
    return prime_fact


prime_fact = prime_factors(num)
print(num, "= ", end="")
print(*prime_fact, sep=" x ")


