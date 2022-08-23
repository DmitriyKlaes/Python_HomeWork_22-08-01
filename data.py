from csv import DictReader as dr
from csv import DictWriter as dw
from input_rules import correct_value, default_value
from logger import log_new, log_fill, log_change_previos, log_change, log_delete

def static_headers():
    return ['Отдел', 'Должность', 'Фамилия', 'Имя', 'Телефон', 'Дата рождения', 'Примечание']


def list_workers():
    with open('base_workers.csv', 'r', encoding='utf8',  newline='') as file:
        headers = dr(file)
        workers_list = [dict_1 for dict_1 in headers]
        return workers_list
    

def fill_phonebook():
    with open('base_workers.csv', 'r+', encoding='utf8',  newline='') as file:
        headers = dr(file)
        writer = dw(file, fieldnames=headers.fieldnames)
        next_row = {}
        next_row = {field: default_value(input(f'{field}: ').title()) for field in headers.fieldnames}
        writer.writerow(next_row)
    log_fill(next_row)
    
    
def change_workers(list_data):
    entry = correct_value('Выберете запись для изменения: ', len(list_data))
    log_change_previos(list_data[entry - 1])
    for position, value in enumerate(static_headers(), 1):
        print(position, ':', value)
    key = correct_value('Выберете поле записи для изменения: ', len(list_data[int(entry)-1]))
    key = static_headers()[key - 1]
    list_data[entry - 1][key] = input(f'Заполните поле "{key}": ').title()
    log_change(key, list_data[entry - 1][key])
    with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=static_headers())
        writer.writeheader()
        writer.writerows(list_data)
        

def del_phonebook(list_data):
    entry = correct_value('Выберете запись для удаления: ', len(list_data))
    list_keys = list(list_data[entry - 1].keys())
    log_delete(list_data[entry - 1])
    list_data.pop(entry - 1)
    with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=list_keys)
        writer.writeheader()
        writer.writerows(list_data)