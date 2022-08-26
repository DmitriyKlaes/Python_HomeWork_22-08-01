from csv import DictReader as dr
from csv import DictWriter as dw
from input_rules import correct_value, default_value, deportaments, positions
from logger import log_fill, log_change_previos, log_change, log_delete

def static_headers():
    return ['Отдел', 'Должность', 'Фамилия', 'Имя', 'Телефон', 'Дата рождения', 'Примечание']


def list_workers():
    with open('base_workers.csv', 'r', encoding='utf8',  newline='') as file:
        headers = dr(file)
        workers_list = [dict_1 for dict_1 in headers]
        return workers_list
    

def fill_workers():
    with open('base_workers.csv', 'r+', encoding='utf8',  newline='') as file:
        headers = dr(file)
        writer = dw(file, fieldnames=headers.fieldnames)
        dep = deportaments()
        pos = positions(dep)
        part_1 = {headers.fieldnames[0]: dep, headers.fieldnames[1]: pos}
        part_2 = {field: default_value(input(f'{field}: ').capitalize()) for field in headers.fieldnames[2:]}
        next_row = {**part_1, **part_2}
        writer.writerow(next_row)
    log_fill(next_row)
    
    
def change_workers():
    list_data = list_workers()
    entry = correct_value('Выберете запись для изменения: ', len(list_data))
    log_change_previos(list_data[entry - 1])
    print()
    for position, value in enumerate(static_headers(), 1):
        print(position, ':', value)
    key = correct_value('\nВыберете поле записи для изменения: ', len(static_headers()))
    key = static_headers()[key - 1]
    temp_key = list_data[entry - 1][key]
    if key == 'Отдел':
        list_data[entry - 1][key] = deportaments()
        log_change(key, list_data[entry - 1][key])        
        if list_data[entry - 1][key] != temp_key:
            print('\nВ выбраннои отделе отсутствует должность ', end = '')
            print(list_data[entry - 1]['Должность'])
            list_data[entry - 1]['Должность'] = positions(list_data[entry - 1][key])
            log_change('Должность', list_data[entry - 1]['Должность'], 2)            
    elif key == 'Должность':
        list_data[entry - 1][key] = positions(list_data[entry - 1]['Отдел'])
        log_change(key, list_data[entry - 1][key])
    else:
        list_data[entry - 1][key] = input(f'Заполните поле "{key}": ').capitalize()
        log_change(key, list_data[entry - 1][key])
    with open('base_workers.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=static_headers())
        writer.writeheader()
        writer.writerows(list_data)
        

def del_workers():
    list_data = list_workers()
    entry = correct_value('Выберете запись для удаления: ', len(list_data))
    log_delete(list_data[entry - 1])
    list_data.pop(entry - 1)
    with open('base_workers.csv', 'w', encoding='utf8',  newline='') as file:
        writer = dw(file, fieldnames=static_headers())
        writer.writeheader()
        writer.writerows(list_data)
        

def print_workers():
    list_data = list_workers()
    if list_data == []:
        print('\nОтсутствуют записи о сотрудниках!')
        return
    print('\n---СПИСОК РАБОТНИКОВ ОАО "РОБОЗАВР"---')
    print(f'ID: ', end = '')
    print('; '.join(static_headers()))          
    for row in enumerate(list_data, 1):
        list_values = list(row[1].values())
        print(f'{row[0]}: ', end = '')
        print('; '.join(list_values))
