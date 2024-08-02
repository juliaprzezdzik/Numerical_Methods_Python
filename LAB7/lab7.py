import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 1 / (1 + x**2)

def f2(x):
    return np.cos(2 * x)

def wyzM(xw, yw, n, alfa, beta):
    h = np.diff(xw)
    d = np.zeros(n + 1)
    lam = np.zeros(n)
    mi = np.zeros(n)
    
    for i in range(1, n):
        lam[i] = h[i] / (h[i] + h[i-1])
        mi[i] = 1 - lam[i]
        d[i] = 6 / (h[i] + h[i-1]) * ((yw[i+1] - yw[i]) / h[i] - (yw[i] - yw[i-1]) / h[i-1])
    
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)
    
    A[0, 0] = 1
    A[n, n] = 1
    b[0] = alfa
    b[n] = beta
    
    for i in range(1, n):
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
    n = len(xw) - 1
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
    plt.legend()
    plt.grid(True)
    plt.show()

for n in [5, 8, 21]:
    xw = np.linspace(-5, 5, n)
    yw = f1(xw)
    rysuj_wykres(xw, yw, f1, n, 0, 0)

    yw = f2(xw)
    rysuj_wykres(xw, yw, f2, n, 0, 0)
