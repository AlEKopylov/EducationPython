'''2.	Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
import os
from random import randint


def inputPlayer(numberPlayer):
    player = int(input(f'Ход {numberPlayer} игрока -> '))
    if player not in range(1, 29):
        print('Неверный ввод! Введите число от 1 до 28!')
        player = inputPlayer(numberPlayer)
    return player


def bot(candy):
    botCandy = candy % 29
    return botCandy


print('Выберите режим игры:\n 1 - PvP\n 2 - PvE')
mode = int(input('Режим номер -> '))
os.system('cls')
# PvP
if mode == 1:
    candy = int(input('Введите количество конфет -> '))
    numberPlayer = 1
    while candy > 0:
        player = inputPlayer(numberPlayer)
        candy -= player
        if candy > 0:
            print(f'Осталось {candy} конфет.')
            if numberPlayer == 1:
                numberPlayer = 2
            else:
                numberPlayer = 1
    print(f'Победил игрок номер {numberPlayer}')

# PvE
if mode == 2:
    candy = int(input('Введите количество конфет -> '))
    numberPlayer = 1
    while candy > 0:
        if numberPlayer == 1:
            player = inputPlayer(numberPlayer)
            candy -= player
            if candy > 0:
                print(f'Осталось {candy} конфет.')
                numberPlayer = 2
        else:
            botStep = bot(candy)
            candy -= botStep
            if candy > 0:
                print(f'Бот взял {botStep}')
                print(f'Осталось {candy} конфет.')
                numberPlayer = 1
    if numberPlayer == 1:
        print(f'Победил игрок')
    else:
        print(f'Победил бот')
