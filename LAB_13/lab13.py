import numpy as np
import matplotlib.pyplot as plt

def gen(a, c, m, seed, n):
    x = seed
    numbers = []
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)
    return np.array(numbers)

def plot_histogram(data, bins, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

n = 10000
seed = 10

#podpunkt a 
a1, c1, m1 = 123, 1, 2**15
uniform_numbers_1 = gen(a1, c1, m1, seed, n)

#podpunkt b 
a2, c2, m2 = 69069, 1, 2**32
uniform_numbers_2 = gen(a2, c2, m2, seed, n)

mu = 0.2
sigma = 0.5
u1 = uniform_numbers_2[:n//2]
u2 = uniform_numbers_2[n//2:]
z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
z1 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)
normal_numbers = mu + sigma * np.concatenate((z0, z1))
normal_numbers = normal_numbers[(normal_numbers >= mu - 3 * sigma) & (normal_numbers <= mu + 3 * sigma)]
plot_histogram(normal_numbers, bins=12, title=' (μ=0.2, σ=0.5)', xlabel='' , ylabel='')
theoretical_mu = np.mean(normal_numbers)
theoretical_sigma = np.std(normal_numbers)
print(f' {theoretical_mu}')
print(f' {theoretical_sigma}')
