#N Reinas

def draw(array):
    n = len(array)
    print('%s+'%('+---'*n))
    for i in range(n):
        s = '|'
        for j in range(n):
            s += ' %c |' % ('Q' if array[j] == i else ' ')
        print(s)
        print('%s+'%('+---'*n))
# draw([0,1,2,3,4])

def isLegal(array, fila, columna):
    for i in range(columna):
        if array[i] == fila: # Misma fila
            return False
        distancia = columna - i
        if array[i] + distancia == fila or array[i] - distancia == fila: # Misma diagonal
            return False
    return True

def nqueensBT(n, columna, array):
        if columna < n:
            for fila in range(n):
                if isLegal(array, fila, columna):
                    array[columna] = fila
                    nqueensBT(n, columna + 1, array)
                    array[columna] = -1
        else:
            draw(array)
n = 4
nqueensBT(n, 0, [-1]*n)