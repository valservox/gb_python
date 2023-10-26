def factorial():

    if input('Запустить вычисление факториала? y/n: ') == 'n': return 

    a = int(input('Input a: '))

    res = 1
    counter = 1

    while counter <= a:

        res *= counter
        counter += 1

    print(f'{a}! = {res}')

def fibonacci():

    if input('Запустить поиск чисел Фибоначчи? y/n: ') == 'n': return 
    
    A = int(input("Введите натуральное число A: "))

    first, second = 0, 1  # Первые два числа Фибоначчи
    current = 1 
    n = 1

    while current < A:

        current = first + second
        # first, second = second, first + second
        second = first
        first = current
        n += 1

    if current == A: 
    
        print(n)
        return

    if A - second == first - A:

        print((-1,(first,second)))
        return
    
    if A - second < first - A:
        
        print((-1,second))
        return

    if A - second > first - A:
        
        print((-1,first))
        return

def melons():

    if input('Запустить решение задачи 15? y/n: ') == 'n': return 

    print(
'''
Задача №15.
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
''')

    n_melons = int(input('Кол-во арбузов: '))

    curr_w = int(input(f'Вес арбуза 1: '))

    min_w = curr_w
    max_w = curr_w

    for i in range(1,n_melons):

        curr_w = int(input(f'Вес арбуза {i+1}: '))

        min_w = curr_w if curr_w < min_w else min_w
        max_w = curr_w if curr_w > max_w else max_w

    print((min_w,max_w))

def weather():

    if input('Запустить решение задачи 13? y/n: ') == 'n': return 

    print(
'''
Задача №13
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
''')
        
    from random import randint

    days_num = int(input('Введите количество дней: '))

    warm_days, max_warm_days = 0, 0

    for i in range(days_num):

        temp = randint(-2,10)
        print(temp, end=' ')
        
        if temp > 0:
            warm_days += 1
        
        else:
        
            if warm_days > max_warm_days:
                max_warm_days = warm_days
        
            warm_days = 0
    
    if warm_days > max_warm_days:
        max_warm_days = warm_days
    
    print()
    print(f'Самая длинная оттепель длилась {max_warm_days} дня/дней')

# factorial()
# fibonacci()
# weather()
# melons()