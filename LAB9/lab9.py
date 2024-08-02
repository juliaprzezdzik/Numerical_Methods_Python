
import numpy as np

def f(x, y):
    return 5/2 * (x**2 - y)**2 + (1 - x)**2

def gradient(f, r, delta=1e-4):
    x, y = r
    df_dx = (f(x + delta, y) - f(x - delta, y)) / (2 * delta)
    df_dy = (f(x, y + delta) - f(x, y - delta)) / (2 * delta)
    return np.array([df_dx, df_dy])

def met(f, r0, h, epsilon, max_iter=1000):
    r = r0
    for i in range(max_iter):
        grad = gradient(f, r)
        r_next = r - h * grad
        if np.linalg.norm(r_next - r) < epsilon:
            break
        iter = i
        r = r_next
    print("liczba iteracji:", iter)
    return r

r0 = np.array([-0.75, 1.75])
h = 0.1

#a
eps1 = 10**(-2)
wynik1= met(f, r0, h, eps1)
print(wynik1)

#b 
eps2 = 10*(-3)
wynik2 = met(f, r0, h, eps2)
print(wynik2)

#nastepne zajecia: algorytm szybkiej transformaty fouriera - znalezc algorytm w bibliotece
