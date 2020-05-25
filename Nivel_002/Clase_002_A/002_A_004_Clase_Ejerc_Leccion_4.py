print()
print('*********************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Leccion 2ª Archivo: 002_A_004_Clase_EjerciciosDeLaLeccion_4')
print('          Profesor: Antonio Centeno')
print('*********************************************************************************\n')
print('*********************************************************************************')
print('*********************************************************************************\n')

# Ejercicio 1
a = "abc"
if not a.isdigit():
    print("no contiene digitos")

# Ejercicio 2
a = "abc"
if a.isalpha():
    print("No contiene digitos, pero si contiene datos alfanumericos")

# Ejercicio 3
# Primera parte
a = "abc"
if a.isdigit() == False and a.isalpha() == True:
    print("No contiene digitos, pero si contiene datos alfanumericos")
# Segunda parte
if a.isdigit() == False or a.isalpha() == True:
    print("Imprime esta frase.")
# Trecera parte
if not a.isdigit():
    print("Imprime frase primera")
elif a.isalpha():
    print("Imprime frase segunda")

# Ejercicio 4
a = "123"
if not a.isdigit():
    print("No contiene numeros pero si tiene letras")
elif a.isalpha():
    print("No contiene numeros, pero si tiene letras")
else:
    print("Si contiene numeros en este caso")

# Ejercicio 5
# Primera parte
a, b, c = 17, 32, 9
if a <= b and a != c:
    print("1.- Correcto porque son verdaderas las dos")
else:
    print("1.- Incorrecto no cumple con las tablas de verdad")
# Segunda parte
if a >= c and b < a:
    print("2.- Correcto porque son verdaderas las dos")
else:
    print("2.- Incorrecto no cumple con las tablas de verdad")

# Ejercicio 6
a1 = ["Rojo", "Verde", "Azul"]
# Primera parte
if len(a1) == 3:
    print("La lista tiene tres colores")
else:
    print("La lista no tiene tres colores")
# Segunda parte
if a1.sort():
    print("La lista esta ordenada")
else:
    print("La lista no está ordenada")

# Ejercicio 7

# Primera parte
b1 = ["Rojo", "Verde", "Azul"]
if b1 == list:
    print("Es una lista")
elif b1 is not None:
    print("Es una lista")
else:
    print("No es una lista")
# Segunda parte
if "Amarillo" in b1:
    print("El amarillo está en la lista")
else:
    print("El amarillo no está en la lista")

# Ejercicio 8
b1 = ["Rojo", "Verde", "Azul"]
# Primera parte
if "Amarillo" in b1:
    print("1.- El Amarillo está en la lista")
elif "Azul" in b1:
    print("2.- El Amarillo está en la lista")
else:
    print("3.- El Amarillo no está en la lista")

# Segunda parte
if "Amarillo" in b1 and "Azul" in b1:
    print("4.- El Amarillo está en la lista")
else:
    print("5.- El Amarillo no está en la lista")

# Ejercicio 9
num1, num2 = 2, 5
if num1 < num2:
    print("Num1 es mas pequeño que Num2")

# Ejercicio 10
aa = (1, 2, 3)
bb = (1, 2, 3, 4)
if len(aa) < len(bb) != 5:
    print("La longitud de bb es mayor que aa y bb tiene longitud menor que 5")

# Ejercicio 11
vocales = ["a", "e", "i", "o", "u"]
for item in vocales:
    print("Esta vocal es: ", item)
for item in vocales[0:2]:
    print(item, "Es una vocal abierta")

# Ejercicio 12
vocales = ["a", "e", "i", "o", "u"]
for item in vocales:
    if item == "a" or item == "e" or item == "o":
        print(item, "Es una vocal abierta")
    else:
        print(item, "Es una vocal cerrada")

# Ejercicio 13
n = [1, 2, 3, 4, 5]
for x in n:
    print(x + 10)

# Ejercicio 14

a = ["g", "a", "p", "s", "f", "z", "m"]
a.sort()
for x in a:
    if x == "a":
        print(x, "Es la primera letra del abecedario")
    elif x == "z":
        print(x, "Es la ultima letra del abecedario")
    else:
        print(x, "Esta letra va delante.")

# Ejercicio 15
a = [13, 14, 16, 17, 11, 12, 19, 18]
for x in a:
    if x % 2 == 0:
        print(x, "Es numero par")
    else:
        print(x, "Es numero impar")

# Ejercicio 16
for x in range(1, 10, 2):
    print(x, "", end="")

# Ejercicio 17
palabra = "murcielago"
v = 0
for x in palabra:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print(x, " Es una vocal de la palabra murcielago")
        v += 1
    else:
        print(x, "No es una vocal de la plabra murcielago")
