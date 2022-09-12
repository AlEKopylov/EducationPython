'''5.	Реализуйте алгоритм перемешивания списка.'''


from random import randint


def newIndex(leng):
    indexNewLst = []
    while len(indexNewLst) < leng:
        randIndex = randint(0, leng-1)
        if randIndex not in indexNewLst:
            indexNewLst.append(randIndex)
    print(f' Новые индексы: {indexNewLst}')
    return indexNewLst


def newShuffle(list):
    print(f' Старый массив: {list}')
    index = newIndex(len(list))
    shuffleList = newList(list)
    for i in range(0, len(list)):
        shuffleList[i] = list[index[i]]
    return print(f' Новый массив: {shuffleList}')


def newList(list):
    copyList = []
    for j in list:
        copyList.append(j)
    return copyList


list = [1, 2, 3, 4, 5]
newShuffle(list)
