"""
Mochila de 15 kg, metemos objetos a las mochilas con valores asociados
meter una cantidad de objetos dentro de la mochila y que sus valores sea la mayor posible
"""

def actSol(objetosP, objetosV, arrMochila, valores):
    pesos = 0
    value = 0
    for i in range(len(arrMochila)):
        if arrMochila[i] == 1:
            pesos += objetosP[i]

    if pesos > 15:
        return 'mochila muy pesada'

    for i in range(len(arrMochila)):
        if arrMochila[i] == 1:
            value += objetosV[i]

    if value > valores:
        for i in range(len(arrMochila)):
            if arrMochila[i] == 1:
                arrVal[i] = objetosP[i]
    return arrVal, value

def mochila(objetosP, objetosV, estado, arrMochila, valores):
    if estado == len(arrMochila):
        print(arrMochila)
        return
    else:
        arrMochila[estado] = 0
        mochila(objetosP, objetosV, estado + 1, arrMochila, valores)
        print(actSol(objetosP, objetosV, arrMochila,valores))

        arrMochila[estado] = 1
        mochila(objetosP, objetosV, estado + 1, arrMochila, valores)
        print(actSol(objetosP, objetosV, arrMochila, valores))

    print('\n')
    return arrVal, val

objetosP = [12, 2, 1, 1, 4]
objetosV = [4, 2, 1, 2, 10]
arrVal = [0]*len(objetosP)
valores = 0
val = 0
arrMochila = [-1]*len(objetosP)
# print(mochila(objetosP, objetosV, 0, arrMochila, valores))

# second solution

def valido(solucion, etapa, objetos):
    peso_total = 0
    for i in range(etapa):
        if solucion[i] == 1:
            peso_total += objetos[i].peso
    if peso_total > 15:
        return False
    return True

def actualizarSolucion(solucion, objetos, mochila_final, peso_final, benef_final):
    benef_total = 0
    peso_total = 0
    for i in range(len(mochila_final)-1):
        if solucion[i] == 1:
            benef_total += objetos[i].valor
            peso_total += objetos[i].peso
    
    if benef_total > benef_final:
        for i in range(len(mochila_final)-1):
            mochila_final[i] = solucion[i]
        benef_final = benef_total
        peso_final = peso_total

def mochilaRec(solucion, etapa, objetos, mochila_final, peso_final, benef_final):
    i = 0
    if etapa > len(mochila_final)-1:
        return
    while solucion[etapa] != 1:
        solucion[etapa] = i
        if valido(solucion, etapa, objetos):
            if etapa == len(mochila_final)-1:
                actualizarSolucion(solucion, objetos, mochila_final, peso_final, benef_final)
            else:
                mochilaRec(solucion, etapa + 1, objetos, mochila_final, peso_final, benef_final)
        i += 1
    solucion[etapa] = -1
    return print(solucion)

n = 4
capacidadM = 15
class objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

Olist = []
obj1 = objeto(12, 4)
obj2 = objeto(2, 2)
obj3 = objeto(1, 1)
obj4 = objeto(1, 2)
obj5 = objeto(4, 10)

Olist.append(obj1)
Olist.append(obj2)
Olist.append(obj3)
Olist.append(obj4)
Olist.append(obj5)

solucion_final, mochila_final = [-1]*5, [-1]*5

# mochilaRec(solucion_final, 0, Olist, mochila_final, 0, 0)


