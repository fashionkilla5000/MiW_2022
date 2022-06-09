import math as m

f = open("australian.dat","r")

lista = []
for x in f.readlines():
    tmp = x.split()
    lista.append(list(map(lambda e: float(e),tmp)))

print('lista:',lista)

def metryka_euklides(row1, row2):
    odleglosc = 0.0
    for i in range(len(row1) - 1):
        odleglosc += m.pow((row1[i] - row2[i]), 2)
    return m.sqrt(odleglosc)

row1 = list(map(float, input("podaj wiersz: ").split()))
print("podane: ",row1)

k = int(input("Podaj k: "))


def knn(row1,k):
    odl = []
    for x in range(len(lista) - 1):
        odl.append((lista[x][-1], metryka_euklides(row1, lista[x])))

    posortowane = sorted(odl, key=lambda odleglosc: odleglosc[1])

    k_posortowane = posortowane[:k]

    print('posortowane k odleglosci:',k_posortowane)

    slownik = {}
    for x in k_posortowane:
        if x[0] not in slownik:
            slownik[x[0]] = [x[1]]
        else:
            slownik[x[0]] += [x[1]]

    print('slownik odleglosci dla decyzji',slownik)

    for key, value in slownik.items():
        slownik[key] = sum(value)

    print('suma odl dla decyzji',slownik)

    return min(slownik, key=slownik.get)

print('Decyzja:')
print(knn(row1, k))

exit()
odl = []
for x in range(len(lista)-1):
    odl.append((lista[x][-1],metryka_euklides(row1,lista[x])))

posortowane = sorted(odl, key=lambda odleglosc: odleglosc[1])

k_posortowane = posortowane[:k]

print(k_posortowane)

slownik = {}
for x in k_posortowane:
    if x[0] not in slownik:
        slownik[x[0]] = [x[1]]
    else:
        slownik[x[0]] += [x[1]]

obliczone = []
for key, value in slownik.items():
    obliczone.append((key, sum(value)))

print(obliczone)

