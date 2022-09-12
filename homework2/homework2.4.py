'''4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях. 
 Позиции хранятся в файле file.txt в одной строке одно число.'''


def inputNumbers(text, leng):
    number = int(input(f'{text}'))
    if leng >= number >= 0:
        return number
    else:
        print("Выход за пределы списка")
        quit()


lst = [int(input('Введите элемент списка: '))
       for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {lst}')
number1 = inputNumbers('Введите позицию первого элемента - > ', len(lst))
number2 = inputNumbers('Введите позицию второго элемента - > ', len(lst))
print(f'Произведение элементов списка: {lst[number1] * lst[number2]}')
