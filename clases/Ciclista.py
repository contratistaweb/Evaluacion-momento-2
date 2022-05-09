class Ciclista():
    def __int__(self):
        self.__nombre = None
        self.__edad = None
        self.__pais = None
        self.__tiempoPrueba = None

    # Metodo Get (Obtener el valor de un atrubuto)
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad

    @property
    def pais(self):
        return self.__pais

    @property
    def tiempoPrueba(self):
        return self.__tiempoPrueba

    

    # Metodo set (Lleva un valor a un atrubuto)
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @tiempoPrueba.setter
    def tiempoPrueba(self, tiempoPrueba):
        self.__tiempoPrueba = tiempoPrueba

    def print(self):
        print("nombre =", self.nombre)
        print("edad =", str(self.edad))
        print("pais =", self.pais)
        print("tiempoPrueba =", str(self.tiempoPrueba))