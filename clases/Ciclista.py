from clases.Persona import Persona

class Ciclista(Persona):
    def __int__(self):
        self.__equipo = None
        self.__tiempoPrueba = None

    # Metodo Get (Obtener el valor de un atrubuto)
    @property
    def equipo(self):
        return self.__equipo

    @property
    def tiempoPrueba(self):
        return self.__tiempoPrueba

    # Metodo set (Lleva un valor a un atrubuto)
    @equipo.setter
    def equipo(self, equipo):
        self.__equipo = equipo

    @tiempoPrueba.setter
    def tiempoPrueba(self, tiempoPrueba):
        self.__tiempoPrueba = tiempoPrueba