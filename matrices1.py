#llenar una matriz de nxn con valores aleatorios en el rango 1 a 100

from random import randint #se encientra disponible en el modulo incorporado randint


n= input("introduce un numero para determinar el numero de filas y columnas")
def llenar_matriz (n):
    matriz =[]

    for i in range(n):  #i fila
        fila = []

        for j in range (n):  #j columna
            fila.append=(randint(0,9))
    matriz.append(fila)
print(fila)



