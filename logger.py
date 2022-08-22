from datetime import datetime as dt


def log_new(all_entry, headers):
    time = str(dt.now())
    with open('log.txt', 'a', encoding='utf8') as file:
        file.write(f'{time[:-7]} --СОЗДАН НОВЫЙ СПРАВОЧНИК-- Поля нового справочника: {headers}\n')
        file.write(f'\t\t\tСтарые данные:\n')
        for entry in all_entry:
            file.write(f'\t\t\t\t{entry}\n')


def log_fill(entry):
    time = str(dt.now())
    with open('log.txt', 'a', encoding='utf8') as file:
        file.write(f'{time[:-7]} --ДОБАВЛЕНИЕ-- Добавлена запись: {entry}\n')


def log_change_previos(entry):
    time = str(dt.now())
    with open('log.txt', 'a', encoding='utf8') as file:
        file.write(f'{time[:-7]} --ИЗМЕНЕНИЕ-- В записи {entry}\n\t\t\t\t\t\t\t\t\t')


def log_change(field, value):
    with open('log.txt', 'a', encoding='utf8') as file:
        file.write(f'изменено поле "{field}" на "{value}"\n')
        
        
def log_delete(entry):
    time = str(dt.now())
    with open('log.txt', 'a', encoding='utf8') as file:
        file.write(f'{time[:-7]} --УДАЛЕНИЕ-- Удалена запись: {entry}\n')
