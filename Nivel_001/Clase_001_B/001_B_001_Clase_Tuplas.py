# Ejemplo 1 tuplas

tupla_ejemplo = ("hola", 2 + 3j, -1.2, 'Antonio', 25)
# Guarda datos tipo cadena (hola y Antonio), un dato complejo 2+3j, un dato entero, 25.
# Algunas acciones con las tuplas.

a = tupla_ejemplo[2]  # -1.2  Nos muestra solo el elemento de el lugar 2º
b = tupla_ejemplo[1:4]  # ((2+3j), -1.2, 'Antonio')# Muestra desde el 1 hasta el tercero.
c = tupla_ejemplo[3:]  # ('Antonio', 25) Nos muestra desde el 3º hasta el final.
d = tupla_ejemplo[:2]  # ('hola', (2+3j)) Muestra desde el inicio hasta el lugar anterior al 2
e = tupla_ejemplo[-1]  # 25 Cuenta hacia atrás; primero el cero que es “hola” y se va al final.
f = tupla_ejemplo[-3]  # -1.2 Cuenta hacia atrás al igual que el ejemplo anterior.

print(a)
print(b)
print(c)
print(d)
print(e)

# Ejemplo 2 tuplas

tupla_ejemplo = ('hola', ('uno', 'dos', 'tres'), 45, -1.2)

a1 = tupla_ejemplo[2]
b1 = tupla_ejemplo[1:4]
c1 = tupla_ejemplo[3:]
d1 = tupla_ejemplo[:2]
e1 = tupla_ejemplo[-1]
f1 = tupla_ejemplo[-3]
print(a1)  # 45
print(b1)  # (('uno', 'dos', 'tres'), 45, -1.2)
print(c1)  # (-1.2,)
print(d1)  # ('hola', ('uno', 'dos', 'tres'))
print(e1)  # -1.2
print(f1)  # ('uno', 'dos', 'tres')

# Ejemplo 3 tuplas

m = tuple('antonio')
print(m)  # la respuesta es una tupla (‘a’, ’n’, ’t’, ’o’, ’n’, ’i’, ’o’)

# Ejemplo 4 tuplas

tupla_ejemplo = ('hola', ('uno', 'dos', 'tres'), 45, -1.2)

a1 = tupla_ejemplo[2]
b1 = tupla_ejemplo[1:4]
c1 = tupla_ejemplo[3:]
d1 = tupla_ejemplo[:2]
e1 = tupla_ejemplo[-1]
f1 = tupla_ejemplo[-3]
print(a1)  # 45
print(b1)  # (('uno', 'dos', 'tres'), 45, -1.2)
print(c1)  # (-1.2,)
print(d1)  # ('hola', ('uno', 'dos', 'tres'))
print(e1)  # -1.2
print(f1)  # ('uno', 'dos', 'tres')

# Ejemplo 5 tuplas ( tupla sin parentesis)

mi_tupla = 2, 3, 4, "burro"
k = mi_tupla[1]
print(k)  # sale por pantalla el número 3

# Ejemplo 6 tuplas (Conversion de tupla en lista)

mi_tupla = 2, 3, 4, "Casa de campo"
k = list(mi_tupla)
print(k)  # Salida [2, 3, 4, 'Casa de campo']

# Ejemplo 7 tuplas (Tupla  de un solo numero con coma al final)

mi_tupla = 2,
print(mi_tupla)  # salida (2,)

# Ejemplo 8 tuplas (Contar cuantos elementos iguales hay en una tupla)

mi_tupla = ('lunes', 'martes', 'jueves', 'lunes', 'lunes')
f = mi_tupla.count('lunes')
print(f)  # salida el numero 3 por que se repite el lunes tres veces.

# Ejemplo 9 tuplas (Averiguar en que posicion se encuentra un item)

mi_tupla = (1640, 123, 450, 1929, 1964)
f = mi_tupla.index(1929)
print(f)  # Nos indica que (1929) se encuentra en la tercera posición.

# Ejemplo 10 tuplas (Ejemplo que resume lo estudiado de tuplas)

mi_tupla = (1, 9, 3, 8, 5, 2, 7, 4, 6)
for item in mi_tupla:
    print("El número es: ", item)

# convertir una tupla en lista para ordenarla
a = list(mi_tupla)  # convertimos tupla en lista
a.sort()  # ordenamos la lista
s = tuple(a)  # la convertimos en tupla
print(s)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
0
# Uso de set() aplicado a un tupla para eliminar items repetidos
mi_tupla = (1, 9, 3, 8, 5, 5, 5, 2, 5, 4, 7, 4, 6)
print(set(mi_tupla))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# método (reverse, append) para ordenar inversamente y añadir items.
k = (5, 9, 4, 1, 3, 0)  # tenemos una tupla
k1 = list(k)  # la convertimos a lista
k1.append(2)  # le añadimos el 2
k1.sort()  # la ordenamos
list.reverse(k1)  # la ordenamos a la inversa
m = tuple(k1)  # la convertimos a tupla
print(m)  # la imprimimos

# métodos (count, index), contar y lugar que ocupa

r = ("a", "z", "d", "m", "p", "d", "miau")

repetidas = r.count("d")  # nos dice cuántas "d" hay
print(repetidas)  # nos imprime 2
lugar = r.index("miau")  # nos dice en qué lugar esta "miau"
print(lugar)  # nos imprime que en el sexto

# operaciones con tuplas
t = (1, 2, 3)
m = (4, 5, 6)
p = t + m;
print(p)  # se unen t y m
p1 = t * 3;
print(p1)  # se triplica la t
p3 = t < m;
print(p3)  # operacion booleana
p4 = t <= m;
print(p4)  # operacion booleana
p5 = t > m;
print(p5)  # operacion booleana
p6 = t >= m;
print(p6)  # operacion booleana
p7 = t != m;
print(p7)  # operacion booleana

# Saber si un item está o no está en una tupla
print(4 in t)  # respuesta false
print(4 not in t)  # respuesta true
