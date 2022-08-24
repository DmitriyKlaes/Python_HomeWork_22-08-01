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
    values = {'Директорат': ['Генеральный директор', 'Личный помощник'], 
              'Финансовый отдел': ['Бухгалтер', 'Помощник бухгалтера'], 
              'IT Отдел': ['Руководитель IT', 'Программист', 'Тестировщик'], 
              'Инженерный отдел': ['Главный инженер', 'Сброрщик'], 
              'Маркетинговый отдел': ['Маркетолог', 'Аналитик'], 
              'Отдел продаж': ['Руководитель отдела продаж', 'Менеджер']}
    for dep in enumerate(values.keys()):
        print(dep)
        # return string
        
dep_and_pos()