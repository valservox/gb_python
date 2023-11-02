# надо найти сумму всех целых чисел от 1 до N, 
# где N вводит пользователь

def summa_cycle(num):
    res = 0
    while True:
        if num == 0:
            break
        res += num
        num -= 1
    return res

# summa_cycle(3) = 3 + 2 + 1 + 0

def summa_rec(num):
    if num == 0:
        return 0
    return num + summa_rec(num - 1)

# summa_rec(4) = (4 + (3 + (2 + (1 + 0)))) погружение
#всплытие  4 + (3 + (2 + 1)) = 4 + (3 + 3) = 4 + 6 = 10  


num = int(input("Введите натуральное число "))
print(f"Сумма всех натуральных чисел от 1 до {num} равна {summa_cycle(num)}")
print(summa_rec(num))