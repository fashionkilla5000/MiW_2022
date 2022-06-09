import copy
import math as m
import random as r


f = open("australian.dat","r")

lista = []
for x in f.readlines():
    tmp = x.split()
    lista.append(list(map(lambda e: float(e),tmp)))

print('dataset:',lista)

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

print('unikalne decyzje:', unikalne_decyzje)

nowe_decyzje = []

for x in lista:
    nowe_decyzje.append(x[:-1])

for x in nowe_decyzje:
    x.append(r.choice(unikalne_decyzje))

print('dataset z nowymi decyzjami:')

for x in nowe_decyzje:
    print(x)


def znajdz_srodkowa(data):

    probka_odleglosci = []
    odleglosci = []
    for y in data:
        probka = y
        for x in data:
            if probka != x:
                odleglosci.append(metryka_euklides(probka,x))

        # for x in set_obliczone:
        #     print(x)
        # exit()
        probka_odleglosci.append([probka,sum(odleglosci)])
        #print(probka)
        #print(sum(odleglosci))

    minimum = min(probka_odleglosci, key=lambda x: x[1])
    #print(minimum)
    srodkowa = minimum[0]
    #print(srodkowa)
    return srodkowa


def pokoloruj(dataset,srodkowe):

    for y in srodkowe:
        dataset.remove(y)

    for probka in dataset:
        odleglosci = []
        print('-------------')
        print('probka przed')
        print(probka)
        for srodkowa in srodkowe:
            odleglosci.append([srodkowa[kolumna_decyzyjna],metryka_euklides(probka,srodkowa)])

        minimum = min(odleglosci, key=lambda x: x[1])

        probka[kolumna_decyzyjna] = minimum[0]
        print('odleglosci')
        print(odleglosci)
        print('probka')
        print(probka)

    for x in srodkowe:
        dataset.append(x)

    return dataset


for x in range(20):
    srodkowe = []
    for x in unikalne_decyzje:
        tablica = []
        for y in nowe_decyzje:
            if y[kolumna_decyzyjna] == x:
                tablica.append(y)

        srodkowe.append(znajdz_srodkowa(tablica))

    print('+++++++++++++++')
    print("srodkowe:")
    print(srodkowe)
    print('+++++++++++++++')
    nowe_decyzje = pokoloruj(nowe_decyzje,srodkowe)

print('---------------------')
print('dataset po algorytmie')
for x in nowe_decyzje:
    print(x)

exit()




## jak obliczyć średnią wartość odległości?

tmp = []

for x in unikalne_decyzje:
    for y in lista:
        if x == y[kolumna_decyzyjna]:
            tmp.append(y)


    exit()

