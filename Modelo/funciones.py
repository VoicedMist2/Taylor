# Calcula x elevado a la n veces
<<<<<<< HEAD
=======

>>>>>>> e00b0848eccfe300a19a3183ea82320362f9f771
def elevado(x, n):
    
    resultado = 1

    for _ in range(n):
        resultado *= x
    return resultado

# Calcula el factorial de n
<<<<<<< HEAD
=======

>>>>>>> e00b0848eccfe300a19a3183ea82320362f9f771
def factorial(n):   
      
    if n == 0 or n == 1:
        return 1
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    return resultado

<<<<<<< HEAD
=======
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

# Calcula arcsen x solo para x en el intervalo [-1, 1]

def arcsen(x, n):
    resultado = 0
    for i in range(n):
        resultado += factorial(2 * i)* elevado(x, 2 * i + 1)/ (elevado(4, i) * elevado(factorial(i), 2) * (2 * i + 1))
    return resultado

# Calcula arccos x solo para x en el intervalo [-1, 1]
def arccos(x, n):
    
    resultado = 0
    pi = 3.141592653589793

    resultado += (pi/2) - arcsen(x, n)
    return resultado

# Calcula senh x

def senh(x, n):
    resultado = 0
    
    for i in range(n):
        resultado += elevado(x, 2*i + 1) /factorial(2*i + 1)
    return resultado

# Calcula cosh x
def cosh(x, n):
    resultado = 0
    
    for i in range(n):
        resultado += elevado(x, 2 * i) / factorial(2 * i)
    return resultado
>>>>>>> e00b0848eccfe300a19a3183ea82320362f9f771
