############################################################################
def factorial(n):

    if n == 0 or n == 1:
        return 1
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado

############################################################################
def elevado(x, n):
    
    resultado = 1

    for _ in range(n):
        resultado *= x
    return resultado

############################################################################

def calcular_e_x(x, n):
    resultado = 1
    for i in range(1, n + 1):
        resultado += elevado(x, i) / factorial(i)
    return resultado

print(factorial(5))
print(elevado(2, 3))
print(calcular_e_x(5, 100))

############################################################################
