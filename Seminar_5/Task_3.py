
'''
Создайте программу для игры в "Крестики-нолики".

Вариант интерфейса:

 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9
'''

from random import randint

def step_players(): # Определяем ходит ли игрок №1 первым
    player1 = randint(1, 6)
    player2 = randint(1, 6)
    print(f"Игроку №1 выпало число: {player1}. Игроку №2 выпало число: {player2}")
    if player1 > player2:
        return True
    elif player2 > player1:
        return False
    else:
        return step_players()


def char_replace(lst, chars, name): # Вставляет символ игрока в сетку и проверяет не занята ли она
    while True:
        step = input(f"Игрок {name} введите номер ячейки куда поставить {chars}: ")
        if step.isdigit() and 1 <= int(step) <= 9:
            step = int(step)
        else:
            print("Номер ячейки введён некорректно!")

        if lst[step - 1] != 'X' and lst[step - 1] != 'O':
            lst[step - 1] = chars
            return lst
        else:
            print("Эта ячейка уже занята!")


def grid_print(lst): # Печать сетки игры
    res = ''
    print()
    for i in range(1, 10):
        if i % 3 == 0:
            res += str(f' {lst[i - 1]} ')
            print(res)
            if i < 7:
                print('---+---+---')
            else: print()
            res = ''
        else:
            res += str(f' {lst[i - 1]} ') + '|'


def win_comb(lst): # Проверка выиграл ли игрок
    print("Проверка победы", lst)
    win_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for ind_elem in win_comb:
        if lst[ind_elem[0]] == lst[ind_elem[1]] == lst[ind_elem[2]]:
            return True
        else:
            return False


grid_game = ['1', '2', '3', '4', '5', '6', '7',  '8', '9']
grid_print(grid_game)


name1 = input("Игрок №1 введите Ваше имя: ")
name2 = input("Игрок №2 введите Ваше имя: ")

chars = input(f"Пользователь {name1} выберите каким символом будете играть (1 - играю КРЕСТИКОМ; 2 - играю НОЛИКОМ): ")
if chars == '1':
    char1 = 'X'
    char2 = 'O'
else:
    char1 = 'O'
    char2 = 'X'


human1 = step_players()
if human1: print(f"Первым ходит {name1}")
else: print(f"Первым ходит {name2}")

wins = False
count = 1
while count <= 9 and wins == False:
    if human1:
        print(f"Ходит игрок {name1}")
        grid_game = char_replace(grid_game, char1, name1)
        if count > 3:
            wins = win_comb(grid_game)
    else:
        print(f"Ходит игрок {name2}")
        grid_game = char_replace(grid_game, char2, name2)
        if count > 3:
            wins = win_comb(grid_game)

    print("count = ", count)
    print("wins = ", wins)
    human1 = not human1
    grid_print(grid_game)
    count += 1
 
if human1 and wins:
    print(f'Победил {name2}')
elif not human1 and wins:
    print(f'Победил {name1}')
else:
    print('Ничья!')
