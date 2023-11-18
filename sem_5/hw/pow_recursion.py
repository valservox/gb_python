def f(a, b):

    if b == 1:
        return a 
    
    return f(a, b - 1) * a

a = 2
b = 3
print(f(a, b))