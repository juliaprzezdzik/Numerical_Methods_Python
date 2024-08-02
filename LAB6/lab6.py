import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def generate_uniform_nodes(a, b, n):
    return np.linspace(a, b, n+1)

def generate_chebyshev_nodes(a, b, n):
    nodes = []
    for m in range(n+1):
        node = 0.5 * ((a + b) + (b - a) * np.cos(np.pi * (2*m + 1) / (2*n + 2)))
        nodes.append(node)
    return np.array(nodes)

a, b = -5, 5
n_values = [5, 10, 15, 20]

x_plot = np.linspace(a, b, 1000)
for n in n_values:
    x_uniform = generate_uniform_nodes(a, b, n)
    y_uniform = f(x_uniform)
    y_uniform_interp = [lagrange_interpolation(x, x_uniform, y_uniform) for x in x_plot]
    x_chebyshev = generate_chebyshev_nodes(a, b, n)
    y_chebyshev = f(x_chebyshev)
    y_chebyshev_interp = [lagrange_interpolation(x, x_chebyshev, y_chebyshev) for x in x_plot]
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(x_plot, f(x_plot), 'violet', label='f(x)')
    plt.plot(x_plot, y_uniform_interp, 'magenta', label=f'W_n(x) - {n} węzłów równomiernych')
    plt.grid()
    plt.scatter(x_uniform, y_uniform, c='violet')
    plt.legend()
    plt.title(f'Interpolacja Lagrange\'a dla węzłów równomiernych (n={n})')
    plt.subplot(1, 2, 2)
    plt.plot(x_plot, f(x_plot), 'violet', label='f(x)')
    plt.plot(x_plot, y_chebyshev_interp, 'magenta', label=f'W_n(x) - {n} węzłów Czebyszewa')
    plt.scatter(x_chebyshev, y_chebyshev, c='violet')
    plt.legend()
    plt.grid()
    plt.title(f'Interpolacja Lagrange\'a dla węzłów Czebyszewa (n={n})')
    plt.show()
