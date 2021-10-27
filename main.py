
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
    
    
    pass
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                    totalAsientos +=1

        return totalAsientos

    def verificarIntegridad(self):
        mensaje = 'Auto original'

        if self.registro == self.motor.registro :
            for asiento in self.asientos:
                if type(asiento) == Asiento:
                    if asiento.registro != self.registro:
                        mensaje = 'Las piezas no son originales'
        else:
            mensaje = 'Las piezas no son originales'

        return mensaje




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