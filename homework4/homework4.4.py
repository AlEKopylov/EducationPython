'''4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.'''


from random import randint

k = int(input("введите степень: "))
for i in range(k+1):
    temp = randint(0, 100)
    if i == k:
        print(f"{temp} = 0")
        continue
    if temp != 0:
        print(f"{temp}x **{k-i} + ", end = ' ')