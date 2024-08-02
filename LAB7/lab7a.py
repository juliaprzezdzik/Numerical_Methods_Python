import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 1 / (1 + x**2)

def wyzM(xw, yw, n, alfa, beta):
    h = np.diff(xw)
    d = np.zeros(n)
    lam = np.zeros(n - 1)
    mi = np.zeros(n - 1)
    
    for i in range(1, n - 1):
        lam[i] = h[i] / (h[i] + h[i-1])
        mi[i] = 1 - lam[i]
        d[i] = 6 / (h[i] + h[i-1]) * ((yw[i+1] - yw[i]) / h[i] - (yw[i] - yw[i-1]) / h[i-1])
    
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    A[0, 0] = 1
    A[n-1, n-1] = 1
    b[0] = alfa
    b[n-1] = beta
    
    for i in range(1, n - 1):
        A[i, i-1] = mi[i]
        A[i, i] = 2
        A[i, i+1] = lam[i]
        b[i] = d[i]
    
    m = np.linalg.solve(A, b)
    return m

def wyzSx(xw, yw, m, x):
    n = len(xw) - 1
    h = np.diff(xw)
    for i in range(1, n+1):
        if xw[i-1] <= x <= xw[i]:
            A = (yw[i] - yw[i-1]) / h[i-1] - h[i-1] / 6 * (m[i] - m[i-1])
            B = yw[i-1] - m[i-1] * h[i-1]**2 / 6
            return m[i-1] * (xw[i] - x)**3 / (6 * h[i-1]) + m[i] * (x - xw[i-1])**3 / (6 * h[i-1]) + A * (x - xw[i-1]) + B

def interpolacja(xw, yw, alfa, beta, x_vals):
    n = len(xw)
    m = wyzM(xw, yw, n, alfa, beta)
    return [wyzSx(xw, yw, m, x) for x in x_vals]

def rysuj_wykres(xw, yw, f, n, alfa, beta):
    x_vals = np.linspace(-5, 5, 400)
    y_vals = f(x_vals)
    y_interpolowane = interpolacja(xw, yw, alfa, beta, x_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, color='pink')
    plt.plot(x_vals, y_interpolowane, color='violet', linestyle='--')
    plt.scatter(xw, yw, color='magenta', zorder=5)
    plt.title(f'Interpolacja dla n={n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['f(x)', 'Interpolacja'], loc='upper right')
    plt.grid(True)
    plt.show()

def drugie_pochodne_roznicowe(f, xw, dx):
    d2f_dx2 = []
    for x in xw:
        d2f_dx2.append((f(x - dx) - 2 * f(x) + f(x + dx)) / dx**2)
    return d2f_dx2

def porownaj_pochodne(xw, m, d2f_dx2):
    plt.figure(figsize=(10, 6))
    plt.plot(xw, m, color='pink')
    plt.plot(xw, d2f_dx2, color='magenta', linestyle='--')
    plt.scatter(xw, m, color='pink', zorder=5)
    plt.scatter(xw, d2f_dx2, color='pink', zorder=5)
    plt.title('Porównanie drugich pochodnych')
    plt.xlabel('x')
    plt.legend()
    plt.grid(True)
    plt.show()

n = 10
xw = np.linspace(-5, 5, n)
yw = f1(xw)
alfa = 0
beta = 0

m = wyzM(xw, yw, n, alfa, beta)

dx = 0.01
d2f_dx2 = drugie_pochodne_roznicowe(f1, xw, dx)

porownaj_pochodne(xw, m, d2f_dx2)
