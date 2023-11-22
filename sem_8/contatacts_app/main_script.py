'''
Задача №49.

Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.

1. Программа должна выводить данные

2. Программа должна сохранять данные в
текстовом файле

3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)

4. Использование функций. Ваша программа
не должна быть линейной
'''

import os

phonebook = dict()

phonebook['Boyle'] = {'phones': [1212121,5555555],'email': '777@mail.com', 'birthday': '10.10.1990'}

# Операции

def import_contacts():

    os.chdir(r"C:\Users\valeo\Documents\gb_python\sem_8\contatacts_app\import")
    cur_dir = os.curdir
    file_list = [file_path for file_path in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, file_path))]

    print('Доступные файлы для импорта: \n')
    
    for i in enumerate(file_list):
        print(*i)

    return

def edit_contact():

    name = (input('Введите имя для редактирования контакта: '))

    def edit_phone():

        n_phone = int(input(f'У контакта {name} Несколько телефонов. Введите порядковый номер для редактирования')) if len(phonebook[name]['phones']) > 1 else 1

        new_phone = int(input(f'Введите номер телефона {n_phone} для контакта {name}: '))

        phonebook[name]['phones'][n_phone - 1] = new_phone

        return
    
    def edit_email():
    
        new_email = input(f'Введите новый Email для контакта {name}:')

        phonebook[name]['email'] = new_email
    
        return
    
    def edit_birthdate():
    
        new_birthdate = input(f'Введите дату рождения для контакта {name}:')

        phonebook[name]['birthday'] = new_birthdate
    
        return
    
    edit_dict = {
                 'phone': edit_phone,
                 'email':edit_email,
                 'birthdate':edit_birthdate
                 }

    field = input('''
Выберите поле для редактирования:
                  
phone - Телефон (по умолчанию 1й в списке) 
email - Электронная почта
birthdate - Дата рождения
'''
                  )
    
    try:
        edit_dict[field]()

    except:
        print('Команда не найдена')

# Словарь операций

def main_cycle():

    app_active = True

    operations_dict = {
                #    'add': add_contact, 
                #    'del': del_contact, 
                #    'find': find_contact,
                #    'all': show_all, 
                   'edit': edit_contact,
                   'import': import_contacts,
                #    'export': export_contacts
                   }

    while app_active:

        print("""Доступные команды:
               
add - добавить контакт 
del - удалить контакт
find - поиск контакта
all - показать все контакты
close - закрыть приложение 
edit - изменить контакт
""")
        
        command = input('Введите комманду: ')

        if command == 'close':
            
            print('Закрытие приложения')
            
            break    
        
        try: 
            operations_dict[command]()
        
        except:
            print('Команда не найдена')

        

# структура контакта
'''
     {"дядя Ваня": {'phones': [1212121,5555555],
                           'email': '777@mail.com', 'birthday': '10.10.1990'},
            }
'''

main_cycle()

