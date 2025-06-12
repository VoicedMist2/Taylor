def factorial(n):

    if n == 0 or n == 1:
        return 1
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
        print(f"Factorial de {i} es {resultado}")
    return resultado

n = 5
print(factorial(n))