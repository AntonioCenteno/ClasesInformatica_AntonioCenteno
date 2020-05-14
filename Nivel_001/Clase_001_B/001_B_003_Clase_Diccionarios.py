
# Ejemplo 1 Diccionarios (Sintaxis de un diccionario)

diccionario = {'Clave1': 'Valor1', 'Clave2': 'Valor2', 'Clave3': ['Val30', 'Val31', 'Val32']}

# Ejemplo 2 Diccionarios (Acceder a un diccionario mediante clave)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
print ('El valor es:',diccionario['nombre']) #Pedro
print ('El valor es:',diccionario['edad'])   #45
print ('El valor es:',diccionario['cursos']) #['Frances','Alemán','Chino']

# Ejemplo 3 Diccionarios (Acceder a un lista dentro de un diccionario mediante indices)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
print ('El valor es:',diccionario['cursos'] [0]) #francés
print ('El valor es:',diccionario['cursos'] [1]) #alemán
print ('El valor es:',diccionario['cursos'] [2]) #chino

# Ejemplo 4 Diccionarios (Recorrer un diccionario con for)

for key in diccionario:
  print ('El valor es:',key, ":", diccionario[key])
#  nombre : Pedro
#  edad : 45
#  cursos : ['Frances', 'Alemán', 'Chino']

# Ejemplo 5 Diccionarios (Reconocer si tenemos una clave en el diccionario)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
f = 'nombre' in diccionario
print ('El valor es:',f)  # Respuesta true

# Ejemplo 5 Diccionarios (Cambiar el valor de una clave)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
diccionario ['nombre'] = 'Antonio'
print ('El valor es:',diccionario) # {'nombre': 'Antonio', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}

# Ejemplo 6 Diccionarios (Añadir datos a un diccionario)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
diccionario ['frutas'] = 'manzana'
print ('El valor es:',diccionario)
# {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino'], 'frutas': 'manzana'}

# Ejemplo 7 Diccionarios (Saber si tenermos cierta clave en diccionario)

diccionario = {'nombre': 'Pedro', 'edad': 45, 'cursos': ['Frances', 'Alemán', 'Chino']}
m = 'edad' in diccionario
print('El valor es:',m)  # True

m = 'Torre' in diccionario
print('El valor es:',m)  # False

# Ejemplo 8 Diccionarios (Crear diccionarios vacios)

Diccionario1 = {} #Crea un diccionario vacío