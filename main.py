from clases.Ciclista import Ciclista
from clases.Cliente import Cliente

ciclista = Ciclista()
cliente = Cliente()
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
        print("Ejercicio Banco")
    elif(menuPrincipal != 0):
        print("Digite una opcion valida")

else:
    print("Hasta Pronto")