import csv
from telebot import TeleBot, types


def read_file(): # Считывание данных из файла в список 
    with open('base.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ";")
        arr = []
        for line in reader:
            arr.append(line)
    return arr


def write_file(arr): # Запись данных из списка в файл
    with open('base.csv', 'w', encoding='utf-8') as f:
        for val in arr:
            text = ";".join(val)
            f.writelines(f"{text}\n")


def input_console(array, text):# для ручного ввода новых данных
    manual_data = text
    data_list = manual_data.split(';')
    if text not in array:
        array.append(data_list)
    else:
        return False
    return array


def delet_user(array, text):# для поиска по номеру телефона
    delete_elem = []
    for data in array:
        for elem in data:
            if text == elem:
                delete_elem = data
    if delete_elem != []:
        array.remove(delete_elem)
        return array
    else:
        return False


def search_user_phone(array, text):# для поиска по номеру телефона
    for data in array:
        for elem in data:
            if text == elem:
                return data
    return False


def read_input_file(file_name): # Считывание импортируемого файла и занесение данных в список
    with open(f'{file_name}', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ";")
        arr = []
        for line in reader:
            arr.append(line)
    return arr


def input_file(array_base, array_file):# для ручного ввода новых данных
    for data in array_file:
        if data not in array_base and data != '':
            array_base.append(data)
    
    return array_base


def read_input_file_html(file_name): # Считывание импортируемого файла html и занесение данных в список
    with open(file_name, 'r', encoding='utf-8') as file:
        arr = []
        res = []
        tr = False
        text = file.readlines()

        for i in text:
            if '<tr>' in i:
                tr = True

            if '<td>' in i and tr == True:
                res.append(i)
            
            if '</tr>' in i:
                arr.append(res)
                res = []
                tr == False

    res1 = ''
    mass2 = []
    for f in arr:
        mass = []
        count = 0
        for t in f:
            if count > 0:
                res1 = t.replace("\t", "")
                res1 = res1.replace("<td>", "")
                res1 = res1.replace("</td>", "")
                res1 = res1.replace("\n", "")
                res1 = res1.replace(" ", "")
                mass.append(res1)
                res1 = ""
                
            count += 1     
        if mass:
            mass2.append(mass)

    return mass2


def write_html(arr):

    with open(f'base.html', 'w', encoding='utf-8') as file:
        file.writelines(f'<!DOCTYPE html>\n')
        file.writelines(f'<html lang="ru">\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\t\t<meta charset="utf-8">\n')
        file.writelines(f'\t\t<title>Phone Book</title>\n')
        file.writelines(f'\t<head>\n')
        file.writelines(f'\n')
        file.writelines(f'\t<body>\n')
        file.writelines(f'\t\t<h2>Phone Book</h2>\n')
        file.writelines(f'\t\t<table border="1" width="600">\n')
        file.writelines(f'\t\t\t<thead>\n')
        file.writelines(f'\t\t\t<tbody>\n')
        file.writelines(f'\t\t\t\t<tr>\n')
        file.writelines(f'\t\t\t\t\t<th>№</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Фамилия</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Имя</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Телефон</th>\n')
        file.writelines(f'\t\t\t\t\t<th>Комментарий</th>\n')
        file.writelines(f'\t\t\t\t</tr>\n')
        file.writelines(f'\t\t\t</thead>\n')
        count = 1
        for text in arr:
            file.writelines(f'\t\t\t\t<tr>\n')
            file.writelines(f'\t\t\t\t\t<td>{count}</td> \n')
            for item in text:
                file.writelines(f'\t\t\t\t\t<td>{item}</td> \n')
            file.writelines(f'\t\t\t\t</tr>\n')
            count += 1
        file.writelines(f'\t\t\t</tbody>\n')
        file.writelines(f'\t\t</table>\n')
        file.writelines(f'\t</body>\n')
        file.writelines(f'</html>')


def mutationes_user_phone(array, text):# для поиска по номеру телефона и внесение изменения в данные\
    search_index = -1
    count = 0
    for data in array:
        for elem in data:
            if text == elem:
                search_index = count
                return search_index
        count += 1
    return False
    

def input_mutationes(array, text):# для ручного ввода новых данных
    data_list = text.split(';')
    return data_list