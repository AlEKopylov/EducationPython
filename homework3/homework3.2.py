'''2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''


def checkListRange(spisok):
    if len(sp) % 2 == 0:
        return len(sp)//2
    else:
        return len(sp)//2 + 1


sp = input().split()
result = []
j = len(sp)-1
for i in range(0, checkListRange(sp)):
    if i != j:
        result.append(int(sp[i]) * int(sp[j]))
        j -= 1
    else:
        result.append(int(sp[i]) ** 2)
print(result)
