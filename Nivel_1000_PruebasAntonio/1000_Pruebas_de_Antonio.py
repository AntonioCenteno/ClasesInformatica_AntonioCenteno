"""print('hola campeon')
diccionario = {'clave1': 25, 'clave': 123}
print (diccionario['clave1'])
print (diccionario ["clave"])
diccionario1 = {'nombre': 'Pedro', 'edad': 45, 'cursos': ["Frances", 'Alemán', 'Chino']}

print (diccionario1['nombre']) # accedemos al nombre de Pedro
print (diccionario1 ['cursos'])# accedemos a los nombre de los cursos
print (diccionario1 ['cursos'][0])# accedemos de los nombre de los cursos al de frances
for key in diccionario1: # me va creando una lectura de todo el diccionario
    print (key, ":", diccionario1[key])
diccionario1["creaNuevaClave"]= 'nuevo valor' # crea una nueva clave y un nuevo valor
print (diccionario1) # imprime todo el diccionario
print("nombre" in diccionario1)# nos dice si tenemos la clave nombre en el diccionario. True
print('nombre'in diccionario1) # nos dice si tenemos la clave nombre en el diccionario. True
print(type (diccionario1)) # nos indica si corresponde diccionario a un tipo de dato.  adaf
"""

"""# SEMAFORO CON VERDE, ROJO, AMBAR
semaforo = str(input('teclea verde, rojo o ambar: '))
if semaforo == "verde":
    print('Cruza la calle')
elif semaforo == "ambar":
    print('Espera un poco')
elif semaforo == "rojo":
    print('Espera al color verde')
else:
    print('No has tecleado bien')


# SEMAFORO CON VERDE, ROJO, AMBAR Y CON EQUIVOCACION DE USUARIO
semaforo = str(input('teclea verde, rojo o ambar: '))
if semaforo == "verde":
    print('Cruza la calle')
elif semaforo == "ambar":
    print('Espera un poco')
else:
    print('Espera al color verde')




#ESCRIBE LAS TABLAS DE VERDAD CON RECORRIDO BOOLEANO
booleanos = [False, True]

# Tabla de verdad de or

print('x\ty\tx or y')
print('-' * 22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y, sep='\t')

print()

# Tabla de verdad de and

print('x\ty\tx and y')
print('-' * 22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y, sep='\t')

print()

# Tabla de verdad de not

print('x\tnot x')
print('-' * 13)
for x in booleanos:
    print(x, not x, sep='\t')

print()

# Tabla de verdad de ^

print('x\ty\tx ^ y')
print('-' * 21)
for x in booleanos:
    for y in booleanos:
        print(x, y, x ^ y, sep='\t')
"""

# UTILIZACION DE OPERADORES LOGICOS

x = int(input('teclea un numero para x: '))
y = int(input('teclea un numero para y: '))
solucion = ((3*x)>(10-y) and ((20+4)!= 10-(y**2)))
print (solucion)

"""
#TEORIA DE GRAFOS
# Autor: Luis García

# Carrera: Ingeniería en Computación


import os

grafo = {}

opc = 0

while opc != 3:

    os.system("cls")

    print("\n\tGrafo Ponderado no Dirigido")

    opc = input("\n1.-Ingresar nodos \n2.-Mostrar grafo \n3.-Salir \nElige una opcion-> ")

    opc = int(opc)

    if opc == 1:

        print("\nINGRESE LOS NODOS Y SU PESO \n")

        origen = input("Ingresa el origen:  ")

        destino = input("Ingresa el destino: ")

        peso = input("Ingresa el peso:    ")

        peso = int(peso)

        ###VERIFICA QUE NO ESTE REPETIDO EL VERTICE ORIGEN Y DESTINO INGRESADO

        repetido = False

        for orig, lista in grafo.items():

            for destin, pesos in grafo[orig]:

                if orig == origen and destin == destino and pesos == peso:
                    print("\nEL VERTICE YA EXISTE\n")

                    repetido = True

        # SI NO ESTÁ REPETIDO INGRESA A VALIDAR SI LOS NODOS ORIGEN Y DESTINO EXISTEN

        if repetido == False:

            if origen in grafo:

                if destino in grafo:

                    lista = grafo[origen]

                    grafo[origen] = lista + [(destino, peso)]

                    lista = grafo[destino]

                    lista.append((origen, peso))

                    grafo[destino] = lista

                else:

                    grafo[destino] = [(origen, peso)]

                    lista = grafo[origen]

                    lista.append((destino, peso))

                    grafo[origen] = lista

            elif destino in grafo:

                grafo[origen] = [(destino, peso)]

                lista = grafo[destino]

                lista.append((origen, peso))

                grafo[destino] = lista

            else:

                grafo[destino] = [(origen, peso)]

                grafo[origen] = [(destino, peso)]

    if opc == 2:

        print()

        # SI EL GRAFO TIENE NODOS LO MUESTRA

        if len(grafo) > 0:

            for key, lista in grafo.items():
                print(key)

                print(lista)

        else:

            print("El grafo esta vacio...")

    print()

    os.system("pause")"""
# averiguar si un numero es par o impar
x = int(input('escribe un numero'))
if x % 2 == 0:
    print ("x es par")
else:
    print ("x es impar")

print("Para trabajar con git hub, primero hago el commit y luego lo subo con push")

"""esto es un comentario de linea multilinea
cuando yo quiera escribir asi lo tenemos.
Para ello les vale y les sobra es lo que hay"""