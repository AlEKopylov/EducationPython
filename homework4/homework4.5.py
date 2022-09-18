'''5.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.'''

def printIndex (stroka):
    indexST = []
    s = [int(s) for s in str.split(stroka) if s.isdigit()]
    for i in range(0, len(s)-1, 2):
        indexST.append(int(s[i]))
    return indexST

def summator(sp1, sp2):
    newSP = []
    if len(sp1) == len(sp2):
        for i in range(0, len(sp)):
            newSP.append(int(sp1[i]) + int(sp2[i]))
        return newSP
    else: 
        if len(sp1) > len (sp2):
            sp2.reverse()
            for i in range(len(sp2), len(sp1)):
                sp2.append('0')
            sp2.reverse()
        elif len(sp1) < len (sp2):
            sp1.reverse()
            for i in range(len(sp1), len(sp2)):
                sp1.append('0')
            sp1.reverse()
        return summator (sp1, sp2)
    
def printStroka (stroka):
    k = len(strokaNew) - 1
    resultFile = open("result.txt", "w")
    resultF = ''
    for i in range(0, k+1):
        if i == k:
            resultF = resultF + f"{strokaNew[i]} = 0"
            continue
        if strokaNew[i] != 0:
            resultF = resultF + f"{strokaNew[i]}x ** {k-i} + "
    resultFile.write (resultF)
    resultFile.close()
    return

def readStroka (nameFile):
    file = open(nameFile, 'rt')
    for temp in file:
        temp = temp.rstrip()
    return temp

stroka1 = readStroka('file1.txt')
stroka2 = readStroka('file2.txt')

sp = printIndex(stroka1)
sp2 = printIndex(stroka2)
strokaNew = summator(sp, sp2)
printStroka (strokaNew)