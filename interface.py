from data import list_workers, fill_workers, change_workers, del_workers, print_workers, \
                 data_search, data_field, search_print
from input_rules import correct_value


def start_menu():
    print('\n---Главное меню---')
    menu_position = correct_value('1. Просмотр списка сотрудников \
                                 \n2. Добавление нового сотрудника \
                                 \n3. Изменение записей о сотрудниках \
                                 \n4. Удаление записи о сотруднике \
                                 \n5. Поиск и сортировка \
                                 \n6. Закончить работу \
                                 \nВведите команду: ', 6)
    return menu_position


def fill_interface():
    print('\n---Добавление нового сотрудника---')
    flag = 1
    while flag:
        fill_workers()
        print_workers()
        move = correct_value('\n1. Добавить еще одного сотрудника \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()        
        if move == 2:
            flag = 0
            
            
def change_interface():
    if list_workers() == []:
        print('\nОтсутствуют записи о сотрудниках!')
        input('\nДля выхода в главное меню нажмите Enter...')
        return
    print('\n---Изменение записей о сотрудниках---')
    print_workers()
    print()
    flag = 1
    while flag:
        change_workers()
        print_workers()
        move = correct_value('\n1. Изменить еще одну запись \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()
        if move == 2:
            flag = 0
            
            
def delete_interface():
    if list_workers() == []:
        print('\nОтсутствуют записи о сотрудниках!')
        input('\nДля выхода в главное меню нажмите Enter...')
        return
    print('\n---Удаление записей---')
    print_workers()
    print()
    flag = 1
    while flag:
        del_workers()
        print_workers()
        if list_workers() == []:
            input('\nДля выхода в главное меню нажмите Enter...')
            return
        move = correct_value('\n1. Удалить еще одну запись \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()
        if move == 2:
            flag = 0
            
            
def search_interface():
    if list_workers() == []:
        print('\nОтсутствуют записи о сотрудниках!')
        input('\nДля выхода в главное меню нажмите Enter...')
        return
    print('\n---Режим поиска---')
    list_data = list_workers()
    all_searching_rules = []
    while True:
        list_data, search_rules = data_search(list_data)
        if list_data == []:
            print('\nНичего не найдено.')
            input('\nДля выхода в главное меню нажмите Enter...')
            return
        all_searching_rules.append(search_rules)
        move = correct_value('\n1. Добавить ещё один критерий \
                              \n2. Продолжить \
                              \nВыбор: ')
        if move == 2:
            break
    sort_fields = data_field()
    search_print(list_data, sort_fields, all_searching_rules)
    input('\nДля выхода в главное меню нажмите Enter...')
    return
