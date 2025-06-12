class Vista_Series_Taylor:

    def mostrar_menu():
        print("____SERIES DE TAYLOR____")
        print("1. e^x")
        print("2. sen(x)")
        print("3. cos(x)")
        print("4. arcsen(x)")
        print("5. arccos(x)")
        print("6. senh(x)")
        print("7. cosh(x)")
        print("0. Salir")

    def pedir_valor():
        x = float(input("Ingresa el valor de x: "))
        return x

    def mostrar_resultado(funcion, valor_ingresado, resultado):
        print(funcion + "(" + valor_ingresado + ") = "+ resultado)

Vista_Series_Taylor.mostrar_menu()
Vista_Series_Taylor.pedir_valor()
Vista_Series_Taylor.mostrar_resultado("e^x", "5", "148.41")