print()
print('*********************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Leccion 2ª Archivo: 001_B_005_Clase_EjerciciosDeLaLeccion_3')
print('          Profesor: Antonio Centeno')
print('*********************************************************************************\n')
print('*********************************************************************************')
print('*********************************************************************************\n')

# Ejercicio 1

Enteros1 = [1, 2, 3, 5, 4, 3, 27, 14, 5, 25]
Enteros1 = [1, 2, 3, 5, 4, 3, 27, 14, 5, 25]
Enteros1.remove(3)  # elimina en numero 3
Enteros1.remove(5)  # elimina el numero 5
Enteros1.sort()  # ordena la lista
print('El resultado es:',Enteros1)

# Ejercicio 2

a = {"melón", "fresa", "manzana"}
b = {"piña", "coco", "melocotón","manzana"}
c = {"papaya", "toronja", "naranja", "cereza", "manzana"}
# Union de los tres conjuntos sin repetición
conjunto_unico = a | b | c
print('El resultado es:',conjunto_unico)
# {'cereza', 'papaya', 'naranja', 'piña', 'melocotón', 'melon', 'coco', 'manzana', 'fresa', 'toronja'}

# Ejercicio 3

# Nos muestra el elemento común a los tres conjuntos

elemento_repetido = a & b & c  # interseccion de los tres conjuntos
print('El resultado es:',elemento_repetido)  # muestra el elemento común

# Eliminación de un elemento al azar.
mi_conjunto = {'cereza', 'papaya', 'naranja', 'piña', 'melocotón', 'melon', 'coco', 'manzana', 'fresa', 'toronja'}
mi_conjunto1 = mi_conjunto.pop()  # elimina item al azar
print('El resultado es:',mi_conjunto1)  # muestra item elegido
print('El resultado es:',mi_conjunto)  # imprime el conjunto sin el item

# eliminacion de item que empieza por "m"
mi_conjunto2 = {"cereza", "papaya", "naranja", "piña", "melocotón", "melon", "coco", "manzana", "fresa", "toronja"}
mi_conjunto2.remove("manzana")
print('El resultado es:',mi_conjunto2)


# Ejercicio 4

# Incluimos Suecia

eur = {"Italia", "Bulgaria", "Francia", "Irlanda", "Hungria", "Finlandia", "España", "Polonia"}
eur.add("Suecia")  # añade item Suecia a conjunto eur
print('El resultado es:',eur)  # imprime conjunto completo

# Realizacion de copia del conjunto

europa = eur.copy()
print('El resultado es:',europa)
variable = eur is eur.copy
print('El resultado es:',variable)

# Preguntamos si Serbia está en el conjunto eur

variable1 = "Serbia" in eur
print('El resultado es:',variable1)

# Preguntamos si Hungria está en el conjunto eur

variable1 = "Hungria" in eur
print('El resultado es:',variable1)

# Averiguamos la longitud del conjunto

longitud_conjunto = len(eur)
print('El resultado es:',longitud_conjunto)


# Ejercicio 5

# Obtenemos los elementos no comunes a los dos conjuntos

D_mito = {"Marte", "Júpiter", "Zeus", "Mercurio", "Cronos", "Neptuno", "Gea", "Cibeles"}
Planetas = {"Urano", "Mercurio", "Marte", "Venus", "Júpiter", "Tierra"}
Elementos_no_Comunes = D_mito.intersection(Planetas)
print('El resultado es:',Elementos_no_Comunes)

# Ejercicio 6

# Conjuntos disjuntos son los que no tienen elementos en común
# Obtenemos el conjunto disjunto en primer lugar

Conjunto_Disjunto = D_mito ^ Planetas
print('El resultado es:',Conjunto_Disjunto)

# Vaciamos el conjunto disjunto. Nos dará set()

Conjunto_Disjunto.clear()
print('El resultado es:',Conjunto_Disjunto)


# Ejercicio 7

# Ordenamos la lista y la imprimimos

lista = ["b", "a", "d", "b", "c", "d"]
lista.sort()
print('El resultado es:',lista)

# Eliminamos duplicados en set

conversion = set(lista)
conversion_a_lista = list(conversion)

# ordenamos nuevamente y imprimimos

conversion_a_lista.sort()
print('El resultado es:',conversion_a_lista)

# Ejercicio 8

# Unimos las dos listas

Lista1 = ["1", "7", "9", "8", "4"]
Lista2 = ["3", "7.5", "2", "6", "0"]
Union_de_listas = Lista1 + Lista2
print('El resultado es:',Union_de_listas)

# Eliminar el (7.5)

Union_de_listas.pop(6)
print('El resultado es:',Union_de_listas)

# Eliminar el (0)

Union_de_listas.pop(8)
print('El resultado es:',Union_de_listas)

# Añadimos el numero (10)

Union_de_listas.append(10)
print('El resultado es:',Union_de_listas)

# Ejercicio 9

# Nuestra lista es Union_de_listas = ['1', '7', '9', '8', '4', '3', '2', '6', 10]
# Hallamos la lista de los impares

