import random
import math

# Ejercicio 1 Variables Globales y Locales

q, r, t = 2, 4, 6  # estas variables son globales


def area_de_rectangulo():
    base1 = 10  # estas variables son locales
    altura1 = 15
    area_1 = base1 * altura1
    print("El area de este rectángulo es: ", area_1, end="")
    return


print("La suma de q más r es: ", q + r)
print("La multiplicación de q por r por t es: ", q * r * t)
area_de_rectangulo()  # llamamos a la función
print("\n")


# Ejercicio 2 Funcines utiles

def sumatoria(x1, y1):
    print("La suma de los numeros es:", x1 + y1)


sumatoria(2, 4)
sumatoria(3, 5)


# Ejercicio 3 Peticion de argumentos al usuario

def media(x_1, y, z):  # función que suma tres números
    media_total = (x_1 + y + z) / 3
    print("la media es: ", media_total)


a = int(input("Teclea el primer valor: "))
b = int(input("Teclea el segundo valor: "))
c = int(input("Teclea el tercer valor: "))

media(a, b, c)
print("Al imprimir esta línea es señal que se ha terminado todo")


# Ejercicio 4 Omisión de argumentos por definición en parámetros. (fecha="12/12/1936)


def identificacion(nombre, apellido, fecha="12/12/2031"):
    print("El nombre completo es: ", nombre + " " + apellido + " " + fecha)


a = str(input("Teclea tu nombre: "))
b = str(input("Teclea tu apellido: "))
identificacion(a, b)
print("Cuando sale esta linea termina todo")


# Ejercicio 4-bis El mismo ejercicio sin el paso por omisión


def identificacion(nombre, apellido, fecha):
    print("El nombre completo es: ", nombre + " " + apellido + " " + fecha)


a = str(input("Teclea tu nombre: "))
b = str(input("Teclea tu apellido: "))
c = str(input("Teclea tu fecha de nacimiento con formato dd/mes/año: "))
identificacion(a, b, c)
print("Cuando sale esta línea termina todo")


# Ejercicio 5 Palabras clave "keywords" como argumentos.

def saludar(nombre, mensaje="hola amigos"):
    print(nombre, mensaje)


saludar(nombre="Así es como hace mi perro. No mi gato:", mensaje="Guau, guau ")
print("Cuando sale esta línea termina todo")


# Ejercicio 6 Parámetros fijos y parámetros arbitrarios

def recorrer_parametos(parametrofijo, *arbitrario):
    print(parametrofijo)
    for argumento in arbitrario:  # recorre los parámetros uno a uno
        print("\t", argumento)


recorrer_parametos("mi parámetro fijo: El perro", "primer parámetro arbitrario", "segundo parámetro arbitrario",
                   "tercer parámetro arbitrario")
print("Cuando sale esta línea termina todo")


# Ejercicio 7 Parámetros que son fijos y parámetros arbitrarios con clave y valor.

def parak1(parmetrofijo, *arbitrario, **claves_valor):
    print(parmetrofijo)  # toma el parámetro fijo
    for argumento in arbitrario:  # toma los parámetros arbitrarios
        print("\t", argumento)
    for clave in claves_valor:  # toma los parámetros clave valor
        print("Con este bucle recorremos la : ", clave, " y el ", claves_valor[clave])


parak1("el perro", "guau-1", "guau-2", "guau-3", ClavePrimera="oro", ClaveSegunda="platino")
print("Cuando sale esta línea termina todo")


# Múltiples retornos del return.

def sumas_multiples(a_1, b_1):
    print("Veamos las múltiples salidas de la instrucción return")
    print("Sacamos el valor: a1 =", a_1),
    print("Sacamos el valor: b1 =", b_1),
    print("Sacamos el valor: a1+b1 = ", a_1 + b_1),
    print("Sacamos el valor: a1*b1 =", a_1 * b_1),
    print("Sacamos el valor: a1-b1 =", a_1 - b_1),
    print("Sacamos el valor: a1/b1 =", a_1 / b_1)
    return  # podemos cambiar el (;) de la línea 5 por (,) y seguirá funcionando.


a1 = int(input("Teclea un número:"))
b1 = int(input("Teclea un número:"))
sumas_multiples(a1, b1)

# Determinar de una lista de números, cuantos empiezan por uno

mi_lista_numeros = ["1", "15", "256", "879", "89", "159", "111", "89",
                    "1", "15", "256", "879", "89", "159", "111", "89"]


def conocedor(aaa):
    cantidad = 0
    clave = "1"
    for item in aaa:
        if clave in item:
            cantidad = cantidad + 1
    print("La cantidad de numeros que empiezan por 1 de esta lista son:")
    print("[1,15,256,879,89,159,111,89] y cantidad: ", cantidad)

    return cantidad


conocedor(mi_lista_numeros)


# Lista de números aleatorios
# import random Lo tenemos arriba


def lista_aleatorios(z):
    lista = [0] * z
    for i in range(z):
        lista[i] = round(random.random(), 3)
    return lista


