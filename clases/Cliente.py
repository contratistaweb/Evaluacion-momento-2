from clases.Persona import Persona

class Cliente(Persona):
    def __init__(self):
        self.__ciudad = None
        self.__cuenta = None
        self.__saldo = None
        self.__listaClientes = None

    @property
    def ciudad(self):
        return(self.__ciudad)
    
    @property
    def cuenta(self):
        return(self.__cuenta)

    @property
    def saldo(self):
        return(self.__saldo)
    
    @property
    def listaClientes(self):
        return(self.__listaClientes)

    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad
    
    @cuenta.setter
    def cuenta(self, cuenta):
        self.__cuenta = cuenta

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @listaClientes.setter
    def listaClientes(self, listaClientes):
        self.__listaClientes = listaClientes

    def mostrarSaldo(self):
        print(self.saldo)