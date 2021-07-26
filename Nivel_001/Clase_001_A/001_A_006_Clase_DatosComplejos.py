print()
print('****************************************************************************************')
print('          Tema: Generalidades del lenguaje Python')
print('          Lección: Datos complejos Tuplas')
print('          Profesor: Antonio Centeno')
print('****************************************************************************************\n')
print('****************************************************************************************')
print("""La Tupla es una variable que permite almacenar varios datos inmutables de tipos diferentes
y que no se permite modificarlos una vez que son creados.
Ejemplo: mi_tupla = ('pongo texto', 20, 2.89, 'otro dato', 30)
Se accede al contenido de la tupla asi: mi_tupla = [0], mi_tupla = [1], etc
****************************************************************************************""")
import math
mi_tupla = ('Primer texto', 11, 2.22, 'Tercer dato', 444)

print(mi_tupla[0])  # sacamos el primer elemento de la tupla
print(mi_tupla[1])  # sacamos el segundo elemento de la tupla
print(mi_tupla[2])  # sacamos el tercer elemento de la tupla
print(mi_tupla[3])  # sacamos el cuarto elemento de la tupla
print(mi_tupla[4])  # sacamos el quinto elemento de la tupla
print(mi_tupla[0:2])  # Extrae los 2 primeros elementos de la lista
print(mi_tupla[2:])  # Extrae desde el segundo hasta el final
print(mi_tupla[:2])  # Extrae hasta el segundo sin incluir.
print(mi_tupla[-1])  # Extrael primero empezando por el final de la tupla.
print(mi_tupla[-3])  # Extra el tercero empezando por el final.

mi_tupla = 4, 16, 25, 36, 49  # Los numeros van separados como en el ejemplo
mi_tupla1 = 'a', 'b', 'c', 'd'  # Las letras llevan todas las comillas por ser string
mi_tupla2 = mi_tupla + mi_tupla1
print (mi_tupla2)
print(mi_tupla*2)  # Lo que hace es duplicar la tupla.