# v += 1  Aqui contaria todas las palabras 10 palabras
print("En la palabra murcielago tenemos: ", v, " vocales")

# Ejercicio 18
for x in range(1, 11):
    print(pow(x, 2), "", end="")

# Ejercicio 19
a = 0
while a <= 10:
    print(a, "", end="")
    a = a + 17

# Ejercicio 20
a = 0
while a <= 10:
    print(a, "", end="")
    a = a + 2

# Ejercicio 20 bis (otra manera de hacerlo)

print("\nEjercicio 20 bis")
contador_de_pares = 0
a = 0
while a <= 10:
    print(a, "", end="")
    if a % 2 == 0:
        print(a, "Es numero par")
        contador_de_pares = contador_de_pares + 1
    else:
        print(a, "Es numero impar")
    a = a + 1  # este es el contador del bucle while
print("Tenemos ", contador_de_pares, "numeros pares")

# Ejercicio 21
a = 1
while a <= 10:
    print(a, "", end="")
    a = a + 2
else:
    print("\nTodos estos numeros son impares")

# Ejercicio 22
lista_escalar = []
a = 0
while a <= 5:
    lista_escalar.append(a)
    a = a + 1
    print(lista_escalar)

# Ejercicio 23
lista1 = []
a = 0
while a <= 5:
    lista1.append(a)
    a = a + 1
else:
    print(lista1)

# Ejercicio 24
a = "Hol"
b = "a"
c = a + b
while len(c) <= 10:
    c = c + b
else:
    print(c + "!")

# Ejercicio 25
a = 0
while pow(a, 2) <= 1000:
    a = a + 16

# Ejercicio 26
a = 0
while pow(a, 2) <= 1000:
    a = a + 1
print("\nTenemos ", a, " numeros que cumplen con la condicion")

# Ejercicio 27 el alumno presentara uno hecho libre

# el import math esta al principio del documeneto
print("*" * 60)  # Encabezado decorativo
print("*" * 60)
print("**                                                        **")
print("**         *****  ******  *****  *****  *****             **")
print("**         ** **  ** ***  **     ** **  **                **")
print("**         *****  ****    ***    *****  ** **             **")
print("**         ** **  ** **   **     ** **     **             **")
print("**         ** **  ** ***  *****  ** **  ** **             **")
print("**                                                        **")
print("*" * 60)
print("*" * 60)
print("**                                                        **")
print("**\t - Opción 00: Salir del programa                      **")  # bloque de menú
print("**\t - Opción 01: Área de cuadrado y perímetro            **")
print("**\t - Opción 02: Área de rectángulos y perímetro         **")
print("**\t - Opción 03: Área de pentágono y perímetro           **")
print("**\t - Opción 04: Área de rombo y perímetro               **")
print("**\t - Opción 05: Área de romboide y perímetro            **")
print("**\t - Opción 06: Área de Trapecio y perímetro            **")
print("**\t - Opción 07: Área del circulo                        **")
print("**\t - Opción 08: Longitud circunferencia                 **")
print("**\t - Opción 09: Área y Volumen de un cubo               **")
print("**\t - Opción 10: Área y volumen de un ortoedro           **")
print("**\t - Opción 11: Área y volumen de un prisma             **")
print("**\t - Opción 12: Área y volumen de un cilindro           **")
print("**\t - Opción 14: Área y volumen de una pirámide          **")
print("**\t - Opción 15: Área y volumen de un cono               **")
print("**\t - Opción 16: Área y volumen de un tronco de pirámide **")
print("**\t - Opción 17: Área y volumen de un tronco de cono     **")
print("**\t - Opción 18: Área y volumen de una esfera            **")
print("**                                                        **")
print("*" * 60)
print("*" * 60)

opcionMenu = input("<< Teclea el número de opción que desees. >> ")  # opción al usuario

if opcionMenu == "01":
    print("")
    input("Has elegido Área de cuadrados....pulsa una tecla para continuar: ")
    baseCuadrado = float(input("Teclea la base del cuadrado: "))
    areaCuadrado = pow(baseCuadrado, 2)
    print("El Perimetro es:", 4 * baseCuadrado)
    print("El area es:", areaCuadrado)

elif opcionMenu == "02":
    print("")
    input("Has elegido Área de rectángulos...pulsa una tecla para continuar: ")
    baseRectangulo = float(input("Teclea la base del rectangulo: "))
    alturaRectangulo = float(input("Teclea la altura del rectangulo: "))
    areaRectangulo = baseRectangulo * alturaRectangulo
    print("El perimetro es: ", 2 * baseRectangulo + 2 * alturaRectangulo)
    print("El area es:", areaRectangulo)