print("Ingrese cuantos numeros aleatorios desea obtener")
n = int(input())

aleatorios = lista_aleatorios(n)
print("Los numeros son: ", aleatorios)

# Lista de números aleatorios entre 0 y 1000
# import random Lo tenemos arriba

print("Ingrese cuantos números aleatorios desea obtener")
n = int(input())
aleatorios = [random.randint(0, 1000) for _ in range(n)]
print(aleatorios)


# Funciones anidadas dentro de otras funciones.


def aceleracion(f, m):
    acel = (f / m)
    return acel


montek2 = aceleracion  # la variable montek2 guarda la función aceleración

libertad = montek2(1000, 2)  # libertad guarda el resultado de función aceleración
print("Este valor es de libertad:", libertad)

montek3 = id(montek2)  # averiguamos la dirección en memoria de montek2
montek4 = id(aceleracion)  # averiguamos la dirección en memoria de aceleración
print(montek3)  # Estos números son iguales ya que tienen el mismo numero en memoria
print(montek4)  # Estos números son iguales ya que tienen el mismo numero en memoria


def velocidad(montek2, tiempo):
    resultado = aceleracion(50, 2) * tiempo  # aceleración es un función dentro de otra funcion
    return resultado


solucion = velocidad((50, 2), 100)
print(solucion)


# La sucesión de Fibonacci

def fibonacci(n_1):
    a_2, b_2 = 0, 1
    while a_2 < n_1:
        print(a_2, ",", end="")
        a_2, b_2 = b_2, a_2 + b_2


fibonacci(n_1=int(input("Teclea numero elementos de tu serie Fibon:")))


# Forma de utilizar y expresar las funciones I

def area():
    base_5 = 10
    altura_5 = 4
    mi_area = base_5 * altura_5
    return mi_area


solucion_k1 = area()
print("\nEl valor es:", solucion_k1)

# Forma de utilizar y expresar las funciones II

base = 10
altura = 4


def area1():
    mi_area = base * altura
    return mi_area


solucion_k11 = area1()
print(solucion_k11)


# Forma de utilizar y expresar las funciones III

def area2(base_7, altura_7):
    mi_area = base_7 * altura_7
    return mi_area


solucion_k111 = area2(10, 4)
print(solucion_k111)


# Fórmula de Heron en función – Resolución de triángulos

def formula_de_heron(a_9, b_9, c_9):
    semi_suma = float(a_9 + b_9 + c_9) / 2
    print("La semi-suma de los lados del triángulo es:", semi_suma)
    solucionformulaheron = math.sqrt(semi_suma * (semi_suma - a_9) * (semi_suma - b_9) * (semi_suma - c_9))
    print(round(solucionformulaheron, 3))
    return


formula_de_heron(80, 70, 60)

# Salida en forma tabulada de las tablas de los cuadrados, cubos, etc.
for x in range(1, 11):
    print(repr(x).rjust(2), repr(pow(x, 2)).rjust(3),
          repr(pow(x, 3)).rjust(4), repr(pow(x, 4)).rjust(5),
          repr(pow(x, 5)).rjust(6), repr(pow(x, 6)).rjust(7))


# El alumno tiene que modificar el código para que sea más genérico y universal.
# Hacerlo con while y bucles for.


# Funcion lee argumentos que le pasamos en forma de tupla parámetros fijos

def mi_lista(*args):
    for count, arg in enumerate(args):
        print('%d - %s' % (count, arg))


print("Primera invocacion de la funcion")
mi_lista("Antonio", "Python.com")

print('Segunda invocacion de la funcion')
mi_lista('Pepito Grillo', 2019, 'Calabaza mix', [1, 2, 3], 'Python.com')


# Función lee argumentos que le pasamos en forma de tupla claves valor

def read_dict_args(**kwargs):
    for key, value in kwargs.items():
        print('%s - %s' % (key, value))


print('\nPrimera lista de diccionarios\n')
read_dict_args(name1='Jose Luis', name2='Rodriguez', web='elpuma.com')

print('\nSegunda lista de diccionarios\n')
read_dict_args(Equipo='Valencia FC', Jugador='Mario Alberto Kempes', Demarcation='Delantero', Dorsal=10)


# Funcion que da distintas opciones
def menubanco():
    opcion = ""
    while not ("a" <= opcion <= "d"):
        print("CAJERO AUTOMATICO")
        print("a.- Ingresar dinero")
        print("b.- Sacar dinero")
        print("c.- Consulta saldo")
        print("d.- Transfesrencias")
        opcion = input("Elija una opción para su actividad: ")
        if opcion == "a":
            print("Ha elegido ingresar dinero")
        elif opcion == "b":
            print("Ha elegido sacar dinero")
        elif opcion == "c":
            print("Ha elegido consultar saldo")
        elif opcion == "d":
            print("Ha elegido realizar transferencias")
        elif opcion > "d":
            print("Se ha producido un error. Pruebe otra vez")
            return opcion


menubanco()
