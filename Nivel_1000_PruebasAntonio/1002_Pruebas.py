# Ejercicio 17

def infobasica (nombre,*estudios,**mejor_nota):
    idx=0
    print(nombre)
    for item in estudios:
        print(item,sep="y")
    for item in mejor_nota:
        print(estudios[0][idx],"",item,mejor_nota[item])
        idx = idx + 1

infobasica("Ana",["Matmematicas: ","Fisica: "],Calculo_Infinitesimal = '10',Fisica_Cuantica ='9')