elif opcionMenu == "03":
    print("")
    input("Has elegido Área de pentágonos...pulsa una tecla para continuar: ")
    basePentagono = float(input("Teclea la base del pentágono: "))
    apotemaPentagono = float(input("Teclea la apotema del pentágono: "))
    perimetro = 5 * basePentagono
    areaPentagono = (perimetro * apotemaPentagono) / 2
    print("El área es:", areaPentagono)
    print("El perímetro es:", areaPentagono)
else:
    print("Adios. Hasta pronto")

# Ejercicio 29 Programa que intercambia las variables
a = input("Introduce un numero o letra: ")
b = input("Introduce un numero o letra: ")
print("Has introducido para la variable a: ", a)
print("Has introducido para la variable b: ", b)
aux = a
a = b
b = aux
print("El nuevo valor de a es: ", a)
print("El nuevo valor de b es: ", b)

# Ejercicio 30 Convertir a segundos
a = float(input("Introduce las horas: "))
b = float(input("Introduce los minutos: "))
c = float(input("Introduce los segundos: "))
horas = a * 3600
minutos = b * 60
segundos = horas + minutos + c
print("El total  en segundos es: ", segundos)

# Ejercicio 31 Porcentaje
hombres = float(input("Introduce el numero de hombres: "))
mujeres = float(input("Introduce el numero de mujeres: "))
total_hombre_mujeres = hombres + mujeres
print("El porcentaje de hombres es: ", (hombres / total_hombre_mujeres) * 100, "%")
print("El porcentaje de hombres es: ", (mujeres / total_hombre_mujeres) * 100, "%")

# Ejercicio 32 Determinar si un número es par o impar
valor = float(input("Introduce un número: "))
numero = valor % 2
if numero != 0:
    print(valor, "Es un numero impar")
else:
    print(valor, "Es un numero par")

# Ejercicio 33 Descuentos.
valorcompra = float(input("Introduce el importe de su compra: "))
if valorcompra <= 100:
    print("Lo sentimos su compra no tiene descuento")
    print("Debe pagar:", valorcompra, ". Gracias por comprar en nustro establecimiento.")
else:
    print("Su compra tiene descuento: ")
    descuento = valorcompra * 0.20
    pago = valorcompra - descuento
    print("Por su compra de:", valorcompra, "tiene un descuento de: ", descuento)
    print("Debe pagar: ", pago, ".Gracias por comprar en nustro establecimiento.")

# Ejercicio 34: Leer dos numeros. Si son iguales que los multiplique
# si el primero es mayor que el segundo que los reste y si no que
# los sume. Concepto de condicional anidado
numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce un número: "))
if numero1 == numero2:
    print("Los números son iguales")
    print("La multiplicación de los números es:", numero1 * numero2)
else:
    if numero1 > numero2:
        print("El ", numero1, " es mayor que ", numero2)
        print("La resta de los números es:", numero1 - numero2)
    else:
        print("El ", numero1, " es menor que ", numero2)
        print("La suma de los números es: ", numero1 + numero2)
print("Se ha terminado el programa. Gracias")

# Ejercicio 35
# Aniversario y decadas.
# Documento 026 Ejercicio de condicionales video 36
# Ejercicio: Elaborar un programa que muestre el significado de aniversario de cada decada hasta los 60
# Bodas de hojalata        10 años
# Bodas de Porcelana       20 años
# Bodas de Perlas          30 años
# Bodas de Rubí            40 años
# Bodas de oro             50 años
# Bodas de diamante        60 años

decadas = float(input("Teclea el año de su boda: "))
fecha = 2019 - decadas

if fecha > 60 or fecha < 10:
    print("No tenemos aniversario para esas fechas.")
elif 10 <= fecha < 20:
    print("Te corresponden bodas de hojalata. ")
elif 20 <= fecha < 30:
    print("Te corresponden bodas de Porcelana. ")
elif 30 <= fecha < 40:
    print("Te corresponden bodas de Perlas. ")
elif 40 <= fecha < 50:
    print("Te corresponden bodas de Rubi ")
elif 50 <= fecha < 60:
    print("Te corresponden bodas de Oro.")
elif 60 <= fecha < 70:
    print("Te corresponden bodas de Diamantes.")
else:
    print("Te corresponden bodas de Platino. ")

# Ejercicio 36
# Documento 023 Ejercicio de condicionales
# Ejercicio: Leer tres numeros diferentes e imprimir el mayor de los tres.
a = float(input("Teclea el primer numero: "))
b = float(input("Teclea el segundo numero: "))
c = float(input("Teclea el tercer numero: "))
if a > b and a > c:
    print("El número mayor es: ", a)
elif b > a and b > c:
    print("El mayor es: ", b)
