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


def dep_and_pos():
    all_values = {'Директорат': ['Генеральный директор', 'Личный помощник'], 
                  'Финансовый отдел': ['Бухгалтер', 'Помощник бухгалтера'], 
                  'IT Отдел': ['Руководитель IT', 'Программист', 'Тестировщик'], 
                  'Инженерный отдел': ['Главный инженер', 'Сброрщик'], 
                  'Маркетинговый отдел': ['Маркетолог', 'Аналитик'], 
                  'Отдел продаж': ['Руководитель отдела продаж', 'Менеджер']}
    list_dep = list(all_values.keys())
    print(list_dep)
    for id, dep in enumerate(list_dep, 1):
        print(f'{id}: {dep}')
    key = correct_value('Выберете отдел: ', len(list_dep))
    dep = list_dep[key-1]
    for id, pos in enumerate(all_values[list_dep[key-1]], 1):
        print(f'{id}: {pos}')
    value = correct_value('Выберете должность: ', len(all_values[list_dep[key-1]]))
    pos = all_values[list_dep[value-1]]
    return dep, pos

