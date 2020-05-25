# Ejercicio 12(La numeracion continua del archivo 002_A_001_Clase_Condicional_if)
print("Vamos a contar")
num = 40
while num <= 50:
    print("el número siguiente es: ", num)
    num = num + 1  # este es un contador. Se puede sustituir por (num +=1)

# Ejercicio 13
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")

# Ejercicio 14
print('Programa que suma los 10 primeros números naturales')
print('Cada suma parcial la muestra en pantalla')
Sum = 0
num = 1
while num < 11:
    Sum = num + Sum
    num = num + 1
    print('La suma es ' + str(Sum))

# Ejercicio 15
numero = int(input("¿Qué número quieres saber si es primo? "))

valor = range(2, numero)
contador = 0
for n in valor:
    if numero % n == 0:
        contador += 1
        print("divisor:", n)
if contador > 0:
    print("El número no es primo")
else:
    print("El número es primo")

# Ejercicio 16
m = 0
a = 2
while m <= 20:
    p = pow(a, m)
    print(p)
    m += 1

# Ejercicio 17
Sum = 0
num = 1
while num < 11:
    Sum = num + Sum
    num = num + 1
    print('La suma es ' + str(Sum))
