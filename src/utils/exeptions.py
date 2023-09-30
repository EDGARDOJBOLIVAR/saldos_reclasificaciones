class ParameterException(Exception):
    def __init__(self, mensaje="Ocurrió un error de parametos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)