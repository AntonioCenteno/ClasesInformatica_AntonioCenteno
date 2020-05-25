# Ejercicio 18(La numeracion continua del archivo 002_A_002_Clase_Condicional_While)
lista_nombres = ["Magallanes", "Pizarro", "Hernán Cortes", "Valdivia", "Balboa"]
for item in lista_nombres:
    print(item)

# Ejercicio 19
lista_planetas = ("Mercurio", "Venus", "Plutón", "Urano", "Tierra", "Júpiter", "Marte")
for planeta in lista_planetas:
    print(planeta)

# Ejercicio 20a
for numero in range(45, 56):
    print("El numero", str(numero), "tiene premio")

# Ejercicio 20b
for x in range(10):
    print(x)

# Ejercicio 21
lista_nombres = ["Magallanes", "Pizarro", "Hernán Cortes", "Valdivia", "Balboa"]
for item in lista_nombres:
    print(item, " tiene: ", len(item), " letras")

# Ejercicio 22

letra = "Python"
for item in letra:
    print(item)
letra = "Python"
for item in letra:
    print(item, item, item, item, item, item)
letra = "Python"
for item in letra:
    print(item, item * 10)
letra = "Python"
for item in letra:
    print((item + item) * 20)
