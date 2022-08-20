#capturando un error de integer
try:
    import math
    import sys
    print("Se pudo importar el Modulo {}".format(sys.argv))
except ImportError as ie:
    print("No se pudo importar el Modulo {}".format(ie))


try:
    edad= int(input("Ingrese su edad: "))
except ValueError:
    print("Ingreso un dato invalido")
except ZeroDivisionError:
    print("Ocurre cuando se itenta dividir por cero")
except TypeError:
    print("Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado")
except OverflowError:
    print("Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.")
except IndexError:
    print("Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.")
except KeyError:
    print("Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.")
except FileNotFoundError:
    print("Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.")
except ImportError:
    print("Ocurre cuando falla la importación de un módulo.")
finally:
    print("El programa se finaliza. Saludos!")