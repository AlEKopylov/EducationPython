'''2.	Измените код одной из решенных ранее задач (любой, с прошлых семинаров), применив лямбды, filter, map, zip, enumerate, списочные выражения.'''

'''Реализуйте алгоритм перемешивания списка.'''

'''Новый вариант'''
from random import random


list = [1, 2, 3, 4, 5]
res = sorted(list, key=lambda x: random())
print(res)

# cтарый вариант

# from random import randint


# def newIndex(leng):
#     indexNewLst = []
#     while len(indexNewLst) < leng:
#         randIndex = randint(0, leng-1)
#         if randIndex not in indexNewLst:
#             indexNewLst.append(randIndex)
#     print(f' Новые индексы: {indexNewLst}')
#     return indexNewLst


# def newShuffle(list):
#     print(f' Старый массив: {list}')
#     index = newIndex(len(list))
#     shuffleList = newList(list)
#     for i in range(0, len(list)):
#         shuffleList[i] = list[index[i]]
#     return print(f' Новый массив: {shuffleList}')


# def newList(list):
#     copyList = []
#     for j in list:
#         copyList.append(j)
#     return copyList


# list = [1, 2, 3, 4, 5]
# newShuffle(list)
