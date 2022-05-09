from clases.Persona import Persona

class Ciclista(Persona):
    def __int__(self):
        self.__equipo = None
        self.__pais = None
        self.__tiempoPrueba = None
        self.__ciclistas = None

    # Metodo Get (Obtener el valor de un atrubuto)
    @property
    def equipo(self):
        return self.__equipo
    
    @property
    def pais(self):
        return self.__pais

    @property
    def tiempoPrueba(self):
        return self.__tiempoPrueba

    @property
    def ciclistas(self):
        return self.__ciclistas

    # Metodo set (Lleva un valor a un atrubuto)
    @equipo.setter
    def equipo(self, equipo):
        self.__equipo = equipo
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @tiempoPrueba.setter
    def tiempoPrueba(self, tiempoPrueba):
        self.__tiempoPrueba = tiempoPrueba

    @ciclistas.setter
    def ciclistas(self, ciclistas):
        self.__ciclistas = ciclistas