lista_impares = Union_de_listas[0:3] + Union_de_listas[5:6]
print('El resultado es:',lista_impares)

# Hallamos la lista de los pares

lista_pares = Union_de_listas[3:5] + Union_de_listas[6:9]
print('El resultado es:',lista_pares)

# invertimos el orden de las listas

lista_pares.reverse()  # primero la de los pares
print('El resultado es:',lista_pares)
lista_impares.reverse()  # la de los impares
print('El resultado es:',lista_impares)


# ejercicio 10

lista4 = [6, 38, 10, 54, 45, 25, 76]
lista_Ordenada4 = [item for item in lista4 if item % 5 == 0]
print('El resultado es:',lista_Ordenada4)

# ejercicio 11 (Lo completa el alumno)

# ejercicio 12

Lista6 = ["Mallorca", "Cordega", "Malta", "Chipre", "Rodas"]
Lista6_Nueva = [item for item in Lista6 + ["Creta"]]
print('El resultado es:',Lista6_Nueva)



# Ejercicio 13

lista7 = ["Argelia", "Gabon", "China", "Senegal", "Canada", "España"]
lista7.pop(2) and [lista7.pop(3) and lista7.pop(3)]
print('El resultado es:',lista7)
# Insertamos los paises que queramos (3)
lista7.insert(2, "Mozambique");
lista7.insert(4, "Marruecos");
lista7.insert(5, "Malawi")
print('El resultado es:',lista7)

# Ejercicio 14 Lo hacemos con los datos originales

lista8 = ["oro", "plata"]
frozenset = ({"Oxigeno", "nitrógeno", "hidrogeno"})
lista10 = ["aluminio", "hierro", "mercurio"]
lista_final = list(lista8) + list(frozenset) + list(lista10)
print('El resultado es:',lista_final)

a1 = ["oro", "plata"]
a2 = ({"Oxigeno", "nitrógeno", "hidrogeno"})
a3 = ["aluminio", "hierro", "mercurio"]
lista_final1 = list(a1) + list(a2) + list(a3)
print('El resultado es:',lista_final1)


# Ejercicio 15

Nueva_lista = ['oro', 'plata', 'hidrogeno', 'nitrógeno', 'Oxigeno', 'aluminio', 'hierro', 'mercurio']
Nueva_lista[3:5] = ["boro", "Cromo"]
print('El resultado es:',Nueva_lista)  # ['oro', 'plata', 'hidrogeno', 'boro', 'Cromo', 'aluminio', 'hierro', 'mercurio']


# Ejercicio 16

a = [1, 2, 3, 4, 5]
b = {1, 2, 3, 4, 5}
c = 1  # este nos dará error porque es un int un objeto no iterable
d = "1"
# Convertimos en tuplas los conjuntos anteriores

tuple(a);print('El resultado es:',a)
tuple(b);print('El resultado es:',b)
tuple(d);print('El resultado es:',d)
# tuple (c)como no es objeto iterable no se puede convertir en tupla.13

# Ejercicio 17

m = ("Aneto", "Teide", "Moncayo")
# añadir "Mulhacen"
b = "Mulhacen",  # cuidado si no pones la coma Mulhacen sale en letras separadas
picos = m + tuple(b)
print('El resultado es:',picos)  # ('Aneto', 'Teide', 'Moncayo', 'Mulhacen')
# determinar la longitud de el ultimo conjunto
longitud_picos = len(picos)
print('El resultado es:',longitud_picos)  # 4 longitud
# determinar mediante indices que item es de los pirineos
print('El resultado es:',picos[0])  # Aneto16

# Ejercicio 18

