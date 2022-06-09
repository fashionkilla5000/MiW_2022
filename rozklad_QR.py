import random as r
import numpy as np
import math as m
from numpy.linalg import inv

A = np.array([[0, 2], [2, 3]])


# A = np.transpose(A)


def obliczE(u):
    return u / (m.sqrt(np.dot(u, u)))


def obliczProj(v, u):
    return np.dot(np.dot(v, u) / np.dot(u, u), u)


def obliczU(v, proj):
    return v - proj


def RozkladQR(A):
    v1 = A[0]
    v2 = A[1]
    u1 = v1
    e1 = obliczE(u1)

    u2 = obliczU(v2, obliczProj(v2, u1))
    e2 = obliczE(u2)

    print("u1" + str(u1))
    print("e1" + str(e1))
    print("u2" + str(u2))
    print("e2" + str(e2))
    Q = np.concatenate(([e1], [e2]), axis=0)
    # Q = np.concatenate(([e1], [e2]), axis=0).transpose()
    print("Q", Q)
    R = np.dot(Q.transpose(), A)
    # R = np.dot(Q.transpose(), A)
    print("R", R)
    return Q,R


RozkladQR(A)



def obliczWartosciWlasne(A):

    for x in range(20):
        Q,R = RozkladQR(A)

        A = np.dot(R,Q)
        print('---------')
        print('A')
        print(A)

print(obliczWartosciWlasne(A))