'''
Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.

Если значение характеристики для разных объектов
отличается - то False.

Для пустого набора объектов, функция
должна возвращать True. 

Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод
values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print(‘same’)

else:
    print(‘different’)

'''

def same_by(characteristic, objects):

    len_filtered = len(list(filter(characteristic, objects)))
    
    return len(objects) == len_filtered or len_filtered == 0

values = [0, 2, 10, 7]

# objects = [0, 2, 10, 7]
# objects_filtrd = [0, 2, 10]
# len(objects) = 4
# len(objects_filtrd) = 3

if same_by(lambda x: x % 2, values):
    print('same')

else:
    print('different')