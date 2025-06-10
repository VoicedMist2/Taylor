# Calcula x elevado a la n veces
def elevado(x, n):
    
    resultado = 1

    for _ in range(n):
        resultado *= x
    return resultado

# Calcula el factorial de n
def factorial(n):   
      
    if n == 0 or n == 1:
        return 1
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado

