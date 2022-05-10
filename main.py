import pprint
from clases.Ciclista import Ciclista
from clases.Cliente import Cliente

ciclista = Ciclista()
cliente = Cliente()
banco = Cliente()
banco.listaClientes=([])
ciclista.ciclistas = ([])
tiemposCrono = []
mejorCrono = None
menuPrincipal = 1
menuCiclista = 1

############################################################################

while(menuPrincipal != 0):
    print(".............................")
    print("...... Menu Principal .......")
    print(".............................")
    print("1 Para Ejercicio Crono")
    print("2 Para Ejercicio Banco")
    print("0 Para Salir") 
    menuPrincipal = int(input("Digite una opcion del menu principal: "))

    if(menuPrincipal == 1):
        print(".........................")
        print("...... Menu Crono .......")
        print(".........................")
        print("1 Para Ingresar Ciclista")
        print("0 Para Salir") 

        while(menuCiclista != 0):
            menuCiclista = int(input("Digite una opcion: "))

            if(menuCiclista == 1):
                opcion = 1

                while(opcion != 0):
                    ciclista.nombre = input("Nombre: ")
                    ciclista.edad = int(input("Edad: "))
                    ciclista.pais = input("Pais: ")
                    ciclista.equipo = input("Equipo: ")
                    ciclista.tiempoPrueba = int(input("Tiempo en minutos: "))

                    ciclista.ciclistas.append([ciclista.nombre, ciclista.edad, ciclista.pais, ciclista.equipo, ciclista.tiempoPrueba])
                    print("...................")
                    print("1 Para Ingresar Nuevo Registro")
                    print("0 Para Salir") 
                    opcion = int(input("Seleccione una opcion: "))
                    menuCiclista = opcion
                    print("...................")
                

            elif(menuCiclista != 0):
                print("Digite una opcion valida")

        else:
            print("Hasta Pronto")

        for i in range(0, len(ciclista.ciclistas)):
            tiemposCrono.append(ciclista.ciclistas[i][4])

        menorCrono = min(tiemposCrono)
        indexMejorCrono = tiemposCrono.index(menorCrono)

        print("El ciclista con el mejor crono de la prueba fue: ")
        print("Nombre: ", ciclista.ciclistas[indexMejorCrono][0])
        print("Edad: ", ciclista.ciclistas[indexMejorCrono][1])
        print("Pais: ", ciclista.ciclistas[indexMejorCrono][2])
        print("Equipo: ", ciclista.ciclistas[indexMejorCrono][3])
        print("Tiempo: ", ciclista.ciclistas[indexMejorCrono][4], "Minutos")
        print("...................")
        

    elif(menuPrincipal == 2):
        print(".........................")
        print("...... Menu Banco .......")
        print(".........................")
        print("1 Para Ingresar Un Cliente")
        print("2 Para Consultar Un Cliente")
        print("3 Para Consignar dinero a la Cuenta un Cliente")
        print("4 Para Retirar dinero de la Cuenta un Cliente")
        print("0 Para Salir") 
        menuBanco = int(input("Digite una opcion: "))
        
        while(menuBanco != 0):

            if menuBanco == 1:
                cliente.nombre = input("Nombre: ")
                cliente.apellido = input("Apellido: ")
                cliente.cedula = int(input("Cedula: "))
                cliente.cuenta = int(input("cuenta: "))
                cliente.saldo = int(input("saldo: "))
                banco.listaClientes.append([cliente.nombre,cliente.apellido,cliente.cedula,cliente.cuenta,cliente.saldo])
                print(banco.listaClientes)
                print(".........................")
                print("*** Registro Guardado ***")
                print(".........................")
                

            elif menuBanco == 2:
                cedula = int(input("Digite la cedula del cliente: "))
                for i in range(0, len(banco.listaClientes)):
                    if banco.listaClientes[i][2] == cedula:
                        print(banco.listaClientes[i])
            
            elif menuBanco == 3:

                cedula = int(input("Digite la cedula del cliente: "))
                valorConsignacion = int(input("Valor a consignar: "))

                for i in range(0, len(banco.listaClientes)):
                    if banco.listaClientes[i][2] == cedula:
                        banco.listaClientes[i][4] = banco.listaClientes[i][4] + valorConsignacion
                        print(f'nuevo saldo: {banco.listaClientes[i][4]}')

            elif menuBanco == 4:

                cedula = int(input("Digite la cedula del cliente: "))
                valorConsignacion = int(input("Valor a retirar: "))

                for i in range(0, len(banco.listaClientes)):
                    if banco.listaClientes[i][2] == cedula:
                        banco.listaClientes[i][4] = banco.listaClientes[i][4] - valorConsignacion
                        print(f'nuevo saldo: {banco.listaClientes[i][4]}')

            else:
                print("Digite una opcion valida")
            
            print(".........................")
            print("...... Menu Banco .......")
            print(".........................")
            print("1 Para Ingresar Un Cliente")
            print("2 Para Consultar Un Cliente")
            print("3 Para Consignar dinero a la Cuenta un Cliente")
            print("4 Para Retirar dinero de la Cuenta un Cliente")
            print("0 Para Salir")
            menuBanco = int(input("Digite una opcion: "))
            


    elif(menuPrincipal != 0):
        print("Digite una opcion valida")
    else:
        print("Hasta Pronto")
