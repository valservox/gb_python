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

phonebook = dict()

# Операции

def edit_contact():

    def edit_phone(name,n_phone = 0):

        new_phone = int(input(f'Введите номер телефона {n_phone} для контакта {name}: '))

        phonebook[name]['phones'][n_phone] = new_phone

        return

    field = input('''
                  Выберите контакт:
                  
                  Телефон
                  Email
                  Дата рождения


                  '''
                  )



# Словарь операций
'''
operations_dict = {
                   'add': add_contact(), 
                   'del': del_contact(), 
                   'find': find_contact(),
                   'all': show_all(), 
                   'edit': edit_contact(),
                   'close': close_app(),
                   'import': import_contacts(),
                   'export': export_contacts()
                   }

'''
def main_cycle():
    while True:

        print("""Доступные команды:
               
              add - добавить контакт 
              del - удалить контакт
              find - поиск контакта 
              save - сохранение 
              all - показать все контакты
              close - закрыть приложение 
              edit - изменеть контакт
              """)
        
        command = input('Введите комманду: ')
'''
        try: 
            operations_dict[command]
        
        except:
            print('Команда не найдена')
'''
        

# структура контакта
'''
     {"дядя Ваня": {'phones': [1212121,5555555],
                           'email': '777@mail.com', 'birthday': '10.10.1990'},
            }
'''

