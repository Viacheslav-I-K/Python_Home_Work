

def check_j(mes):
    if 'j' not in mes:
        return False
    else:
        return True


def ration(mes):
    lst = []
    if mes == '':
        return lst.append('0')
    res = ''
    size = len(mes)
    for i in range(size):
        if mes[i].isdigit() or mes[i] == '.' or mes[i] == 'j' or mes[i] == ')' or mes[i] == '(':
            res += mes[i]
        else:
            if res != '':
                lst.append(res)
                res = ''
                lst.append(mes[i])
        if i == size - 1:
            lst.append(res)
    return lst


def result(lst, check):
    size = len(lst)
    division_zero = False
    
    if size <= 1:
        return '0'

    if check:
        lst = "".join(lst)
        print(f'lst = {lst}')
        if ')+(' in lst:
            lst = lst.replace(")+(", ") + (")
            lst = lst.split()
        elif ')-(' in lst:
            lst = lst.replace(")-(", ") - (")
            lst = lst.split()
        elif ')*(' in lst:
            lst = lst.replace(")*(", ") * (")
            lst = lst.split()
        elif ')/(' in lst:
            lst = lst.replace(")/(", ") / (")
            lst = lst.split()

        if lst[2] == '0' and lst[1] == '/':
            division_zero = True

        lst[0] = lst[0][1:-1]
        lst[2] = lst[2][1:-1]

        if '-' in lst[0] or '+' in lst[0]:
            elem_0 = complex(lst[0])
        elif '-' not in lst[0] or '+' not in lst[0]:
            print('lst[0] = ' + lst[0])
            lst[0] = f'0+{lst[0]}'
            elem_0 = complex(lst[0])

        if '-' in lst[2] or '+' in lst[2]:
            elem_2 = complex(lst[2])
        elif '-' not in lst[2] or '+' not in lst[2]:
            lst[2] = f'0+{lst[2]}'
            elem_2 = complex(lst[2])

        if lst[1] == '+':
            res = complex(elem_0 + elem_2)
        if lst[1] == '-':
            res = complex(elem_0 - elem_2)
        if lst[1] == '*':
            res = complex(elem_0 * elem_2)
        if lst[1] == '/':
            res = complex(elem_0 / elem_2)
        
        if division_zero:
            return 'Ошибка'
        else:
            return str(res)

    else:
        res = int(lst[0])
        pos = 1
        while pos <= size:
            if lst[pos] == '+':
                res += int(lst[pos + 1])
                pos += 1
            elif lst[pos] == '-':
                res -= int(lst[pos + 1])
                pos += 1
            elif lst[pos] == '*':
                res *= int(lst[pos + 1])
            elif lst[pos] == '/':
                res /= int(lst[pos + 1])
            elif lst[pos] == '%':
                res %= int(lst[pos + 1])
            if pos != size - 1:
                pos += 1
            else:
                break

    return str(res)

