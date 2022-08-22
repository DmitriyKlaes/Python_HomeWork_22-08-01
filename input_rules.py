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