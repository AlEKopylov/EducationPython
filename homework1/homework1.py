# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def CheckNumberOfWeek(N):
    if N < 8 and N > 0:
        if N == 6 or N == 7:
            print('да')
        else:
            print('нет')
    else:
        print('Неверный ввод')
    return


N = int(input('Введите число дня недели [1-7] -> '))
CheckNumberOfWeek(N)

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
lstX = [0, 1, 0, 1, 0, 1, 0, 1]
lstY = [0, 0, 1, 1, 0, 0, 1, 1]
lstZ = [0, 0, 0, 0, 1, 1, 1, 1]


def CheckPredicat(x, y, z):
    if (not (x or y or z)) == ((not x) and (not y) and (not z)):
        print(f'{z}, {y}, {x}: true')
    else:
        print(f'{z}, {y}, {x}: false')


for i in range(0, len(lstX)):
    CheckPredicat(lstX[i], lstY[i], lstZ[i])

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


def InputСoordinate(stroka):
    Num = int(input(f'{stroka} -> '))
    if Num == 0 and Num == int(Num):
        print('Неверный ввод')
        exit(0)
    return Num


def CheckQuadrant(x, y):
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
CheckQuadrant(x, y)
#4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти(x и y).


def InputNumber(stroka):
    Num = int(input(f'{stroka} -> '))
    if (Num < 1 or Num > 4) and Num == int(Num):
        print('Неверный ввод')
        exit(0)
    return Num


def OutputQuadrant(numberQuadrant):
    if numberQuadrant == 1:
        outputString = 'Первая четверть x > 0, y > 0'
    elif numberQuadrant == 2:
        outputString = 'Вторая четверть x < 0, y > 0'
    elif numberQuadrant == 3:
        outputString = 'Третья четверть x < 0, y < 0'
    elif numberQuadrant == 4:
        outputString = 'Четвертая четверть x > 0, y < 0'
    return print(outputString)


number = InputNumber('Введите номер квадранта оси координат [1..4]')
OutputQuadrant(number)

#5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def InputСoordinate(stroka):
    Num = int(input(f'{stroka} -> '))
    if Num == 0:
        print('Неверный ввод')
        exit(0)
    return Num


def CheckDistance(coordX1, coordY1, coordX2, coordY2):
    distance = ((coordX2 - coordX1) ** 2 + (coordY2 - coordY1) ** 2) ** 0.5
    return print('%.2f' % distance)


x1 = InputСoordinate('Введите координату Х1')
y1 = InputСoordinate('Введите координату Y1')
x2 = InputСoordinate('Введите координату Х2')
y2 = InputСoordinate('Введите координату Y2')
CheckDistance(x1, y1, x2, y2)
