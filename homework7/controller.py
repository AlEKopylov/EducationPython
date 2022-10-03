import view
import csv_create
import xml_create

def Select_process ():
    select = view.User_select()
    if select == 1:
        Import_process_csv(view.User_data_input())
    elif select == 2:
        Export_process_csv()
    elif select == 3:
        Import_process_xml(view.User_data_input())
    elif select == 4:
        Export_process_xml()

def Export_process_csv():
    view.view_result(csv_create.File_reading())

def Import_process_csv(data):
    csv_create.File_recording(data)

def Export_process_xml():
    view.view_result(xml_create.File_reading())

def Import_process_xml(data):
    xml_create.File_recording(data)