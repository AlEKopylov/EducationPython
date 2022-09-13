'''5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.'''
k = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n):
        fibo_nums.append(a)
        a, b = b, a + b
    return fibo_nums
    
fibo1 = get_fibonacci(k)
fibo2 = list(reversed(fibo1))
for i in range(len(fibo2)):
    if k % 2 ==0:
        if i % 2 == 0: 
            fibo2[i] *= -1
    else:
        if i % 2 != 0: 
            fibo2[i] *= -1
fibo2.append(0)              
print(f'для k = {k} список будет выглядеть так:', fibo2 + fibo1)