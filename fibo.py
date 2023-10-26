def fib(n): 
    
    if n in [1, 2]:
        return 1
    
    first = fib(n - 1)
    second = fib(n - 2)
    
    return first + second

list_1 = [] 

for i in range(1, 10):
    list_1.append(fib(i))
    
print(list_1)# [1, 1, 2, 3, 5, 8, 13, 21, 34]