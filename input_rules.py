def correct_value(message, length = 2):
    value = input(message)
    while not value.isdigit() or not 0 < int(value) <= length:
        value = input(f'Неверный ввод. Введите соответствующий номер: ')
    return int(value)


def default_value(string):
    temp_string = string.replace(' ', '')
    if temp_string == '':
        return '(отсутствует)'
    else:
        return string


def dep_and_pos_list():
    return {'Директорат': ['Генеральный директор', 'Личный помощник'], 
            'Финансовый отдел': ['Бухгалтер', 'Помощник бухгалтера'], 
            'IT Отдел': ['Руководитель IT', 'Программист', 'Тестировщик'], 
            'Инженерный отдел': ['Главный инженер', 'Сброрщик'], 
            'Маркетинговый отдел': ['Маркетолог', 'Аналитик'], 
            'Отдел продаж': ['Руководитель отдела продаж', 'Менеджер']}


def deportaments():
    list_dep = list(dep_and_pos_list().keys())
    print(f'\nОтделы:')
    for id, dep in enumerate(dep_and_pos_list().keys(), 1):
        print(f'{id}: {dep}')    
    key = correct_value('\nВыберете отдел: ', len(list_dep))
    dep = list_dep[key-1]
    return dep


def positions(key):
    print(f'\nДолжности из отдела "{key}":')
    for id, pos in enumerate(dep_and_pos_list()[key], 1):
        print(f'{id}: {pos}')
    value = correct_value('\nВыберете должность: ', len(dep_and_pos_list()[key]))
    pos = dep_and_pos_list()[key][value-1]
    return pos

