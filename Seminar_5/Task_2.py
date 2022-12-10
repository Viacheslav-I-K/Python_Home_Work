'''
 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
# В начале начал делать по своему, но на семинаре №6 увидел ваше модульное решение и все переделал)
from random import randint


def rules_game():
    print("ПРАВИЛА ИГРЫ:")
    print("В начале игры есть какое - то количество конфет.")
    print("Каждый игрок в свой ход берет от 1 до максимально разрешенного количества конфет.")
    print("Выигрывает тот, кто взял последнюю/последние конфеты.")
    print("Очередность хода игроков определяется жеребьевкой. Ходит тот, кому выпало большее число.")
    print("Если обоим игрокам выпало одинаковое число, то жеребьевка повторяется.")


def mode_game(): # Определяем игра происходит против бота или игрок с игроком
    while True:
        mode_game = input("Введите режим игры (1 - пользователь играет против Бота; 2 - пользователь играет против пользователя): ")
        if mode_game.isdigit() and (mode_game == '1' or mode_game == '2'):
            mode_game = int(mode_game)
            break
        print("Вы ввели что то не то!")
    
    if mode_game == 1:
        return 1
    return 2
    

def step_players(): # Определяем ходит ли игрок №1 первым
    player1 = randint(1, 6)
    player2 = randint(1, 6)
    if player1 > player2:
        print(f"Игроку №1 выпало число: {player1}. Игроку №2 выпало число: {player2}")
        return True
    elif player2 > player1: return False
    else: step_players()


def get_ai_step(candies, max_step):
    step = candies % (max_step + 1)
    return step
 
 
def get_human_step(candies, max_step):
    while True:
        step = input('Введите количество конфет: ')
        if step.isdigit() and 1 <= int(step) <= min(max_step, candies):
            return int(step)
        print('Введено некорректное значение!')

rules_game()
mod_game = mode_game()

name1 = input("Введите имя игрока №1: ")
name2 = ('Бот' if mod_game == 1 else input("Введите имя игрока №2: "))

while True:
    candies = input("Введите количество конфет в начале игры: ")
    if candies.isdigit() and int(candies) > 1:
        candies = int(candies)
        break
    else: print("Вы ввели что то не то!")

while True:
    max_step = input("Введите, какое максимальное количество конфет можно взять за ход: ")
    if max_step.isdigit() and int(max_step) > 1:
        max_step = int(max_step)
        break
    else: print("Вы ввели что то не то!")

human = step_players()
if human: print(f"Первым ходит {name1}")
else: print(f"Первым ходит {name2}")

while candies:
    if human:
        print(f"Ходит игрок {name1}")
        step = get_human_step(candies, max_step)
        candies -= step
        print(f'{name1} взял {step} конфет. Осталось {candies}.')
    else:
        print(f"Ходит игрок {name2}")
        if mod_game == 1:
            step =get_ai_step(candies, max_step)
        else:
            step = get_human_step(candies, max_step)
        candies -= step
        print(f'{name2} взял {step} конфет. Осталось {candies}.')
    human = not human
 
if human:
    print(f'Победил {name2}')
else:
    print(f'Победил {name1}')