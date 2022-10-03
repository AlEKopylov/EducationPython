def User_select():
    user_menu = ("Импорт в CSV", "Экспорт из CSV",
                 "Импорт в XML", "Экспорт из XML")
    for i in enumerate(user_menu, 1):
        print(i[0], i[1])
    while True:
        try:
            number = int(input("Введите № пункта: "))
            if 1 <= number <= 4:
                return number
            else:
                raise ValueError
        except ValueError:
            print ("Введите число от 1 до 4: ")

def User_data_input():
    name = input ("Введите имя: ")
    surname = input ("Введите фамилию: ")
    phone = input ("Введите номер телефона: ")
    comment = input ("Введите описание: ")
    directory_input = {
        "name": name,
        "surname": surname,
        "phone": phone,
        "comment": comment
    }
    return directory_input

def view_result(data):
    print(data)