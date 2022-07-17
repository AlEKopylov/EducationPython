# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def sum_of_number(number: any):
    sum = 0
    num = str(number).replace(".", "")
    for index in num:
        sum += int(index)
    return sum
number = input("Введите вещественное число -> ")
print(f'{number} ->', sum_of_number(number))
# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def factorial(n):
    i = 1
    factor = 1
    while i <= n:
        factor *= i
        i += 1
        print(factor, end=" ")
n = int(input('Введите целое число: '))
factorial(n)