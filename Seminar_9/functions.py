import csv
from telebot import TeleBot, types


def read_file():
    with open('base.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter = ";")
        arr = []
        for line in reader:
            arr.append(line)
    return arr


def write_file(arr):
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


def read_input_file(file_name):
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

