import math  # Debemos importar el modulo de math para poder operar
print()
print('****************************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Tipos basicos')
print('          Profesor: Antonio Centeno')
print('****************************************************************************************\n')

print('****************************************************************************************')
print("""3- Escribe un programa que realice las siguientes operaciones con los tipos estudiados.
Pedira los tipos por pantalla para que el usuario pueda introducirlos y luego operará.
Operaciones: Suma, resta, multiplicación, división, Raíz, Potencia.
Tipos: int, float, complex, char, bool, str""")
print('****************************************************************************************\n')

print('****************************************************************************************')
print('Tipos basicos: int()')
print('****************************************************************************************\n')
numero1 = int(input("Teclea primer numero:"))
numero2 = int(input("Teclea segundo numero:"))
print('La suma es: ', end="")
print(round((numero1 + numero2), 3))
print('La resta es: ', end="")
print(round((numero1 - numero2), 3))
print('La multiplicacion es: ', end="")
print(round((numero1 * numero2), 3))
print('La division es:', end="")
print(round((numero1 / numero2), 3))

numero11 = float(input("\nIngrese numero para hallar la raiz cuadrada: "))
raiz = math.sqrt(numero11)
print(raiz)

print('\nRealizacion de potencia de números reales')
base = float(input("Ingrese la base: "))
potencia = float(input("Ingrese la potencia: "))
resultado = math.pow(base, potencia)
print(resultado)

print('\n****************************************************************************************')
print('Tipos basicos: float')
print('****************************************************************************************')

num1 = float(input('Teclea primer numero: '))
num2 = float(input('Teclea segundo numero: '))
print('La suma es: ', end="")
print(round((num1 + num2), 5))
print('La resta es:', end="")
print(round((num1 - num2), 5))
print('La multiplicacion es: ', end="")
print(round((num1 * num2), 5))
print('La division es: ', end="")
print(round((num1 / num2), 5))

num13 = float(input("\nIngrese numero para hallar la raiz cuadrada: "))
raiz = math.sqrt(num13)
print(raiz)

print('\nRealizacion de potencia de números reales')
base = float(input("Ingrese la base: "))
potencia = float(input("Ingrese la potencia: "))
resultado = math.pow(base, potencia)
print(resultado)

print('\n****************************************************************************************')
print('Tipos basicos: Operaciones con numeros complejos')
print('****************************************************************************************')

primer_complejo = complex(input("Dígame una numero: "))
segundo_complejo = complex(input("Dígame una numero: "))

solucion1 = (primer_complejo + segundo_complejo)
solucion2 = (primer_complejo - segundo_complejo)
solucion3 = (primer_complejo * segundo_complejo)
solucion4 = (primer_complejo / segundo_complejo)

print('La suma es:', end="")
print(solucion1)
print('La resta es:', end="")
print(solucion2)
print('La multiplicación es:', end="")
print(solucion3)
print('La division es:', end="")
print(solucion4)

print('\n****************************************************************************************')
print('Tipos basicos: Char() ')
print('****************************************************************************************')

print('Char nos muestra el carácter 35 de la tabla ASCII  ', end="")
print(chr(35))

print('\n****************************************************************************************')
print('Tipos basicos: bool() ')
print('****************************************************************************************')

aa = True
bb = False
print(aa)
print(bb)

print('\n****************************************************************************************')
print('Tipos basicos: str() ')
print('****************************************************************************************')

print('\nCadena asignada a una variable de una sola linea')
Primera_cadena = input("Teclea tu nombre:")
print(f"Bienvenido, {Primera_cadena}, al curso de Python")