m = ("a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "b", "c" "a", "d", "f", "a", "b", "c")
cuenta_a = m.count("a");
print('El resultado es:',cuenta_a)  # m es la variable o tupla de donde se toman los datos.
cuenta_b = m.count("b");
print('El resultado es:',cuenta_b)
cuenta_c = m.count("c");
print('El resultado es:',cuenta_c)
cuenta_d = m.count("d");
print('El resultado es:',cuenta_d)
cuenta_e = m.count("e");
print('El resultado es:',cuenta_e)
cuenta_f = m.count("f");
print('El resultado es:',cuenta_f)
cuenta_g = m.count("g");
print('El resultado es:',cuenta_g)


# Ejercicio 19
# Determinar la longitud de la tupla m

longitud_m = len(m)
print('El resultado es:',longitud_m)  # longitud 17
# añadimos los elementos hasta completar el abecedario español
m = ("a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "b", "c", "a", "d", "f", "a", "b", "c")
m1 = ("h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z")
lista_completa_abecedario = m1 + m  # esto nos da la unión de tuplas "m" y "m1"
print('El resultado es:',lista_completa_abecedario)  # nos imprime la tupla para verla
lista_a_lista = list(lista_completa_abecedario)  # convertimos la tupla en lista
print('El resultado es:',lista_a_lista)  # imprimimos la lista
conversion_a_set = set(lista_a_lista)  # convertimos la lista en un set
kata = list(conversion_a_set)  # el set lo convertimos a lista nuevamente
por_fin_ordenada = sorted(list(kata))  # ordenamos la lista con sus metodos
print('El resultado es:',por_fin_ordenada)  # por fin imprimimos la lista ordenada.
# dividimos la tupla en tres partes. La tupla es lista_completa_abecedario
division_de_unaTupla = len(por_fin_ordenada) / 3
print('El resultado es:',division_de_unaTupla)  # nos dara 8.333 tomamos 8 para los primeros
primera_division = lista_completa_abecedario[0:8];
print('El resultado es:',primera_division)
# tiene 8 elementos
segunda_division = lista_completa_abecedario[8:16];
print('El resultado es:',segunda_division)
# tiene 8 elementos
tercera_division = lista_completa_abecedario[16:25];
print('El resultado es:',tercera_division)
# tiene 9 elementos
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
# averiguar en que lugar esta la letra "c" y la "g" en la tuplas "por_fin_ordenada"
# y en las tres divisiones anteriores de la tupla original
pregunta_por_c = "c" in por_fin_ordenada  # preguntamos si "c" está en el conjunto
print('El resultado es:',pregunta_por_c)
pregunta_por_g = "g" in por_fin_ordenada  # preguntamos si "c" está en el conjunto
print('El resultado es:',pregunta_por_g)
posicionde_c = por_fin_ordenada.index("c")  # posicion de "c"
print('El resultado es:',posicionde_c)
posicionde_g = por_fin_ordenada.index("g")  # posicion de "g"
print('El resultado es:',posicionde_g)
posicionde_z = por_fin_ordenada.index("z")  # posicion de "z"
print('El resultado es:',posicionde_z)



# Ejercicio 20
D = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
longitud_D = len(D)
print('El resultado es:',longitud_D)
# verficacion si existen las claves c,d,f
verificacion_c = "c" in D
print('El resultado es:',verificacion_c)  # True
verificacion_e = "e" in D  # True
print('El resultado es:',verificacion_e)
verificacion_f = "f" in D  # False
print('El resultado es:',verificacion_f)


# Ejercicio 21
# introducir el par clave g:7

D["g"] = 7
print('El resultado es:',D)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7}
# eliminar "b":2 sin metodo
print('El resultado es:',D)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'g': 7}
del D["b"]  # Eliminacion de "b"
print('El resultado es:',D)  # D={'a': 1, 'c': 3, 'd': 4, 'e': 5, 'g': 7}
# Sustitucion de clave "d"
del D["d"]  # eliminacion de d
D["h"] = 4
print('El resultado es:',D)  # {'a': 1, 'c': 3, 'e': 5, 'g': 7, 'h': 4}19	20

# Ejercicio 22

capitales = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}
num = (1, 2, 3)
# Asignar a cada clave la tupla num
capitales1 = capitales.fromkeys(capitales, num)
print('El resultado es:',capitales1)  # capitales1 = {'España': (1, 2, 3), 'Francia': (1, 2, 3), 'Italia': (1, 2, 3)}
# Asignar a diccionario cada elementos de la tupla num
capitales2 = capitales.fromkeys(num, capitales)
print('El resultado es:',capitales2)
# {1: {'España': 'Madrid', 'Francia': 'Paris', 'Italia': 'Roma'}, 2: {'España': 'Madrid', 'Francia': 'Paris', 'Italia': 'Roma'}, 3: {'España': 'Madrid', 'Francia': 'Paris', 'Italia': 'Roma'}}


# Ejercicio 23

capitales = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}
print('El resultado es:',capitales.keys())  # nos da las claves del diccionario
print('El resultado es:',capitales.values())  # nos da los valores del diccionario7


# Ejercicio 24

capitales = {"España": "Madrid", "Francia": "Paris", "Italia": "Roma"}
capitales3 = {"Alemania": "Berlin", "Noruega": "Oslo", "Portugal": "Lisboa"}
# unir el diccionario capitales con capitales3
capitales.update(capitales3)  # unimos a capitales el diccionario capitales3
print('El resultado es:',capitales)
# eliminamos un par con un metodo
capitales.pop("Portugal")  # eliminamos Portugal
print('El resultado es:',capitales)
# realizacion de una copia superficial
capitales4 = capitales.copy()  # nos crea una copia del diccionario capitales
print('El resultado es:',capitales4)
capitales4.clear()  # vaciamos el diccionario capitales4
print('El resultado es:',capitales4)  # el resultado es un diccionario vacío {}23


# ejercicio 25

mi_diccionario = {key: pow(key, 2) for key in (1, 2, 3, 4, 5)}
print('El resultado es:',mi_diccionario)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
mi_diccionario = {key: pow(key, 2) for key in (1, 2, 3, 4, 5) if key % 2 == 0}
print('El resultado es:',mi_diccionario)  # mi_diccionario = {2: 4, 4: 16}8
