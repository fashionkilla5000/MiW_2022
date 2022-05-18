import random as r

a = 0
b = 1
n = 1000

def funkcja(x):
    return x ** 2

def metoda_prostokatow(a,b,n,funkcja):
    s = 0
    dx = (b - a)/n

    for x in range(n):
        x = x * dx + a
        s += dx * funkcja(x)

    return s

def monte_carlo(a,b,n,funkcja):
    s = 0.
    dx = b - a

    for x in range(n):
        s += funkcja(a + r.uniform(0, dx))

    s *= dx/n
    return s

print(metoda_prostokatow(a,b,n,funkcja))
print(monte_carlo(a,b,n,funkcja))