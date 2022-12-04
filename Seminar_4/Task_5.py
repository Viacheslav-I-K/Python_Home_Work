
'''
Даны два файла (equantions1.txt и equantions2.txt), в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. 
Степени многочленов могут отличаться.
'''

with open('equantions1.txt', 'rt') as f:
    equant1 = f.readline()
print("Первое уравнение: ", equant1)

with open('equantions2.txt', 'rt') as f:
    equant2 = f.readline()
print("Второе уравнение: ", equant2)


def convert_equant(equant): # Преобразование в более удобную форму для работы
    equant_new = equant.replace(" - ", " -")
    equant_new = equant_new.replace(" * X ", "")
    equant_new = equant_new.replace(" + ", " +")
    equant_new = equant_new.replace(" * ", "*")
    equant_new = equant_new.replace(" = 0", "")
    return equant_new


def summ_equant(equant1, equant2): # Сумирование значений элементов по одинаковым ключам + перевод в строку и добавление знака '+'
    res_equant = {}
    for i, k in equant1.items():
        res_equant[i] = int(k)
        
    for i, k in equant2.items():
        if i not in res_equant:
            res_equant[i] = int(k)
        else:
            res_equant[i] += int(k)     

    for key, item in res_equant.items():
        if int(item) > 0:
           res_equant[key] = '+' + str(item)
        else:
            res_equant[key] = str(item)

    return res_equant
    

def equant_split(equant): # Разделение уравнения на элементы и добавление в словарь
    new_equant = []
    for el in equant:
       new_equant.append(el.split("**"))

    dict_equant = {}
    for i in new_equant:
        dict_equant[i[1]] = i[0]
       
    return dict_equant


def res_equant(sum_equants): # Преобразование словаря в в строку и добавление элементов, чтоб получилось уравнение
    res_lst = ''
    for key, item in sum_equants.items():
        if int(key) >= 2:
            res_lst += str(item) + ' * X' + '**' + key
        elif int(key) == 1:
            res_lst += str(item) + ' * X'
        else:
            res_lst += str(item)
        
    res_lst = res_lst.replace("**", "^")
    res_lst = res_lst.replace("+", " + ")
    res_lst = res_lst.replace("-", " - ")
    res_lst += ' = 0'
    return res_lst


equant1 = equant1.replace(" * X", "")
equant2 = equant2.replace(" * X", "")
equant1 = convert_equant(equant1).split(" ")
equant2 = convert_equant(equant2).split(" ")
print(equant1)
print(equant2)

equant1 = equant_split(equant1)
equant2 = equant_split(equant2)
print(equant1)
print(equant2)

sum_equants = summ_equant(equant1, equant2)
print("Результирующий словарь: ", sum_equants)

result = res_equant(sum_equants)
print("Результирующее уравнение: ", result)

with open('result_equantions.txt', 'wt', encoding='utf-8') as f:
    f.write(result)
