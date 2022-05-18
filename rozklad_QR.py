import random as r
import numpy as np
import math as m

A = np.array([[1, 1, 0], [0, 1, 1]])
A = np.transpose(A)


def obliczE(u):
    return u / (m.sqrt(np.dot(u, u)))


def obliczProj(v, u):
    return np.dot(np.dot(v, u) / np.dot(u, u), u)


def obliczU(v, proj):
    return v - proj


def RozkladQR(A):
    v1 = A[:, 0]
    v2 = A[:, 1]
    u1 = v1
    e1 = obliczE(u1)

    u2 = obliczU(v2, obliczProj(v2, u1))
    e2 = obliczE(u2)

    print("u1" + str(u1))
    print("e1" + str(e1))
    print("u2" + str(u2))
    print("e2" + str(e2))
    Q = np.concatenate(([e1], [e2]), axis=0).transpose()
    print("Q", Q)
    R = np.dot(Q.transpose(), A)
    print("R", R)

    print(np.dot(np.dot(Q.transpose(), A), Q.transpose()))


print(RozkladQR(A))