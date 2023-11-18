sp = [1,2,3,4,5,6,7]

calculator = {  
                "+": lambda x,y: x+y,
                "-": lambda x,y: x-y,
                "/": lambda x,y: x/y,
                "*": lambda x,y: x*y
             }
x, op, y = input("Введите арифметическое выражение ").split()

print(f"Результат равен {calculator[op] (int(x), int(y)) }")