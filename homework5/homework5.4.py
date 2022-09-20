'''4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''

def coder (lst):
    count = 1
    res = ''
    for i in range(0, len(lst)-1):
        if lst[i+1] == lst[i]:
            count += 1
        else:
            res = res + str(count) + lst[i]
            count = 1
        if i == len(lst)-2:
            res = res + str(count) + lst[i+1]
    return res

def decoder(lst):
    res = ''
    numberChar = ''
    for i in range(0, len(lst)):
        if not lst[i].isdigit():
            char = lst[i]
            number = int(numberChar)
            res = res + number*char
            numberChar = ''
        elif lst[i].isdigit():
            numberChar = numberChar + lst[i]
    return res

def readStroka (nameFile):
    file = open(nameFile, 'rt')
    line = file.readline()
    return line

def printStroka (stroka, namefile):
    resultFile = open(namefile, "w")
    resultFile.write (stroka)
    resultFile.close()
    return

text = readStroka('inputText.txt')
print(f'Входящий текст -> {text}')
textRLE = coder(text)
printStroka (textRLE, 'TextRLE')
print(f'Текст после кодировки -> {textRLE}')
textDeRLE = decoder(textRLE)
printStroka (textRLE, 'TextDeRLE')
print(f'Текст после дешифровки -> {textDeRLE}')




