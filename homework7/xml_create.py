NAME_FILE = "contact_book.xml"


def File_recording(data):
    xml = '<xml>\n'
    xml += '    <name units = "Имя">{}</name>\n'\
        .format(data["name"])
    xml += '    <surname units = "Фамилия">{}</surname>\n'\
        .format(data["surname"])
    xml += '    <phone units = "Телефон">{}</phone>\n'\
        .format(data["phone"])
    xml += '    <comment units = "Описание">{}</comment>\n'\
        .format(data["comment"])
    xml += '<xml>\n'

    with open(NAME_FILE, "a") as directory:
        directory.writelines(xml)

def File_reading():
    with open(NAME_FILE, "r") as directory:
        return directory.read()
