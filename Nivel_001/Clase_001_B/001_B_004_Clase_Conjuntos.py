# Ejemplo 1 Conjuntos (Conjunto set)

aa = set({1, 2, 3})
print('El valor es:',aa) # Salida {1, 2, 3}

# Ejemplo 2 Conjuntos (Eliminación de datos en listas)

m = [1,2,3,4,5,6,2]
print('El valor es:',m)   # Nos imprime todos los números.
m = list(set(m))
print ('El valor es:',m) # Elimina los repetidos [1, 2, 3, 4, 5, 6]

# Ejemplo 3 Conjuntos (Conversion a conjunto)

aa = set ([1,2,3,"aa"])
print('El valor es:',aa) # Salida {1, 2, 3, 'aa'}

# Ejemplo 4 Conjuntos (Conversion a conjunto *)

aa1 = set(frozenset ([1,2,3]))
print('El valor es:',aa1) # Salida {1, 2, 3}

# Ejemplo 5 Conjuntos (Operaciones con los conjuntos)

s1, s2 = {1,2,3}, {4,5,6,3,2}
k = s1 - s2 # diferencia de conjuntos
print ('El valor es:',k) # Salida {1}

s1, s2 = {1,2,3}, {4,5,6,3,2}
k1 = s1 & s2 # Intersección de conjuntos
print ('El valor es:',k1) # Salida {2,3}

s1, s2 = {1,2,3}, {4,5,6,3,2}
k2 = s1 ^ s2 # Diferencia simétrica
print ('El valor es:',k2) # Salida {1, 4, 5, 6}

s1, s2 = {1,2,3}, {4,5,6,3,2}
k3 = s1 | s2 # unión de conjuntos
print ('El valor es:',k3) # Salida {1, 2, 3, 4, 5, 6}

# Ejemplo 6 Conjuntos (Utiizacion de set con strings)

s3 = set ({"Triangulo", "Circulo", "Cuadrado", "Rombo", "Rectángulo"})
print('El valor es:',s3) # los imprime aleatoriamente cada vez que se ejecuta

# Ejemplo 7 Conjuntos (Creacion de conjunto con numeros como strings)

aa = set ("12356")
print('El valor es:',aa) # Salida {'6', '2', '1', '5', '3'}

# Ejemplo 8 Conjuntos (Escritura de un conjunto directamente)

mucho= {"hola", "amigos"}
print('El valor es:',mucho) # {'hola', 'amigos'} Conjunto de strings

mucho1= {123456789}
print('El valor es:',mucho1) # {123456789} conjunto de números
