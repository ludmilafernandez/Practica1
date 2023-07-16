#llenar una matriz de nxn con valores aleatorios en el rango 1 a 100

from random import randint #se encientra disponible en el modulo incorporado randint

n = int(input("Introduce un número para determinar el numero de filas y columnas: ")) 

def llenar_matriz(n):
    matriz =[]

    for i in range(n):  #i fila
        fila = []

        for j in range (n):  #j columna
            fila.append(randint(0,9)) #por cada elemento llenar la fina con numeros aleatorios
        matriz.append(fila) #por cada 

    return matriz


resultado = llenar_matriz (n)

for fila in resultado:  #esto es para imprimir en forma de matrix
    for i in fila:
        print (i, end='  ')
    print('')

matriz= resultado

suma_filas =[]
suma_columnas = []
for i in matriz:
    suma_filas.append(sum(i))

print ("La suma de cada fila es ", suma_filas)

for j in matriz:
    suma_columnas.append (sum(j))

print ("La suma de cada columna es", suma_columnas)