else:
    print("El mayor es: ", c)

# Ejercicio 37
# Documento 024 Ejercicio de condicionales
# Ejercicio: Una frutería oferta manzanas según la siguiente oferta.
# 0-2 kg        0 % descuento
# 2.01-5 kg     10% descuento
# 5.01-10 kg    15% descuento
# 10.01 - mas   20% descuento
precio = 2.5
kilos = float(input("Teclea la cantidad en kg de su compra: "))
if 0 <= kilos <= 2:
    print("Su compra no tiene descuento. Gracias.")
    pagar1 = kilos * precio
    print("\nEl importe de su compra es: ", pagar1)
elif 2.01 <= kilos <= 5:
    print("Su compra tiene descuento del 10 por cien. Gracias.")
    pagar2 = kilos * precio * 0.9
    print("\nEl importe de su compra es: ", pagar2)
elif 5.01 <= kilos <= 10:
    print("Su compra tiene descuento del 15 por cien. Gracias.")
    pagar3 = kilos * precio * 0.85
    print("\nEl importe de su compra es: ", pagar3)
else:
    print("Su compra tiene descuento del 20 por cien. Gracias.")
    pagar3 = kilos * precio * 0.8
    print("\nEl importe de su compra es: ", pagar3)

# Ejercicio 38
# Documento 025 Ejercicio de condicionales
# Ejercicio: Elaborar un programa que saque los días de la semana cuando se ingrese un número del 1 al 7
# 1 lunes
# 2 martes.... y así sucesivamente.
dia = int(input("Escribe un número entre 1 y 7: "))
if dia == 1:
    print(" El día elegido es lunes: ")
elif dia == 2:
    print(" El día elegido es martes: ")
elif dia == 3:
    print(" El día elegido es miércoles: ")
elif dia == 4:
    print(" El día elegido es jueves: ")
elif dia == 5:
    print(" El día elegido es viernes: ")
elif dia == 6:
    print(" El día elegido es sábado: ")
elif dia == 7:
    print(" El día elegido es Domingo: ")
else:
    print(" No hay día para número elegido. Gracias: ")

# Ejercicio 39
# Documento 029 Ejercicio de Estructuras Ciclicas (bucles)
# Tema bucles: Para...hasta...hacer
# Ejercicio: Calcular la suma de los N primeros numeros.
numeros = int(input("Teclea cuantos numeros deseas sumar"))
suma = 0
for item in range(numeros):
    suma = suma + item
print("La suma total es: ", suma)

# Ejercicio 40
# Documento 030 Ejercicio de Estructuras Ciclicas (bucles)
# // Tema bucles: Para...hasta...hacer
# // Ejercicio: Calcular la suma de los numero pares e impares por separado
# // desde el 1 hasta el 100 sin incluir el 100
sumapares = 0
sumaimpares = 0
for item in range(100):
    if item % 2 == 0:
        sumapares = sumapares + item
    else:
        sumaimpares = sumaimpares + item
print("La suma de los pares es: ", sumapares)
print("La suma de los impares es: ", sumaimpares)

# Ejercicio 41
# Documento 031 Ejercicio de Estructuras Ciclicas (bucles)
# Tema bucles: Para...hasta...hacer
# Ejercicio: Leer 10 numeros introducidos por teclado y calcular
# cuantos son positivos, cuantos negativos, y neutros. (+,-,0)
# Profesor Antonio Centeno
contar_pos = 0
contar_neg = 0
contar_neutros = 0
for item in range(10):
    numero1 = int(input("Teclea un numero: "))
    if numero1 == 0:
        contar_neutros += 1
    else:
        if numero1 > 0:
            contar_pos += 1
        else:
            contar_neg += 1
print("Los numeros positivos son: ", contar_pos)
print("Los numeros negativos son: ", contar_neg)
print("Los numeros neutros son: ", contar_neutros)

# Ejercicio 42
# Documento 032 Ejercicio de Estructuras Ciclicas (bucles)
# Ejercicio: Se tiene un conjunto de calificaciones de 10 alumnos.
# Realizar un algoritmo para calcular la media del grupo y la nota mas baja.
notasuma = 0
notamenor = 9999
for item in range(10):
    print(item, ".- Ingresa un numero")
    nota = int(input())
    notasuma = notasuma + nota
    if nota < notamenor:
        notamenor = nota
    else:
        print("veamos")
notapromedio = notasuma / 10
print("La media total es de:", notapromedio)
print("La nota menor es:", notamenor)

# Ejercicio43
# Factorial
factorial = 1
numero = int(input("Teclea el numero que desees como factorial: "))
while numero != 0:
    factorial = factorial * numero
    numero = numero - 1
print("El factorial de es: ", str(factorial))
