from interface import start_menu, fill_interface, change_interface, delete_interface
from data import create_phonebook, print_phonebook
from input_rules import correct_value


dict_command = {1 : print_phonebook,     
                2 : fill_interface,
                3 : change_interface,
                4 : delete_interface,
                5 : create_phonebook}

print_type = 0

while True:
    command = start_menu()
    if print_type == 0 and command != 5 or command == 6:
        print_type = correct_value('\nВыберете формат вывода списка контактов: \
                                    \n1. Одна запись - одна строка \
                                    \n2. Каждая ячейка записи с новой строки \
                                    \nВыбор: ')
    if command == 1:
        dict_command[command](print_type)
        input('\nДля выхода в главное меню нажмите Enter...')
    elif command == 7:
        break
    elif command != 6:
        dict_command[command](print_type)
        