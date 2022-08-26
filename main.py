from interface import start_menu, fill_interface, change_interface, delete_interface
from data import print_workers


dict_command = {1 : print_workers,     
                2 : fill_interface,
                3 : change_interface,
                4 : delete_interface,
                5 : print('netu')}

while True:
    command = start_menu()
    if command == 1:
        dict_command[command]()
        input('\nДля выхода в главное меню нажмите Enter...')
    elif command == 6:
        break
    elif command != 6:
        dict_command[command]()

