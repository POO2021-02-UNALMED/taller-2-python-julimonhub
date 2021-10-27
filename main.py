
class Asiento:


    pass
    def _init_(self,color, precio , registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        if color=='rojo' or color=='verde' or color=='amarillo' or color=='negro' or color=='blanco':
            self.color = color

class Auto:
    
    
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        n = 0
        for i in range (0,len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                n = n + 1
        return n
    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in range (0,len(self.asientos)):
                if type(self.asientos[i]) == Asiento and self.registro != self.asientos[i].registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"


class Motor:
   
    pass
    def _init_(self, numeroCilindros, tipo, registro):
        self.tipo = tipo
        self.numeroCilindros = numeroCilindros
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self, tipo):
        if tipo =="gasolina" or tipo == "electrico":
            self.tipo = tipo