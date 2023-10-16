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

ans = n if current == A else -1
'''
if ans == -1 and current - first < second - current:

    ans = first

elif ans == -1 and current - first > second - current:

    ans = second

elif ans == -1 and current - first == second - current:

    ans = (first,second)
'''
print(ans)


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

n_melons = int(input('Кол-во арбузов: '))

n = 1

while n <= n_melons:

    curr_w = int(input(f'Вес арбуза {n}: '))

    if n <= 1:

        min_w = curr_w
        max_w = curr_w

    min_w = curr_w if curr_w < min_w else min_w
    max_w = curr_w if curr_w > max_w else max_w

    n += 1

print((min_w,max_w)) 