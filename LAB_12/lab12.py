import numpy as np
from scipy.special import roots_legendre, roots_laguerre, roots_hermite
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt

#zad 1
def f1(x):
    return x/(4*x**2 + 1)

def dok_wart_f1(x):
    return 1/8*np.log(np.abs(4*2**2+1)) - 1/8

def kw_gauss_legendre(f, a, b, n):
    wezly, wagi = roots_legendre(n) 
    nowe_wezly = 0.5 * (wezly + 1) * (b-a)+a 
    nowe_wagi = 0.5*(b - a)*wagi
    return np.sum(nowe_wezly + f(nowe_wagi))

a = 0
b = 2
wartosci_n = range(2,20)
for n in wartosci_n:
    kw_gauss_legendre(f1, 0, 2, n)

x_val = np.linspace(0, 2, 400)
y_val =f1(x_val)

plt.figure(figsize=(10, 6))
plt.plot(x_val, y_val, label=r'$\frac{x}{4x^2 + 1}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

#zad 2
def f2(x, k):
    if x == 0:
        return 0
    else:
        return x**k * np.exp(-x)

def kw_gauss_laguerre(func, k, n):
    nodes, weights = roots_laguerre(n)
    return np.sum(weights * func(nodes, k))

#zad 3 
    
def f3(x,y):
    return (np.sin(x))**2*(np.sin(y)**4)*np.exp(-x**2-y**2)

c_dok = 0.1919832644

def kw_gauss_hermite(f, a, b, n):
    wezly,wagi = roots_hermite(n)
    p = 0.0
    for i in range(n):
        for j in range(n):
            p += wagi[i] * wezly[j] * f(wezly[i], wezly[j])
    return p

wartosci_n = range(2,15)
for n in wartosci_n:
    kw_gauss_hermite(f2, 0, 2, n)
