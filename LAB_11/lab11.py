import numpy as np

def f(x, m, k):
    return x**m*np.sin(k*x)

def simpson(a, b, n, m, k):
    if n % 2 == 1: 
        n += 1 
    h = (b - a) / n 
    x = np.linspace(a, b, n + 1) 
    y = f(x, m, k)
    S = y[0] + y[-1] 
    S += 2 * np.sum(y[2:n:2]) 
    S += 4 * np.sum(y[1:n:2]) 
    return (h / 3) * S

#podpunkt a
m_1 = 0
k_1 = 1
n_wezl = [11, 21, 51, 101, 201]
w_dokl_1 = 2

#podpunkt b
m_2 = 1
k_2 = 1
w_dokl_2 = np.pi
#roznica miedzy wartoscia dokladna a obliczona 1

#podpunkt c 
m_3 = 5
k_3 = 5
w_dokl_3 = 56.363569
#roznica miedzy wartoscia dokladna a obliczona 1

print("podpunkt a:")
for n in n_wezl:
    print(simpson(0, np.pi, n, m_1, k_1))
    #roznica miedzy wartoscia dokladna a obliczona 1
    C_I_1 = np.abs(simpson(0, np.pi, n, m_1, k_1) - w_dokl_1)
    print("roznica: ", C_I_1)

print()
print("podpunkt b:")
for n in n_wezl:
    print(simpson(0, np.pi, n, m_2, k_2))
    #roznica miedzy wartoscia dokladna a obliczona 2
    C_I_2 = np.abs(simpson(0, np.pi, n, m_2, k_2) - w_dokl_2)
    print("roznica: ", C_I_2)

print()
print("popunkt c:")
for n in n_wezl:
    print(simpson(0, np.pi, n, m_3, k_3))
    #roznica miedzy wartoscia dokladna a obliczona 3
    C_I_3 = np.abs(simpson(0, np.pi, n, m_3, k_3) - w_dokl_3)
    print("roznica: ", C_I_3)
