from Modelo import funciones
from Vista import vista

class Controlador_Series_Taylor:
        
    def iniciar():

        opcion = input("Selecciona una operacion: ")    

        x = vista.Vista_Series_Taylor.pedir_valor()

        acciones = {
            "1": ("e^x", funciones.Series_Taylor.calcular_e_x),
            "2": ("sen", funciones.Series_Taylor.sen),
            "3": ("cos", funciones.Series_Taylor.cos),
            "4": ("arcsen", funciones.Series_Taylor.arcsen),
            "5": ("arccos", funciones.Series_Taylor.arccos),
            "6": ("senh", funciones.Series_Taylor.senh),
            "7": ("cosh", funciones.Series_Taylor.cosh),
            }

        if opcion in acciones:
            nombre_funcion, funcion = acciones[opcion]
            resultado = funcion(x)
            vista.Vista_Series_Taylor.mostrar_resultado(nombre_funcion, x, resultado)
        else:
            print("Opción no válida")
