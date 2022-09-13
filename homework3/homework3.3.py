'''3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.'''

def updateList (list):
    newList = []
    for i in list:
        newList.append(i % 1)
    return newList

sp = [1.1, 1.2, 3.1, 5, 10.01]
sp = updateList(sp)

print(max(sp) - min(sp))