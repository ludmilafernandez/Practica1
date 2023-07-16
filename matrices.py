"""matriz(array, arreglo) colección o conjunto de elementos 
formada por filas y columnas"""

#.......MATRIZ UNIDIMENSIONAL (6) -VERTICAL......
for i in range(1,7):
    print (i)

print ('\n')  # salto de linea


#......MATRIZ UNIDIMENSIONAL (6) -HORIZONTAL......
for i in range(1,7):
    print (i, end=' ') #se imprimirá un espacio en blanco después de cada elemento

print ('\n')


#......MATRIZ BIDIMENSIONAL (6 X 6) ......
#for anidado

for i in range(1,7):       #para elemento "i" del rango 1,7 
    for j in range (1,7):  #imprima todos los elementos"j" del rango 1,7
        print (0, end='  ')   
    print ('')
print ('\n')

for i in range(1,7):       #para elemento "i" del rango 1,7 
    for j in range (1,7):  #imprima todos los elementos"j" del rango 1,7
        print (f'({i}, {j})', end='  ')   
    print ('')
print ('\n')
    """ print (f'({i}, {j})', end='  ') imprimirá los valores de i y
      j entre paréntesis, separados por una coma, 
      y luego añadirá dos espacios adicionales al final. P"""

#ejercicio 1: colocar 1  en la diagonal
for i in range(1,7):       #para elemento "i" del rango 1,7 
    for j in range (1,7):  #imprima todos los elementos"j" del rango 1,7
        if (i==j):
          print (1, end='  ')   
        else:
          print (0, end='  ')  
    print ('')
print ('\n')


#ejercicio 2: colocar 1, 2. 3 etc segun coincida el numero en el vertice 
for i in range(1,7):       #para elemento "i" del rango 1,7 
    for j in range (1,7):  #imprima todos los elementos"j" del rango 1,7
        if (i==1 and j==1):
          print (1, end='  ')   
        elif (i==2 and j==2):
            print (2, end='  ')  
        elif (i==3 and j==3):
          print (3, end='  ')   
        elif (i==4 and j==4):
            print (4, end='  ')  
        elif (i==5 and j==5):
          print (5, end='  ')   
        elif (i==6 and j==6):
            print (6, end='  ')  
        else:
          print (0, end='  ')  
    print ('')
print ('\n')

#otra forma de hacer matrices
matrix= [[1,2,3],
         [4,5,6],
         [7,8,9]]

print ("mostrar todos los elementos de la matriz fila por fila")
for row in matrix:
   print (row)

print("mostrar todos los elementos matriz elemento a elemnto en columna")
for row in matrix:
   for element in row:
      print (element)

print("mostrar todos los elementos matriz en formato de matiz")
for row in matrix:
   for element in row:
      print (element, end=' ')
   print('')


   """MATRIZ GENERADA POR EL TECLADO, PREG AL USUARIO
   ¿Cuántas filas tendrá la matriz?
   ¿Cuántas columnas tendrá la matriz?
   Introdiçuce un elemento a la fila 0:"""

rows=int(input ("¿Cuántas filas tendrá la matriz?: ")) #int valor de tipo entero
columns= int(input ("¿Cuántas columnas tendrá la matriz?: ")) 
matrix= []

for row_position in range (rows):     #se le asigna una variable a este ciglo. es importante porq va a ir recorriendo
    row= []                                      #fila por fila 
    for element in range (columns):
       row.append(int(input(f"introduce un elemento a la fila {row_position}: ")))     #append arregas elementos a la lista, y el row position 
    matrix.append (row)                                                               #va diciendo la posicion del numero a ingresar

for row in matrix:
   print(row)

