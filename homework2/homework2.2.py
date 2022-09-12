''' 2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.'''


def factorial(num):
    factorialOut = 1
    while num > 1:
        factorialOut *= num
        num -= 1
    return factorialOut

def inputNumbers(text):
    number = int(input(f'{text}'))
    return number

number = inputNumbers('Введите число -> ')
result = [1]
for j in range(2, number + 1):
    result.append(factorial(j))
print(f'пусть N = {number}, тогда {result}')
