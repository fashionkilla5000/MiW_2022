import numpy as np
import math as m
from numpy.linalg import inv

B = np.array([[1,1,1,1,1,1,1,1],
     [1,1,1,1,-1,-1,-1,-1],
     [1,1,-1,-1,0,0,0,0],
     [0,0,0,0,1,1,-1,-1],
     [1,-1,0,0,0,0,0,0],
     [0,0,1,-1,0,0,0,0],
     [0,0,0,0,1,-1,0,0],
     [0,0,0,0,0,0,1,-1]])

print(B)

def czyOrtogonalna(BBT):
    i, j = np.nonzero(BBT)
    return np.all(i == j)

print("czy ortogonalna?")
print(czyOrtogonalna(np.dot(B,B.transpose())))

def normalizuj_wektory(B):
     znormalizowaneB = []
     for x in range(len(B)):
          dlg = m.sqrt(np.dot(B[x], B[x]))
          znormalizowaneB.append(1 / dlg * B[x])

     return np.array(znormalizowaneB)

B = normalizuj_wektory(B)

print(B)

print("czy ortogonalna?")
print(np.dot(B,B.transpose()))
print(czyOrtogonalna(np.dot(B,B.transpose())))

print(np.eye(len(B)))

xa = np.array([[8,6,2,3,4,6,6,5]])

xa = normalizuj_wektory(xa)
print(xa)
print('-----')

xb = np.dot(B.transpose(),xa.transpose())
print(xb)




