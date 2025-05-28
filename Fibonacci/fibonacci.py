def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("no definido para numeros negativos")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("no definido para numeros negativos")
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)