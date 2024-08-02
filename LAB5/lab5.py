import numpy as np
import math

def f(x):
    return (np.log(x)*(x-2)**2)

def df(x): #pochodna funkcji f
    return (1/x)*2*(x-2)

def df2(x): #druga pochodna funkcji f
    return ((-1)/(x**2))*2


def newt(x, f, df, df2, m_iter = 100):
    x0 = x
    wynik = []
    itr = 0
    while True:
        u_x = f(x)/df(x)
        du_x = 1 - (df2(x)/df(x))*u_x 
        x_next = x - u_x/du_x 
        t = abs(x_next - x)
        if t < 10e-6 or itr > m_iter:
            break
        itr = itr + 1
        wynik.append(x_next)
        x = x_next
    print("wynik:")
    print(wynik)
    print("liczba iteracji:")
    print(itr)


newt(0.5, f, df, df2)

def newt2(x, f, df, df2, m_iter = 100):
    x0 = x
    wynik = []
    itr = 0
    while True:
        x_next = x0 - 2*(f(x)/df(x))
        t = abs(x_next - x)
        if t < 10e-6 or itr > m_iter:
            break
        itr = itr + 1
        wynik.append(x_next)
        x0 = x_next
    print("wynik:")
    print(wynik)
    print("liczba iteracji:")
    print(itr)

newt2(0.5, f, df, df2)  
