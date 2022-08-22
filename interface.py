from data import list_phonebook, fill_phonebook, change_phonebook, del_phonebook, print_phonebook
from input_rules import correct_value


def start_menu():
    print('\n---Главное меню---')
    menu_position = correct_value('1. Просмотр справочника \
                                 \n2. Добавление записей в справочник \
                                 \n3. Изменение записей в справочнике \
                                 \n4. Удаление записей из справочника \
                                 \n5. Создать новый справочник \
                                 \n6. Изменить тип вывода записей \
                                 \n7. Закончить работу \
                                 \nВведите команду: ', 7)
    return menu_position


def fill_interface(print_type):
    print('\n---Добавление записей---')
    filling_type = correct_value('\nВыберете тип заполнения: \
                                  \n1. Всё в одну строку \
                                  \n2. С новой строки \
                                  \nВыбор: ')
    print()
    flag = 1
    while flag:
        fill_phonebook(filling_type)
        print_phonebook(print_type)
        move = correct_value('\n1. Добавить еще одну запись \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()
        if move == 2:
            flag = 0
            
            
def change_interface(print_type):
    if list_phonebook() == []:
        print('\nСправочник не заполнен!')
        input('\nДля выхода в главное меню нажмите Enter...')
        return
    print('\n---Изменение записей---')
    print_phonebook(print_type)
    print()
    flag = 1
    while flag:
        change_phonebook(list_phonebook())
        print_phonebook(print_type)
        move = correct_value('\n1. Изменить еще одну запись \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()
        if move == 2:
            flag = 0
            
            
def delete_interface(print_type):
    if list_phonebook() == []:
        print('\nСправочник не заполнен!')
        input('\nДля выхода в главное меню нажмите Enter...')
        return
    print('\n---Удаление записей---')
    print_phonebook(print_type)
    print()
    flag = 1
    while flag:
        del_phonebook(list_phonebook())
        print_phonebook(print_type)
        if list_phonebook() == []:
            input('\nДля выхода в главное меню нажмите Enter...')
            return
        move = correct_value('\n1. Удалить еще одну запись \
                              \n2. Вернуться в главное меню \
                              \nВыбор: ')
        print()
        if move == 2:
            flag = 0
