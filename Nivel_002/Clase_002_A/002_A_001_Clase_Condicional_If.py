# Ejercicio 1
x = int(input("Teclea tu edad: "))  # int para convertir el string
if x < 18:
    print("Eres menor de edad")
else:
    print("Eres Mayor de edad")

# Ejercicio 02
x = input("Teclea 'verde' o 'rojo':")  # "x" guarda un string
if x == "verde":  # utilizamos el comparador de igualdad
    print("Cruza la calle")
else:
    print("Espera tu turno ")

# Ejercicio 04
y = int(input("Teclea el dinero que te ha costado la compra: "))
if y > 1000:
    print("Pagar con tarjeta de crédito")

# Ejercicio 05
x = int(input("Teclea un número para tu edad :"))  # "x" guarda un string convertido en numero
if x < 15:
    print("Eres un niño")
elif 18 > x >= 15:
    print("Eres un joven")
elif 30 > x >= 18:
    print("Eres un adulto")
elif 50 > x >= 30:
    print("Eres un experimentado")
elif 60 > x >= 50:
    print("Eres un experto")
elif 70 > x >= 60:
    print("Debes descansar en las Bahamas.")
else:
    print("Toma un libro y lee")

# Ejercicio 06 (Ejercicio igual que el anterior con anidamiento)

x = int(input("Teclea un número: "))  # "x" guarda un string convertido en número
y = input("Teclea 'm' si eres mujer, 'h' si eres hombre: ")  # "x" guarda un string
if x < 15:
    if y == "m":
        print(f"Eres una niña de: ", x, "años", end="")
    else:
        print(f"Eres un niño de: ", x, "años", end="")
    print("No juegues tanto a la videoconsola")
elif 18 > x >= 15:
    if y == "m":
        print(f"Eres una joven de: ", x, "años", end="")
    else:
        print(f"Eres un joven de: ", x, "años", end="")
    print("Sal un poco a bailar")
elif 30 > x >= 18:
    if y == "m":
        print(f"Eres una adulta de: ", x, "años", end="")
    else:
        print(f"Eres un adulto de: ", x, "años", end="")
    print("Debes formarte bien para ser un profesional.")
elif 50 > x >= 30:
    if y == "m":
        print(f"Eres una experimentada de: ", x, "años. ", end="")
    else:
        print(f"Eres un experimentado de: ", x, "años. ", end="")
    print("Con las responsabilidades no se juega.")
elif 60 > x >= 50:
    if y == "m":
        print(f"Eres una experta de: ", x, "años. ", end="")
    else:
        print(f"Eres un experto de: ", x, "años. ", end="")
    print("Cuida tus activos.")
elif 70 > x >= 60:
    if y == "m":
        print(f"Eres una mujer con: ", x, "años de recuerdos. ", end="")
    else:
        print(f"Eres un hombre con: ", x, "años de recuerdos. ", end="")
    print("Debes descansar en las Bahamas.")
else:
    if y == "m":
        print(f"Eres una mujer de: ", x, "años vividos con amor. ", end="")
    else:
        print(f"Eres un hombre de: ", x, "años vividos con amor. ", end="")
    print("Toma un libro, lee y disfruta")

# Ejercicio 07 (No se aconseja la utilizacion de varios if)
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
if edad >= 18:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")

# Ejercicio 08 (Una parte del bucle no se ejecuta-pass)
edad = int(input("¿Cuántos años tiene? "))
if edad < 120:
    pass  # Si no se quiere que se realice alguna parte del bucle
    print("¡No me lo creo!")
print(f"Usted dice que tiene {edad} años.")

# Ejercicio 09
print("Piense un número de 1 a 4.")
print("Conteste S (sí) o N (no) a mis preguntas.Uitlizando letras mayusculas")
primera = input("¿El número pensado es mayor que 2? ")
if primera == "S":
    segunda = input("¿El número pensado es mayor que 3? ")
    if segunda == "S":
        print("El número pensado es 4.")
    else:
        print("El número pensado es 3")
else:
    segunda = input("¿El número pensado es mayor que 1? ")
    if segunda == "S":
        print("El número pensado es 2.")
    else:
        print("El número pensado es 1.")
print("¡Hasta la próxima!")

# Ejercicio 10
numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print(f"{numero} es múltiplo de dos")
elif numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
else:
    print(f"{numero} no es múltiplo de dos")

# Ejercicio 11
numero = int(input("Escriba un número: "))
if numero % 2 != 0:
    print(f"{numero} es impar")
else:
    print(f"{numero} es par")
