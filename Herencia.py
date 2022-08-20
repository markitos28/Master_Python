class Auto():
    def __init__(self, in_rueda, in_motor, in_carroceria):
        self.rueda = in_rueda
        self.motor = in_motor
        self.carroceria = in_carroceria
    
    def displayAtributos(self):
        print("El atributo rueda es de tipo: {}".format(type(self.rueda)))
        print("El atributo motor es de tipo: {}".format(type(self.motor)))
        print("El atributo carroceria es de tipo: {}".format(type(self.carroceria)))

class Rueda():
    def __init__(self, in_marca, in_modelo, in_rodado):
        self.marca= in_marca
        self.modelo= in_modelo
        self.rodado= in_rodado


class Motor():
    def __init__(self, in_marca, in_modelo, in_potencia):
        self.marca= in_marca
        self.modelo= in_modelo
        self.potencia= in_potencia

    def mejorarPotencia(self, mejora):
        if mejora == "Turbo":
            self.potencia = self.potencia + " + 50HP(Turbo)"
        elif mejora == "Caño de Escape":
            self.potencia = self.potencia + " + 10HP(Caño de Escape)"
        elif mejora == "Nitro":
            self.potencia = self.potencia + " + 120HP(Nitro)"
        else:
            pass


class Carroceria():
    def __init__(self, in_marca, in_modelo, in_dimension, in_color):
        self.marca= in_marca
        self.modelo= in_modelo
        self.dimension= in_dimension
        self.color= in_color


obj_rueda= Rueda("Bridgestone","E150", "R17")
obj_motor= Motor("Ford", "Focus", "100HP")
obj_carroceria= Carroceria("Ford", "Focus", "210cm x 80cm x 120cm", "Blanco")
creamos_auto= Auto(obj_rueda, obj_motor, obj_carroceria)

print("El color del auto creado es {}".format(creamos_auto.carroceria.color))
print("La potencia del auto creado es {}".format(creamos_auto.motor.potencia))
print("Las dimensiones del auto creado es {}".format(creamos_auto.carroceria.dimension))
print("La marca del motor del auto creado es {}".format(creamos_auto.motor.modelo))
# vamos a mejorar nuestro auto
creamos_auto.motor.mejorarPotencia("Turbo")

print("La potencia del auto MEJORADO es: {}".format(creamos_auto.motor.potencia))