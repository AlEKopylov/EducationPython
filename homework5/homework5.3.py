'''3.	Создайте программу для игры в "Крестики-нолики".'''


formatka = [['11', '12', '13'], 
            ['21', '22', '23'],
            ['31', '32', '33']]
print ('Подсказка формата выбора ячейки.')
for i in formatka:
    print(*i)
print ()
arr = [['*', '*', '*'], 
       ['*', '*', '*'],
       ['*', '*', '*']]
for i in arr:
    print(*i)
a = False
while a == False:
    a1, b1 = int(input('игрок Х: строка-> ')), int(input('игрок Х: столбец-> '))
    arr[a1-1][b1-1] = 'x'
    for i in arr:
        print(*i)
    if (arr[0][0] == arr[0][1] == arr[0][2] == 'x' or arr[1][0] == arr[1][1] == arr[1][2] == 'x' or arr[2][0] == arr[2][1] == arr[2][2] == 'x'
         or arr[0][0] == arr[1][0] == arr[2][0] == 'x' or arr[0][1] == arr[1][1] == arr[2][1] == 'x' or arr[0][2] == arr[1][2] == arr[2][2] == 'x'
         or arr[0][0] == arr[1][1] == arr[2][2] == 'x' or arr[2][0] == arr[1][1] == arr[2][0] == 'x'):
         a = True
         print('Выиграл 1 игрок!')
         break
    a2, b2 = int(input('игрок 0: строка-> ')), int(input('игрок 0: столбец -> '))
    arr[a2-1][b2-1] = '0'
    for i in arr:
        print(*i)
    if (arr[0][0] == arr[0][1] == arr[0][2] == '0' or arr[1][0] == arr[1][1] == arr[1][2] == '0' or arr[2][0] == arr[2][1] == arr[2][2] == '0'
         or arr[0][0] == arr[1][0] == arr[2][0] == '0' or arr[0][1] == arr[1][1] == arr[2][1] == '0' or arr[0][2] == arr[1][2] == arr[2][2] == '0'
         or arr[0][0] == arr[1][1] == arr[2][2] == '0' or arr[2][0] == arr[1][1] == arr[2][0] == '0'):
         a = True
         print('Выиграл 2 игрок!')
         break
