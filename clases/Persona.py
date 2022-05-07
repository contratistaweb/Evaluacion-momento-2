class Persona:
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__cedula = None
        self.__edad = None

    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def apellido(self):
        return(self.__apellido)

    @property
    def cedula(self):
        return(self.__cedula)

    @property
    def edad(self):
        return(self.__edad)

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @edad.setter
    def edad(self, edad):
        self.__edad = edad