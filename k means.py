import math as m
import random as r


f = open("australian.dat","r")

lista = []
for x in f.readlines():
    tmp = x.split()
    lista.append(list(map(lambda e: float(e),tmp)))

print(lista)

def metryka_euklides(row1, row2):
    odleglosc = 0.0
    for i in range(len(row1) - 1):
        odleglosc += m.pow((row1[i] - row2[i]), 2)
    return m.sqrt(odleglosc)

kolumna_decyzyjna = 14
decyzje = []
for x in lista:
    decyzje.append(x[kolumna_decyzyjna])

unikalne_decyzje = list(set(decyzje))

nowe_decyzje = []

for x in lista:
    nowe_decyzje.append(x[:-1])

for x in nowe_decyzje:
    x.append(r.choice(unikalne_decyzje))

print(nowe_decyzje)

## jak obliczyć średnią wartość odległości?

tmp = []

for x in unikalne_decyzje:
    for y in lista:
        if x == y[kolumna_decyzyjna]:
            tmp.append(y)


    exit()

