class FabricaVehiculo():
    marca= ""
    modelo=""
    precio=0
    version_motor=""
    velocidad=0
    max_speed=0

    def __init__(self, in_marca, in_modelo, in_precio, in_version_motor, in_max_speed):
        self.marca= in_marca
        self.modelo= in_modelo
        self.precio= in_precio
        self.version_motor= in_version_motor
        self.max_speed= in_max_speed
    
    def acelerar(self):
        if self.max_speed >= self.velocidad + 10:
            self.velocidad +=10
            print("El vehiculo aumenta su velocidad en 10Km/h")
        else:
            print("El vehiculo está alcanzando su maxima velocidad y no es posible seguir acelerando")
            self.velocidad = self.max_speed
        
    
    def frenar(self):
        if self.velocidad >= 10:
            self.velocidad -=10
            print("El vehiculo disminuye su velocidad en 10Km/h")
        else:
            print("El vehiculo se está deteniendo.")
            self.velocidad=0
    
    def doblar(self, direccion):
        print("El vehiculo dobla con direccion hacia la {}".format(direccion))

    def displayDatos(self):
        print("Los datos del vehiculo son:\n\tMarca: {0}\n\tModelo: {1}\n\tPrecio: {2}\n\tModelo de Motor: {3}\n\tMaxima Velocidad: {4}\n\tVelocidad Actual: {5}".format(self.marca,self.modelo,self.precio,self.version_motor,self.max_speed, self.velocidad))

    def CompararVehiculo(self, vehiculo):
        if self.max_speed >= vehiculo.max_speed:
            print("El vehiculo actual es mas rapido que el segundo.")
        else:
            print("El segundo vehiculo es mas rapido que el actual.")
    
vehiculo1= FabricaVehiculo("Alfa Romeo", "AR500", 80000, "Version 2.1", 310)
vehiculo2= FabricaVehiculo("Lamborguinhi", "Murcielago", 120000, "Version 1.9", 325)
vehiculo3= FabricaVehiculo("Peugeot", "208 Like Pack", 10000, "Version 1.6", 190)
vehiculo4= FabricaVehiculo("Ford", "Focus", 12000, "Version 1.8", 210)

vehiculo1.displayDatos()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.acelerar()
vehiculo1.displayDatos()

vehiculo3.CompararVehiculo(vehiculo4)