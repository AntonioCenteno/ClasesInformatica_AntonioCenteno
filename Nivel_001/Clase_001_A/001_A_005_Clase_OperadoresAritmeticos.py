print()
print('****************************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Ejercicios: Operadores Aritmeticos')
print('          Profesor: Antonio Centeno')
print('****************************************************************************************\n')
print('****************************************************************************************')
print(""" - Tabla de Operadores Aritméticos.
****************************************************************************************
Simbolo     Significado     Ejemplo         Resultado
+           Suma            a = 10 + 3      a es 15
-           Resta           a = 10 - 3      a es 7
-           Negación        a = -2          a es -2
*           Multiplicacion  a = 3 * 3       a es 9
**          Exponente       a = 2 ** 3      a es 8
/           División        a = 10 / 2      a es 5
//          Division entera a = 15.5 // 2   a es 7
%           Modulo          a = 27 % 4      a es 3""")
print("""\nEl alumno realizará un programa con cada uno de los operadores aritméticos.
Pedirá por pantalla los datos y evaluara las operaciones con enter.""")
print('****************************************************************************************\n')
print('****************************************************************************************')
print("""5- Calcular los intereses anuales que produce un banco.
Pedir por pantalla el Capital, el tiempo y el redito.""")
print('****************************************************************************************\n')

capital = int(input("Teclea el capital a imponer en el banco: "))
redito = float(input("Teclea el redito en decimal: "))
tiempo = int(input("Teclea el tiempo en años: "))
interes = capital * (redito * tiempo)
print('Los intereses producidos son: ', end="")
print(round(interes, 3), end=""); print(' €')