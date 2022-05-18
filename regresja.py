import random as r
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
X = np.array([[2, 5, 7, 8], [1, 1, 1, 1]])
Y = np.array([1, 2, 3, 3])


def srednia(x):
    s = np.dot(x, np.ones(len(x)))
    s = s * (1 / len(x))

    return s


def odchylenie(x):
    s = x - (srednia(x) * np.ones(len(x)))
    s = np.transpose(s) * s
    s = s * (1 / len(x))
    return s


# print(srednia(x))
# print(odchylenie(x))

def regresja(X, Y):
    x = np.append(X, [1, 1, 1, 1])
    print(x)
    # xTx =


print(regresja(X, Y))