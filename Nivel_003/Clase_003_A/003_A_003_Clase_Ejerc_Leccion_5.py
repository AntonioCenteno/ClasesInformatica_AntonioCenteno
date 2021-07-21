print()
print('*********************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Leccion 2ª Archivo: 003_A_003_Clase_Ejerc_Leccion_5')
print('          Profesor: Antonio Centeno')
print('*********************************************************************************\n')
print('*********************************************************************************')
print('*********************************************************************************\n')
"""

# Ejercicio 1
def funcion():
    palabra = input("Escribe una palabra: ")
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", ]
    if palabra[0] in vocales:
        print("Empieza por la vocal", palabra[0])
    else:
        print("No empieza por vocal")


funcion()


# Ejercicio 2
def funcion():
    palabra = input("Escribe una palabra: ")
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", ]
    if len(palabra) > 7:
        print("Palabra demasiado larga")
        funcion_9()
    else:
        if palabra[0] in vocales:
            print("Empieza por la vocal", palabra[0])
        else:
            print("No empieza por vocal")


funcion()


# Ejercicio 3
def fun():
    lista1 = input("Introduce una lista de números")  # introduce 13579
    lista = []
    for item in lista1:
        lista.append(int(item))
    lista2 = input("introduce una lista de números segunda")  # introduce 2468
    for item in lista2:
        lista.append(int(item))
    lista = set(lista)
    lista = list(lista)
    print(lista)  # salida por pantalla [1, 2, 3, 4, 5, 6, 7, 8, 9]


fun()


# Ejercicio 4
def funcionexponente(exp):
    a = float(input("Teclea la base: "))
    n = a ** exp
    return print("El numero:", a, " elevado a:", exp, " es:", n)


funcionexponente(int(input("Teclea un numero para el exponent: ")))


# Ejercicio 5
def fun(exp):
    a = float(input("Teclea la base: "))
    n = a ** exp
    return n


def fun2(fun_5):
    division = fun_5 / 3
    return print(division)


fun2(fun(3))


# Ejercicio 6
def funcion1():
    p = input("Introduce una palabra o frase: ")
    return len(p)


funcion1()


def funcion2():
    p = globals()["funcion1"]()
    m = p * 5
    return print("Valor multiplicado por cinco: ", m)


funcion2()


# Ejercicio 7
def aceleracion_movimiento_circular():
    a = float((v ** 2) / r)
    return print(a)


v = float(input("Introduce la velocidad: "))
r = float(input("Introduce el radio: "))

aceleracion_movimiento_circular()


# Ejercicio 8
def funcion_8():
    return "Tu llamada a una función dentro de una función resulto ok"


def saludar(nombre, mensaje='hola'):
    print(mensaje, nombre)
    print(funcion_8())


saludar("Juan Antonio")


# Ejercicio 9
def funcion_9():
    return "Hola mundo"


def llamada_de_retorno(func=""):
    return globals()[func]()  # llamada de retorno a nivel global


print(llamada_de_retorno("funcion"))

nombredelafuncion = "funcion"
print(locals()[nombredelafuncion]())  # llamada de retorno a nivel local12	13	14

# Ejercicio 10 Apartado a

mitupla = (1, 2, 3)


def duplicar(x):
    print(x * 2)


duplicar(mitupla)

# Ejercicio 10 Apartado a Realizado de otra forma
mitupla = (1, 2, 3)


def duplicar(x):
    print(x + x)


duplicar(mitupla)

# Ejercicio 10 Apartado b
mitupla1 = (1, 2, 3)


def multiplicar():  # Se puede poner argumento en def "x"
    for _ in mitupla1:
        print(mitupla1)


multiplicar()

# Ejercicio 11 Multiplicamos por 3.14
mitupla = (1.25, 2.345, 3.456, 4.567, 5.678, 6.789, 7.456)


def multiplicar():
    for i in mitupla:
        m = round((i * 3.14), 4)
        print(m)


multiplicar()



# Ejercicio 12 Multiplicamos x 2


def operar(*h):
    for x in h:
        print("El resultado al x por 2, es:", int(x) * 2, end="\n")


operar(1, "2", 3)


# Ejercicio 13 Paso de argumento

def operar(*h, argumento="El resultado al x por 2, es:"):
    for x in h:
        print(argumento, int(x) * 2, end="\n")


operar(1, "2", 3)
"""


# Ejercicio 14

def palabras(a, b, c, *, s="fisica", p="Quimica"):
    listadepalabras = [a, b, c]
    for i in listadepalabras:
        print(i + s, end="\n")
    print(p + s)  # Este print crea la ultima suma


palabras("Astro", "Bio", "Nano")

# Ejercicio 15

midiccionario = {"Portugal": "Lisboa", "España": "Madrid", "Francia": "Paris", "Italia": "Roma"}


def capitales(**dicci15):
    for item in dicci15:
        print("País: ", item, ",", "Capital: ", dicci15[item])


capitales(**midiccionario)
