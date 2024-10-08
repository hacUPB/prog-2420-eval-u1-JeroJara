Matriz = [[1,4,6,8,3],[8,9,12,54,47],[98,45,78,3,10]]
print(Matriz[0][4] + Matriz[2][0])
Matriz[2][4] = 50

print(Matriz[1])

##Generar los índices para recorrer la matriz
for i in range(3): 
    for j in range(5):
        print(f"Fila {i} Columna {j}")
        #matriz ij es contenido de l amtriz en ese lgugar
        Matriz[i][j] = Matriz[i][j]*2
print(Matriz)

#El for interno se reinicia cada vez que el externo vuelve a empezar

#Esta no es la forma correcta de crear una matriz
a = [0]*5
Matrix = [a]*3
print(Matrix)
Matrix[2][4] = 100
print(Matrix)
