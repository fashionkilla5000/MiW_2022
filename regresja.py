import random as r
import numpy as np
from numpy.linalg import inv

x = np.array([0, 1, 2, 3, 4, 5])

y = np.array([1, 2, 3, 3, 4, 5])


def srednia(x):
    s = np.dot(x, np.ones(len(x)))
    s = s * (1 / len(x))

    return s


def odchylenie(x):
    s = x - (srednia(x) * np.ones(len(x)))
    s = np.transpose(s) * s
    s = s * (1 / len(x))
    return s


print(srednia(x))
print(odchylenie(x))

def regresja(x, y):

    x = np.concatenate(([np.ones(len(x))],[x]),axis=0).transpose()

    xTx = np.dot(x.transpose(),x)
    xTy = np.dot(x.transpose(),y)

    B = np.dot(inv(xTx),xTy)

    print('y=',B[0],'+',B[1],'x')



print(regresja(x, y))