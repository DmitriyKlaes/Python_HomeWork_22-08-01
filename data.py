from csv import DictReader as dr
from csv import DictWriter as dw
from input_rules import correct_value, default_value


def create_phonebook(nothing):
    warning = correct_value('\n!!!ВНИМАНИЕ!!! ТЕКУЩИЙ СПРАВОЧНИК БУДЕТ ПОЛНОСТЬЮ УДАЛЕН. ВЫ СОГЛАСНЫ? \
                             \n1. Да \
                             \n2. Нет \
                             \nВыбор: ')   
    if warning == 1:
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
        with open('phonebook.csv', 'w', encoding='utf8',  newline='') as file:
            writer = dw(file, fieldnames=headers)
            writer.writeheader()
    else:
        return