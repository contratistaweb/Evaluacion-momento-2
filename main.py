import pprint
from clases.Ciclista import Ciclista
from clases.Cliente import Cliente


opcion = input('Seleccione una opcion:\nA) Programa de ciclistas.\nB) Programa de clientes.\nExit) Para salir.\n')
ciclistas = [];

while opcion!= 'exit':
    if opcion == 'A':
        ciclista = Ciclista()
        ciclista.nombre = input('nombre: ')
        ciclista.edad = int(input('edad: '))
        ciclista.pais = input('pais: ')
        ciclista.tiempoPrueba = int(input('tiempo de prueba: '))
        ciclistas.append(ciclista);
        opcion = input('\nSeleccione una opcion:\nA) Programa de ciclistas.\nB) Programa de clientes.\nExit) Para salir.\n')





    elif opcion=='B':
        print('clientes')
        opcion = input('\nSeleccione una opcion:\nA) Programa de ciclistas.\nB) Programa de clientes.\nExit) Para salir.\n')

    else:
        opcion = input('\nSeleccione una opcion:\nA) Programa de ciclistas.\nB) Programa de clientes.\nExit) Para salir.\n')

ganador = Ciclista()
ganador.tiempoPrueba = 9999999999

for ciclista in ciclistas:
    if ganador.tiempoPrueba > ciclista.tiempoPrueba:
        ganador.nombre = ciclista.nombre
        ganador.edad = ciclista.edad
        ganador.pais = ciclista.pais
        ganador.tiempoPrueba = ciclista.tiempoPrueba
        

print(ganador.nombre)
print(ganador.edad)
print(ganador.pais)
print(ganador.tiempoPrueba)
