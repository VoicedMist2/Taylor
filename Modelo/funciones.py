class Series_Taylor:

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
            resultado += Series_Taylor.elevado(x, i) / Series_Taylor.factorial(i)
        return resultado

    # Calcula sen x

    def sen(x, n):
        resultado = 0
        for i in range(n):
            resultado += Series_Taylor.elevado(-1, i) * Series_Taylor.elevado(x, 2*i + 1) / Series_Taylor.factorial(2*i + 1)
        return resultado

    # Calcula cos x

    def cos(x, n):
        resultado = 0
        for i in range(n):
            resultado += Series_Taylor.elevado(-1, i) * Series_Taylor.elevado(x, 2 * i) / Series_Taylor.factorial(2 * i)
        return resultado

    # Calcula arcsen x solo para x en el intervalo [-1, 1]

    def arcsen(x, n):
        resultado = 0
        for i in range(n):
            resultado += Series_Taylor.factorial(2 * i)* Series_Taylor.elevado(x, 2 * i + 1)/ (Series_Taylor.elevado(4, i) * Series_Taylor.elevado(Series_Taylor.factorial(i), 2) * (2 * i + 1))
        return resultado

    # Calcula arccos x solo para x en el intervalo [-1, 1]
    def arccos(x, n):
        
        resultado = 0
        pi = 3.141592653589793

        resultado += (pi/2) - Series_Taylor.arcsen(x, n)
        return resultado

    # Calcula senh x

    def senh(x, n):
        resultado = 0
        
        for i in range(n):
            resultado += Series_Taylor.elevado(x, 2*i + 1) / Series_Taylor.factorial(2*i + 1)
        return resultado


    # Calcula cosh x
    def cosh(x, n):
        resultado = 0
        
        for i in range(n):
            resultado += Series_Taylor.elevado(x, 2 * i) / Series_Taylor.factorial(2 * i)
        return resultado


