'''1.	Напишите программу, удаляющую из текста все слова, содержащие "абв". '''

text = "Текст для проверки абв работыабв програбвммы"

lst = list(filter(lambda x: 'абв' not in x, text.split()))
print(*lst)