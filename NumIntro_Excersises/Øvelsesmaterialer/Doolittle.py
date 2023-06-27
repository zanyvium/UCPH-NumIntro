import numpy as np

n=3
A=np.array([[60,30,20],[30,20,15],[20,15,12]])
U=np.zeros(shape=(n,n))
L=np.zeros(shape=(n,n))

for k in range(0,n):
    L[k][k] = 1.0
    if k == 0:
        for j in range(k, n):
           U[k][j]=A[k][j]
    else:
        for j in range(k,n):
            sum = 0.0
            for s in range(0,k):
              sum += L[k][s]*U[s][j]
            U[k][j]=A[k][j]-sum

    if k == 0:
        for i in range(k, n):
           L[i][k]=A[i][k]/U[k][k]
    else:
        for i in range(k+1,n):
            sum = 0.0
            for s in range(0,k):
              sum += L[i][s]*U[s][k]
            L[i][k]=(A[k][i]-sum)/U[k][k]

print(U)
print(L)
