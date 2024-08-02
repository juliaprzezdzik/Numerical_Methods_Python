import math 
import numpy as np

m = 4
D = np.zeros((m,m)) #macierz wspolczynnikow

kch = 5.92*10**2 
kcc = 15.8*10**2 
mh = 1 #amu, 1 amu = 1.6605*10^(-27) 
mc = 12 

D[0,0] = kch/mh
D[0,1] = -kch/mh
D[0,1] = -kch/mc
D[1,1] = (kch+kcc)/mc
D[1,2] = -kcc/mc
D[2,1] = -kcc/mc
D[2,2] = (kch+kcc)/mc
D[2,3] = -kch/mc
D[3,2] = -kch/mh
D[3,3] = kch/mh 

print(D)

def rozklad_qr(A, n):
    R = A
    Q = np.identity(n)
    for i in range(n-1):
        x = np.zeros(n)
        for j in range(n):
            if(j >= i):
                x[j] = R[j, i]
        e = np.zeros(n)
        e[i] = 1
        u = x - np.dot(np.linalg.norm(x, ord = 2), e)
        u_norm = np.linalg.norm(u, ord = 2)
        v = np.zeros(n)
        if(u_norm != 0):
            v = u/u_norm
        I = np.identity(n)
        Qt = I - np.dot(v, v )*2 
        Q = np.dot(Qt, Q)
        R = np.dot(Qt, R)
    QT = np.zeros((n,n))
    print("macierz Q:")
    for m in range(n):
         for p in range(n):
            QT[m][p] = Q[p][m]
    print(QT)
    print("\nmacierz R:")
    print(R)
    return Q, R  


rozklad_qr(D, m)
