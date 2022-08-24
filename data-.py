from csv import DictReader as dr
from csv import DictWriter as dw
from input_rules import correct_value, default_value
from logger import log_new, log_fill, log_change_previos, log_change, log_delete

            
def list_phonebook():
    with open('base_workers.csv', 'r', encoding='utf8',  newline='') as file:
        headers = dr(file)
        phonebook_list = [dict_1 for dict_1 in headers]
        return phonebook_list
    
        
def change_headers(headers):
    action = correct_value('\nВыберете действие: \
                            \n1. Добавить поле \
                            \n2. Удалить поле \
                            \nВыбор: ')
    print()
    print(', '.join(headers))
    length = len(headers) + 1
    if action == 2:
        length = len(headers)    
    position = correct_value(f'Введите номер позиции от 1 до {length}: ', length)
    if action == 1:
        headers.insert(position - 1, (input('Введите название поля: ').title()))
    elif action == 5:
        headers.append(input('Введите название поля: ').title())
    else:
        headers.pop(position - 1)
    print(f'\nРезультат:')
    print(', '.join(headers))
    complite = correct_value('\nСохранить изменения? \
                              \n1. Да \
                              \n2. Вернуть стандартные \
                              \n3. Изменить текущие \
                              \nВыбор: ', 3)
    return complite
        
        
def create_phonebook(nothing):
    warning = correct_value('\n!!!ВНИМАНИЕ!!! ТЕКУЩИЙ СПРАВОЧНИК БУДЕТ ПОЛНОСТЬЮ УДАЛЕН. ВЫ СОГЛАСНЫ? \
                             \n1. Да \
                             \n2. Нет \
                             \nВыбор: ')   
    if warning == 1:
        headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']    
        print('\nСтандартные поля для заполнения:')
        print(', '.join(headers))
        choice = correct_value('\nЖелаете их изменить? \
                                \n1. Да \
                                \n2. Нет \
                                \nВыбор: ')
        if choice == 1:
            complite = change_headers(headers)
            while complite == 3:
                complite = change_headers(headers)
            if complite == 2:
                headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']
        print('\nСоздан телефонный справочник с полями: ')
        print(', '.join(headers))
        log_new(list_phonebook(), headers)
        with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
            writer = dw(file, fieldnames=headers)
            writer.writeheader()
    else:
        return 


def fill_phonebook(filling_type):
    with open('phonebook.csv', 'r+', encoding='utf8',  newline='') as file:
        headers = dr(file)
        writer = dw(file, fieldnames=headers.fieldnames)
        next_row = {}
        if filling_type == 1:
            print('Введите значения в формате:')
            print('; '.join(headers.fieldnames))
            temp_row = input('Новая запись: ').split(';')
            next_row = dict([(field, default_value(value.title()))for field, value in zip(headers.fieldnames, temp_row)])       
        else:
            next_row = {field: default_value(input(f'{field}: ').title()) for field in headers.fieldnames}
        writer.writerow(next_row)
    log_fill(next_row)
        
        
def change_phonebook(list_data):
    entry = correct_value('Выберете запись для изменения: ', len(list_data))
    log_change_previos(list_data[entry - 1])
    list_keys = list(list_data[entry - 1].keys())
    for position, value in enumerate(list_keys, 1):
        print(position, ':', value)
    key = correct_value('Выберете поле записи для изменения: ', len(list_data[int(entry)-1]))
    key = list_keys[key - 1]
    list_data[entry - 1][key] = input(f'Заполните поле "{key}": ').title()
    log_change(key, list_data[entry - 1][key])
    with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=list_keys)
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
        

def print_phonebook(print_type):
    list_data = list_phonebook()
    if list_data == []:
        print('\nСправочник не заполнен!')
        return
    print('\n---ТЕЛЕФОННЫЙ СПРАВОЧНИК---')
    if print_type == 1:
        print(f'ID: ', end = '')
        print('; '.join(list(list_data[0].keys())))          
        for row in enumerate(list_data, 1):
            list_values = list(row[1].values())
            print(f'{row[0]}: ', end = '')
            print('; '.join(list_values))
    else:
        for row in enumerate(list_data, 1):
            print(f'{row[0]}. ')
            for key, value in row[1].items():
                print(key, ':', value)
            print()
            
            
def create_phonebook(): 
    headers = ['Отдел', 'Должность', 'Фамилия', 'Имя', 'Телефон', 'Дата рождения', 'Примечание']    
    print('\nСтандартные поля для заполнения:')
    print(', '.join(headers))
    choice = correct_value('\nЖелаете их изменить? \
                            \n1. Да \
                            \n2. Нет \
                            \nВыбор: ')
    if choice == 1:
        complite = change_headers(headers)
        while complite == 3:
            complite = change_headers(headers)
        if complite == 2:
            headers = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    print('\nСоздан телефонный справочник с полями: ')
    print(', '.join(headers))
    log_new(list_phonebook(), headers)
    with open('base_workers.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=headers)
        writer.writeheader()

