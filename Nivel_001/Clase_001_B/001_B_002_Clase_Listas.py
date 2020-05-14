# Ejemplo 1 Listas (Ejemplo de lista)

mi_lista = ["nombre", 23, -23, 3+4j, 23.36]

# Ejemplo 2 Listas (Extraccion de una lista un subconjunto. Es lista tambien)

alumnos = [45632, 59681, 62561, 19640]
k = alumnos [0:2]
print (k) # La salida será [45632, 59681]

# Ejemplo 3 Listas (Saber la longitud de una lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada']
d = len(alumnos)
print ("El valor de la lista es:",d)  # salida 4

# Ejemplo 4 Listas (Como se accede a los datos de una lista)

lista_ejemplo = ['hola', 2+3j, -1.2, 'Antonio', 25] # tupla de ejemplo

a = lista_ejemplo[2]   # -1.2  Nos muestra solo el elemento que ocupa el lugar 2
b = lista_ejemplo[1:4] # ((2+3j), -1.2, 'Antonio')# Muestra desde el 1 hasta el 3.
c = lista_ejemplo[3:]  #('Antonio', 25) Nos muestra desde el tercer lugar hasta el final.
d = lista_ejemplo[:2]  #('hola', (2+3j)) #Muestra desde inicio hasta el lugar anterior al 2
e = lista_ejemplo[-1]  #25 Cuenta hacia atrás primero “hola” y se va al final de la tupla.
f = lista_ejemplo[-3]  #-1.2 Cuenta hacia atrás al igual que el ejemplo anterior.
print("El valor de la lista es:",a)
print("El valor de la lista es:",b)
print("El valor de la lista es:",c)
print("El valor de la lista es:",d)
print("El valor de la lista es:",e)

# Ejemplo 5 Listas (Cambiando elementos de lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada'] # cambiamos mermelada por compota
alumnos[3]= 'compota'
print ("El valor de la lista es:",alumnos)  # la salida es [45632, 59681, (62561, 19640), 'compota']

# Ejemplo 6 Listas (Agregar item a una lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada'] # agregamos manzanas al final.
alumnos.append('manzanas')
print ("El valor de la lista es:",alumnos)       # [45632, 59681, (62561, 19640), 'Mermelada', 'manzanas']

# Ejemplo 7 Listas (Agregar item en posicion determinada k)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada']
alumnos.insert(3,'limon')
print ("El valor de la lista es:",alumnos) # salida [45632, 59681, (62561, 19640), 'limon', 'Mermelada']

# Ejemplo 8 Listas (Eliminar un item de una lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada']
alumnos.remove(59681)
print("El valor de la lista es:",alumnos) # salida [45632, (62561, 19640), 'Mermelada']

# Ejemplo 9 Listas (Saber si un item pertenece a la lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada']
d = 45632 in alumnos
print("El valor de la lista es:",d) # Salida True. Prueba cambiando el número y verifica si da False
# Pruebe el alumno con el nº6251 y después con la tupla (62561, 19640)

# Ejemplo 10 Listas (Conocer la posicion de un item dentro de la lista)

alumnos = [45632, 59681, (62561, 19640), 'Mermelada']
d = alumnos.index ('Mermelada')
print("El valor de la lista es:",d) # salida 3

# Ejemplo 11 Listas (Concatenar secuencias de dos listas)

alumnos = [2,4,6,8,9]
frutas = ['manzana', 'pera']
k = alumnos + frutas
print("El valor de la lista es:",k) # salida [2, 4, 6, 8, 9, 'manzana', 'pera']

# Ejemplo 12 Listas (Concatenar o duplicar listas)

alumnos = [2,4,6,8,9]
frutas = ['manzana', 'pera']
k =  frutas * 2
print("El valor de la lista es:",k) # salida ['manzana', 'pera', 'manzana', 'pera']

# Ejemplo 13 Listas (Maximo de una lista)

alumnos = [1,2,4,6,8,10]
k = max(alumnos)
print("El valor de la lista es:",k) # salida 10

# Ejemplo 14 Listas (Minimo de una lista)

alumnos = [1,2,4,6,8,10]
k = min(alumnos)
print("El valor de la lista es:",k) # salida 1

# Ejemplo 15 Listas (Tamaño de una lista)

alumnos = [1,2,4,6,8,10]
k = len(alumnos)
print("El valor de la lista es:",k) # salida 6 elementos

# Ejemplo 16 Listas (Acceso a una tupla e intercambio)

Ai = ['Mono', 1,2,3,4]
Ai.append("Orangutan") # escribe "Orangután" al final
print("El valor es:",Ai)
Ai.insert(2, "Simio") # escribe "Simio" en el lugar de 2
print("El valor es:",Ai)
Ai.extend(["hola", "gato"]) # añade al final "hola" y "gato"
print("El valor es:",Ai)

# Ejemplo 17 Listas (Acceso a una tupla dentro de una lista)

mi_lista = [1,2,3,('Oranutan', 'Chimpance', 'Simio')] # lista que guarda tupla
k = mi_lista[3][2]
print("El valor es:",k) # Salida Simio

# Ejemplo 18 Listas (Acceso a una lista dentro de una lista)

mi_lista = [1,2,3,['dia', 'mes', 'año']] # Acceso a una lista dentro de una lista
k = mi_lista[3][1]
print("El valor es:",k) # Salida "mes"

# Ejemplo 19 Listas (Intercambio dentro de listas)

lista = [1, 'dos', 'False', [45, 'cien']]
lista [0:2] = [5, 'mil']   # sustituimos  1 y “dos” por 5 y “mil”.
print("El valor es:",lista)               #Salida [5, 'mil', 'False', [45, 'cien']]

