import random as r
import numpy as np
import math as m
from numpy.linalg import inv

# A = np.array([[0, 2, 3], [2, 3, 3], [1, 2, 3]])
# A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
A = np.array([[0,2],[2,3]])

def obliczE(u):
    return u / (m.sqrt(np.dot(u, u)))


def obliczProj(v, u):
    return np.dot(np.dot(v, u) / np.dot(u, u), u)


def obliczU(v, proj):
    return v - proj


def RozkladQR(A):

    u = []
    e = []
    u.append(A[0])
    e.append(obliczE(u[0]))
    for v in range(1,len(A)):
        u.append(obliczU(A[v],obliczProj(A[v],u[v-1])))
        e.append(obliczE(u[v]))



    Q = np.array(e)

    print("Q", Q)
    R = np.dot(Q.transpose(), A)

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