from csv import DictReader as dr
from csv import DictWriter as dw
from input_rules import correct_value, default_value, deportaments, positions, static_headers, dep_and_pos_list
from logger import log_fill, log_change_previos, log_change, log_delete


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
        print(f'{position}: {value}')
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

        
def data_search(list_data):
    list_fields = static_headers()
    list_pos = [value for pos in dep_and_pos_list().values() for value in pos]
    for id, field in enumerate(list_fields, 1):
        print(f'{id}: {field}')
    search_field = correct_value('По каким полям выполнить поиск: ', len(list_fields))
    if search_field == 1:
        dep = deportaments()
        for_search = (list_fields[search_field - 1], dep)
    elif search_field == 2:
        for id, pos in enumerate(list_pos, 1):
            print(f'{id}: {pos}')
        pos = correct_value('\nПо какой должности выполнить поиск: ', len(list_pos))
        for_search = (list_fields[search_field - 1], list_pos[pos - 1])
    else:
        value = input(f'Введите значение для поиска в поле "{list_fields[search_field - 1]}": ').capitalize()
        for_search = (list_fields[search_field - 1], value)
    return [entry for entry in list_data if for_search in entry.items()]
    

def data_field():
    dict_fields = {key: value for key, value in enumerate(static_headers(), 1)}
    dict_fields[len(dict_fields) + 1] = '---Закончить выбор---'
    length = len(dict_fields)
    list_for_print = []
    while True:
        for value in dict_fields.items():
            print(f'{value[0]}: {value[1]}')
        print('\nВыбранные поля: ', end = '')
        print(', '.join(list_for_print))
        index = correct_value('\nВыберете поле для отображения: ', length)
        print()
        if index == length or index not in dict_fields.keys():
            break
        list_for_print.append(dict_fields[index])
        dict_fields.pop(index)
    return [value for value in static_headers() if value in list_for_print]
    

def search_print(sort_fields, list_data):
    print(f'ID: ', end = '')
    print('; '.join(sort_fields))
    for row in enumerate(list_data, 1):
        row_for_print = {key: value for key, value in row[1].items() if key in sort_fields}
        list_values = list(row_for_print.values())
        print(f'{row[0]}: ', end = '')
        print('; '.join(list_values))
        

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

search_data = data_search(list_workers())
search_fields = data_field()
search_print(search_fields, search_data)


# print(data_search(list_data, list_fields))


# print(dep_and_pos_list())

# a = data_search()
# b = data_field()
# search_print(b,a)
# search_positions = data_search()
# list_data = list_workers()

# list_dict = [{1:11, 2:22}, {3:33, 4:44}]
# dict_1 = [(1, 11), (2, 22)]
# search_list = [entry for entry in list_dict if dict_1 in entry.items()]
# print(search_list)
# print(list_dict[0].items())

# a = {1:11, 2:22, 3:33, 4:44}
# b = (1,11)

# # print(b if b in a.items())
# for i in a.items():
#     if b == i:
#         print(i)


# print_workers()
# print(a)
# print(b)
# search_print()