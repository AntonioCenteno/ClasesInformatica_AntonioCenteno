# Ejemplo 1 (Estructura basica funcion)


def saludos():
    print("Hola Pythonistas")
    return


saludos()  # Cada vez que se invoque, se ejecutará el código del interior de la función.
saludos()
saludos()


# Ejemplo 2 (Paso parametros sin limite)
def recorrer_ciudades(ciudad_fija, *ciudades_arbitrarias):
    print(ciudad_fija)
    for item in ciudades_arbitrarias:
        print(item)


recorrer_ciudades("Zamora", "León", "Salamanca", "Valladolid", "Ávila", "Segovia", "Soria", "Burgos")


# Ejemplo 3 (Paso parametros sin limite)
def recorrer_ciudades(ciudad_fija, *ciudades_arbitrarias, **keyword):
    print(ciudad_fija)
    for item in ciudades_arbitrarias:
        print(item)
    for clave in keyword:
        print("El número ", clave, "corresponde a: ", keyword[clave])


recorrer_ciudades("Zamora", "León", "Salamanca", "Valladolid", "Ávila", "Segovia", "Soria", "Burgos", clave1="Almería",
                  clave2="Córdoba", clave3="Huelva", clave4="Cádiz", clave5="Sevilla", clave6="Málaga",
                  clave7="Granada", clave8="Jaén")


# Ejemplo 3 (Paso parametros en forma tupla)


def benavente(x, ciudad=[]):
    ciudad.append(x)
    return ciudad


print(benavente(10))  # [10]
print(benavente(7))  # [10, 7]
print(benavente(12))  # [10, 7, 12]


# Ejemplo 4 (Paso parametros en forma tupla)


def benavente(x, ciudad=None):
    if ciudad is None: ciudad = []
    ciudad.append(x)
    return ciudad


print(benavente(10))  # [10]
print(benavente(7))  # [7]


# Ejemplo 5 (Argumentos Posicionales)


def suma(x, y):
    return print("El resultado sumado es:", x + y)


suma(3, 4)


# Ejemplo 6 (Argumentos nominales)

def suma(a, b):
    return print("La suma es:", a + b)


suma(a=3, b=4)


# Ejemplo 7 (Tuplas como argumento)


def america(x, y, z):
    z.append(13)
    return print(x, y, z)  # La salida es: 10 11 [12, 14, 15, 13]


k = 10
kk = 11
america(k, kk, z=[12, 14, 15])


# Ejemplo 8 (Diccionario como argumento)

def america(**kwargs):
    return print(kwargs)


america(clave1=12, clave2=14, clave4="Hola Pitonistas")
# Salida {'clave1': 12, 'clave2': 14, 'clave4': 'Hola Pitonistas'}

