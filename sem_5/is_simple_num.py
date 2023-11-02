def easy(n, divisor):
    
    if n % divisor == 0:
        return False
    if divisor*divisor > n:
        return True
    return easy(n, divisor + 1)

print (easy(11, 2))