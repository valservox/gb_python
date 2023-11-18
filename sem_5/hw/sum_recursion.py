def sum(first,second):
    
    if first == 0:
        return second
        
    return sum(first - 1, second + 1)

a = 3
b = 5

print(sum(a, b))