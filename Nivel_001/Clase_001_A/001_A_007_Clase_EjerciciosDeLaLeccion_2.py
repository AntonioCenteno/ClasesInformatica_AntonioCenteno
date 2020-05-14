print()
print('*********************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Leccion 2ª Archivo: 001_007_Clase_EjerciciosDeLaLeccion_2')
print('          Profesor: Antonio Centeno')
print('*********************************************************************************\n')
print('*********************************************************************************')
print('*********************************************************************************\n')

# Ejercicio 1

a,b,c,d,e,f,g,h,j = 2,4,3,5,6,7,8,9,10
solucion = ((a**2)/(b-c))+((d-e)/(f-((g*h)/j)))
print (solucion)

# Ejercicio 2,3,4

"Ejercicios de teoria para resolver en cuaderno"

# Ejercicio 5

import math # este import debe ir a inicio de archivo

# Módulo de petición de datos

a = int(input("Teclea el valor del coeficiente 'a': "))
b = int(input("Teclea el valor del coeficiente 'b': "))
c = int(input("Teclea el valor del coeficiente 'c': "))

#Módulo de operaciones

m = math.sqrt(b**2+(-4)*(a)*(c)) # Hacer captura de errores.
Solucion1 = ((-b) + m)/(2*(a))
Solucion2 = ((-b) - m)/(2*(a))

#Salida de respuestas

print(f"La solucion primera es: {Solucion1}", end="")
print(f" \nLa solucion segunda es: {Solucion2}", end="")
print(f" \nEl discriminante tiene un valor de:  {m}", end="")

#Salida respuesta discriminante.

if m == 0:
    print(f"\nTiene una solución doble. Discriminante: {m}")
elif m >=0:
    print (f"\nTiene dos soluciones reales. Discriminante: {m}")
else:
    print(f"\nNo tiene solución real. Discriminante: {m}")

# Ejercicio 6

# Módulo de petición de datos

print ("***************************")
print ("*** Cambio 1.5 $  = 1 € ***")
print ("****************************\n")

print("Teclea el 1 para cambio de dólares a euros: ")
print("Teclea el 2 para cambio de euros a dólares: ")
a = int(input("Número: "))

# Módulo de operaciones

if a ==1:
    c = int(input("Teclea el número de dólares a cambiar: "))
    d = c/1.5
    g = (round(d,4))
    print(f"\n Por,{c}, dólares le corresponden: ", g , "€")
else:
    e = float(input("Teclea el número de euros a cambiar: "))
    f = e * 1.5;    h = (round(f,4))
    print(f"\n Por,{e}, euros le corresponden: ", h , "$")

# Ejercicio 7
"Ejercicio para que el alumno realice un programa libre"

# Ejercicio 8

# apartado a
a = 27 // 4
b = a + (15/4)
print (b)

# apartado b
c = float((37/(4^2))-2)
print (c)

# apartado c
m = ((9*2)/(3*25*3))
print (m)

# apartado d
w = (((7*3)-(4*4))**2)/(4*2)
print (w)

# apartado e
a, b, c = 25, 7, 2 # Puedo declarar estas variables en la misma línea.
if (a >= b) and (not (7 <= 20)):
    print("Si es vedad lo anterior escribo esta frase")
else:
    print("Si escribo esta frase es por que lo anterior es falso")

# apartado f
if (((24 > 5) and  (10 <= 0)) or (10 == 5)):
    print("Si es vedad lo anterior escribo esta frase")
else:
    print("Si escribo esta frase es por que lo anterior es falso")

# apartado g
if (((10 >= 15) or  (23 == 13)) and (not (8 == 8))):
    print("Si es vedad lo anterior escribo esta frase")
else:
    print("Si escribo esta frase es por que lo anterior es falso")

# apartado h
if ((not (6/3) > 3) or (7 > 7)) and ((3 <= (9/2) or (2+3) <= (7/2))):
    print("Si es vedad lo anterior escribo esta frase: VERDADERO")
else:
    print("Si escribo esta frase es por que lo anterior es falso: FALSO")

