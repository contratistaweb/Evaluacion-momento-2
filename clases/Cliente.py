from clases.Persona import Persona

class Cliente(Persona):
    def __init__(self):
        self.__ciudad = None
        self.__saldo = None

    @property
    def ciudad(self):
        return(self.__ciudad)

    @property
    def saldo(self):
        return(self.__saldo)

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def mostrarSaldo(self):
        print(self.saldo)