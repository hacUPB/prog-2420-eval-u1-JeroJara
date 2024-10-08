from random import randint
filas = 5
columnas = 12
Lista = []
#Creamos una lista vacía [[6,8,67],[4,7,12]]
for i in range(filas):        #Número de filas que tendrá la matriz (4)
    Lista.append([])      #Agregamos una fila vacía a la matriz
    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
        n = randint(31,195)
        Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente

def imprimir_m(List):
    filas = len(List)
    columnas = len(List[0])
    for fila in range(filas):
        print()
        for colum in range(columnas):
            print(f"|{List[fila][colum]:^1}|\t", end = '')
        print()
    return List

# Llamamos a la función con nuestra matriz de ejemplo
imprimir_m(Lista)

def mayordato(List):
    mayoresdatos = []
    for fila in range(len(List)):
        mayordatofila = max(List[fila])
        mayoresdatos.append(mayordatofila)
    mejordato = max(mayoresdatos)
    return mejordato

Listus = [[3,4,5],[2,67,8],[2,3,6]]
print(mayordato(Lista))












