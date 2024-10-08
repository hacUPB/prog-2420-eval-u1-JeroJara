from random import randint
#Crear una matriz correctamente
def crea_matriz (filas:int, columnas:int, lim_inf:int,lim_superior:int):
    Lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
    for i in range(filas):        #Número de filas que tendrá la matriz (4)
        Lista.append([])      #Agregamos una fila vacía a la matriz
        for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
            n = randint(lim_inf,lim_superior)
            Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente
    return Lista      #Devolvemos la matriz creada

def imprim_matriz(Lista:list):
#imprimir el contenido de la matriz como una tabla
    for f in range(filas):
        print('|', end = ' ')
        for c in range(columnas):
            print(f"{Lista[f][c]:^6}|",end=' ') #deja espacio para 5 enteros
        print()


filas = 5
columnas = 12
Matriz = crea_matriz(filas,columnas,31,195)

imprim_matriz(Matriz)

##¿En qué año y mes se produjo la mayor venta?