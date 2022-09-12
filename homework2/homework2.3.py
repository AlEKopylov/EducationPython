'''3.	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.'''


def inputNumbers(text):
    number = int(input(f'{text}'))
    return number


def progressionSumma(num):
    list = []
    i = 1
    summa = 0
    while i <= num:
        progressNumber = (1 + (1/i)) ** i
        list.append('%.3f' % progressNumber)
        summa += progressNumber
        i += 1
    print(list)
    print('%.3f' % summa)
    return


number = inputNumbers('Введите число -> ')
progressionSumma(number)
