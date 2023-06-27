import numpy as np
import matplotlib.pyplot as plt
from math import pi


def f(x):
    c = 1.0 / np.sqrt(2.0 * pi)
    d = np.exp(-x ** 2 / 2.0)
    return c * d


x = np.linspace(-4, 4, 1000)
y = f(x)

# plt.plot(x, y)
# plt.show()


def trapez(f, a, b, n):
    h = (b - a) / n
    I = (h / 2) * (f(a) + 2 * np.sum(f(a + i * h) for i in range(1, n)))
    return I


def Rich_trapez(f,a,b,n):
    int1 = trapez(f,a,b,n)
    int2 = trapez(f,a,b,2*n)
    int = 4.0/3 * int2 - 1.0/3 * int1
    return int


def Newton_Rich(f,x0,newtonit,richprec, solvefor):
    for i in range(1,newtonit+1):
        g = Rich_trapez(f,0,x0,richprec)-solvefor
        dg = f(x0)
        x0 = x0 - g/dg
    return(x0)

# print('trapiez test', trapez(f,0,2,20))
# print('trapiez test', Rich_trapez(f,0,2,20))
# print('95 pct fraktilen', Newton_Rich(f,1.0,100,100, 0.475))

#---------------------------------
#Richardason implementation fra s. 476

def phi(f, x, h):
    return 1/(2*h) * (f(x+h)-f(x-h))

def RichDiff(phi,x,h,M):
    M = M + 1 #Vi sørger for at M er antallet af Richardsson extrapolationer
    D = np.zeros(shape = (M,M), dtype=np.float64)
    for n in range(0,M):
        D[n,0] = phi(f,x,h/(2**n))
    for k in range(1,M):
        for n in range(k,M):
            D[n,k] = D[n,k-1]+(D[n,k-1]-D[n-1,k-1])/(4**k-1)
    return D[M-1,M-1]

#Programmeringsopgave 1 uge 7

def f(x):
    return np.exp(2*x)

q = RichDiff(phi, 1, 0.01, 2)
print(q)
print(np.exp(1)**2*2)

