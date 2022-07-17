# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
N = int(input('Введите число дня недели [1-7] -> '))
def CheckNumberOfWeek(N):
    if  N < 8 and N > 0:
        if N == 6 or N == 7:
            print('да')
        else:
            print('нет')
    else:
        print('Неверный ввод')
    return 
CheckNumberOfWeek(N)
# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
def InputСoordinate(stroka):
    Num = int(input(f'{stroka} -> '))
    if Num == 0 and Num == int(Num):
        print('Неверный ввод')
        exit(0)
    return Num
def CheckQuadrant (x, y):
    if x > 0 and y > 0:
        n = 1
    elif x < 0 and y > 0:
        n = 2
    elif x < 0 and y < 0:
        n = 3
    elif x > 0 and y < 0:
        n = 4
    return print(f'{n}я четверть')
x = InputСoordinate('Введите координату Х')
y = InputСoordinate('Введите координату Y')
CheckQuadrant (x, y)