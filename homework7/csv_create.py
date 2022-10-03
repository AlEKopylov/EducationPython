
NAME_FILE = "contact_book.csv"

def File_recording(data):
    with open(NAME_FILE, "a") as directory:
        text = data["name"] + ";" + data["surname"] +\
                ";" + data["phone"] + ";" + data["comment"] + "\n"
        directory.writelines(text)

def File_reading():
    lst = []
    with open(NAME_FILE, "r") as directory:
        for line in directory.read().split():
            lst.append(line.split(";"))
            return lst