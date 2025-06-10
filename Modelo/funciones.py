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

#Calcula e ** x

def calcular_e_x(x, n):
    resultado = 1
    for i in range(1, n + 1):
        resultado += elevado(x, i) / factorial(i)
    return resultado

# Calcula sen x

def sen(x, n):
    resultado = 0
    for i in range(n):
        resultado += elevado(-1, i) * elevado(x, 2*i + 1) / factorial(2*i + 1)
    return resultado

# Calcula cos x

def cos(x, n):
    resultado = 0
    for i in range(n):
        resultado += elevado(-1, i) * elevado(x, 2 * i) / factorial(2 * i)
    return resultado
