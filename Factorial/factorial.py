def factorial_iterative(n):
    if n<0:
        raise ValueError("factorial no definido para numeros negativos")
    
    result = 1
    for i in range(1, n+1):
        result *= i

def factorial_recursive(n):
    if n < 0:
        raise ValueError("factorial no definido para numeros negativos")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)