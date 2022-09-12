""" 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """
def inputNumbers(text):
    number = float(input(f'{text}'))
    return number

def sumNumbers(numbers):
    sum = 0
    for i in str(numbers):
        if i != ".":
            sum += int(i)
    return sum

number= inputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNumbers(number)}")