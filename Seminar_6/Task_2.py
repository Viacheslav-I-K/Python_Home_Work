# УЖЕ ИСПОЛЬЗОВАЛ list compehension на 19 строке
'''
Напишите программу, удаляющую из файла все слова, содержащие "абв".
'''

user_text = str(input("Введите текст на кирилице, через пробел: "))

with open('file.txt', 'w', encoding='utf-8') as in_fl:
    lst_in = in_fl.write(user_text)

n = False
while n == False:
    chr = input("Данные были внесены в файл. Для продолжения нажмите 'Enter': ")
    if chr == '':
        print("Идем дальше!")
        n = True

with open('file.txt', 'rt', encoding='utf-8') as out_fl:
    lst_new = list(filter(lambda x: 'абв' not in x.lower(), out_fl.readline().split()))
print(*lst_new)
print(type(lst_new))

with open('file_new.txt', 'wt', encoding='utf-8') as f:
    f.write(str(" ".join(lst_new)))
