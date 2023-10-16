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

a = int(input('Input N: '))
array = [0, 1]

while a > array[-1]:
    
    array.append(array[-1] +  array[-2])

if a == array[-1]:
    
    print(len(array))

elif a - array[-2] < array[-1] - a:

    print(array[-2])

elif a - array[-2] == array[-1] - a:

    print((array[-2]),array[-1])

else:

    print(array[-1])