'''
Факториал
'''

# a = int(input('Input a: '))

# res = 1
# counter = 1

# while counter <= a:

#     res *= counter
#     counter += 1


# print(f'{a}! = {res}')

'''
Фибоначи
'''

# A = int(input("Введите натуральное число A: "))

# first, second = 0, 1  # Первые два числа Фибоначчи
# current = 1 
# n = 1

# while current < A:

#     current = first + second
#     # first, second = second, first + second
#     second = first
#     first = current
#     n += 1

# ans = n if current == A else -1
# '''
# if ans == -1 and current - first < second - current:

#     ans = first

# elif ans == -1 and current - first > second - current:

#     ans = second

# elif ans == -1 and current - first == second - current:

#     ans = (first,second)
# '''
# print(ans)


'''
# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
'''

# n_melons = int(input('Кол-во арбузов: '))

# n = 1

# while n <= n_melons:

#     curr_w = int(input(f'Вес арбуза {n}: '))

#     if n <= 1:

#         min_w = curr_w
#         max_w = curr_w

#     min_w = curr_w if curr_w < min_w else min_w
#     max_w = curr_w if curr_w > max_w else max_w

#     n += 1

# print((min_w,max_w))

'''
# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
'''

from random import randint
days_num = int(input('Введите количество дней: '))

warm_days, max_warm_days = 0, 0
for i in range(days_num):
    temp = int(input(f'Температура дня {i+1}: '))
    print(temp, end=' ')
    if temp > 0:
        warm_days += 1
    else:
        if warm_days > max_warm_days:
            max_warm_days = warm_days
        print(f'mwd: {max_warm_days}')
        warm_days = 0
if warm_days > max_warm_days:
    max_warm_days = warm_days
    print(f'mwd: {max_warm_days}')
print()
print(f'Самая длинная оттепель длилась {max_warm_days} дня/дней')