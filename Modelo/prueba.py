############################################################################
def factorial(n):

    if n == 0 or n == 1:
        return 1
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))
############################################################################
def elevado(x, n):
    
    resultado = 1

    for _ in range(n):
        resultado *= x
    return resultado

print(elevado(2, 3))

############################################################################

def calcular_e_x(x, n):
    resultado = 1
    for i in range(1, n + 1):
        resultado += elevado(x, i) / factorial(i)
    return resultado

print(calcular_e_x(5, 100))

############################################################################

def sen(x, n):
    resultado = 0
    for i in range(n):
        resultado += elevado(-1, i) * elevado(x, 2*i + 1) / factorial(2 * i + 1)
    return resultado
print(sen(5, 100))

############################################################################

def cos(x, n):
    resultado = 0
    for i in range(n):
        resultado += elevado(-1, i) * elevado(x, 2 * i) / factorial(2 * i)
    return resultado

print(cos(5, 100))

############################################################################

def arcsen(x, n):
    resultado = 0
    for i in range(n):
        resultado += factorial(2 * i)* elevado(x, 2 * i + 1)/ (elevado(4, i) * elevado(factorial(i), 2) * (2 * i + 1))
    return resultado

print(arcsen(0.5, 10))

############################################################################
def arccos(x, n):
    
    resultado = 0
    pi = 3.141592653589793

    resultado += (pi/2) - arcsen(x, n) 
    return resultado

print(arccos(0.5, 10))
############################################################################

def senh(x, n):
    resultado = 0
    
    for i in range(n):
        resultado += elevado(x, 2*i + 1) /factorial(2*i + 1)
    return resultado
print(senh(5, 100))
############################################################################

def cosh(x, n):
    resultado = 0
    
    for i in range(n):
        resultado += elevado(x, 2 * i) / factorial(2 * i)
    return resultado
print(cosh(5, 100))
