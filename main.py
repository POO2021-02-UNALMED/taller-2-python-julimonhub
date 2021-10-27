class Asiento:
    pass
    def __init__(color, precio , registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(color):
        if color=='rojo' or color=='verde' or color=='amarillo' or color=='negro' or color=='blanco':

class Auto:
    pass
    def __init__(modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        TotalAsientos = 0
        for asiento in asientos:
            if type(asiento) == Asiento:
                    TotalAsientos +=1

        return TotalAsientos

    def verificarIntegridad(Asiento):
        mensaje = 'Auto original'

        if registro == motor.registro :
            for asiento in asientos:
                if type(asiento) == Asiento:
                    if asiento.registro != registro:
                        mensaje = 'Las piezas no son originales'
        else:
            mensaje = 'Las piezas no son originales'

        return mensaje
class Motor:
      def __init__(numCilindros,tipo,registro):
        self.numCilindros = numCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(numero):
        self.registro = numero
    def asignarTipo(tipo):
        Permitidos = ["electrico","gasolina"]
        if tipo in Permitidos:
            self.tipo = tipo 