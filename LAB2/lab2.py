import numpy as np
import math

n = 1000
m = 5

A = np.zeros((n,n)) #uwtorzenie macierzy A
for i in range(0,n):
    for j in range(0, n):
        if abs(i-j) <= m:
            A[i][j] = 1/(1+abs(i-j))
        else:
            A[i][j] = 0
print(A)

b = np.zeros(n) #utworzenie macierzy b 
for i in range(0, n):
    b[i] = i
print(b)

def naj_spadek(A,b,x, e = 1e-6): #funkcja obliczajaca najwiekszy spadek 
    x = np.zeros(n)
    r = b - np.dot(A,x)
    k = 0
    while math.sqrt(np.dot(r,r)) > e:
        alpha = np.dot(r,r) / np.dot(r, np.dot(A, r))
        x += alpha * r
        r = b - np.dot(A, x)
        k = k+1
        print(k) #wypisanie iteracji
        print(math.sqrt(np.dot(r,r))) #wypisanie normy euklidesowej wektora reszt
        print(alpha) #wypisywanie wartosci alpha
        print(math.sqrt(np.dot(x, x))) #wypisywanie normy euklidesowej wektora rozwiazan
    return r, x, k, alpha

#a x0 = 0
x0 = np.zeros(n)
spadek_1, x01, k1, alpha1 = naj_spadek(A,b,x0)
print(spadek_1, x01)
print("Liczba iteracji dla x0:")
print(k1)
print("Wartosc alpha1:")
print(alpha1)

#b x0 = 1
x1 = np.ones(n)
spadek_2, x11, k2, alpha2 = naj_spadek(A,b, x1)
print(spadek_2)
print(x11)
print("Liczba iteracji dla x1:")
print(k2)
print("Wartosc alpha2:")
print(alpha2)

