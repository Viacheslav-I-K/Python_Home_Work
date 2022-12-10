
'''
 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''


def spl():
    with open('user_text.txt', 'r', encoding='utf-8') as of:
        tex = str(of.readline())
    
    lst = []
    size = len(tex)
    res = tex[0]

    for i in range(1, size):
        if tex[i] == tex[i - 1]:
            res += tex[i]
            if i == size -1:
                lst.append(res)   
        else:
            lst.append(res)
            res = tex[i]
    return lst


def count_text(lst):
    res = ''
    for elem in lst:
        size = len(elem)
        if size < 10:
            res += str(size) + elem[0]
        else:
            while size != 0:
                if size > 9:
                    res += '9' + elem[0]
                    size -= 9
                else:
                    res += str(size) + elem[0]
                    size -= size

    with open('user_txt_conv.txt', 'w', encoding='utf-8') as ofw:
        ofw.write(res)
    return res


user_text = str(input("Введите текст на кирилице, через пробел: "))

with open('user_text.txt', 'w', encoding='utf-8') as ut:
    ut.write(user_text)


lst = spl()
print("Разбил по символам", lst)

result = count_text(lst)
print("Сжал данные", result)



