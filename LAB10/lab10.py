import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

el_k = [8,10,12]

for k in el_k:
    Nk = 2**k 
    T = 1.0 
    t_max = 3 * T  
    dt = t_max / Nk  
    sigma = T / 20  
    t = np.linspace(0, t_max, 2 * Nk, endpoint=False)  
    omega = 2 * np.pi / T
    f0 = np.sin(omega * t) + np.sin(2 * omega * t) + np.sin(3 * omega * t)
    delta = np.random.uniform(-0.5, 0.5, 2 * Nk)
    f = f0 + delta
    g1 = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(t - t_max / 2)**2 / (2 * sigma**2))
    g2 = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(t - t_max / 2)**2 / (2 * sigma**2))
    F_f = fft(f)
    G1 = fft(g1)
    G2 = ifft(g2)
    t_splt = F_f *(G1 + G2)
    f_wygl= ifft(t_splt).real
    f_wygl = f_wygl[:2*Nk]
    plt.figure(figsize=(12, 6))
    plt.plot(t, f, color='red', linestyle='--')
    plt.plot(t, f0, color='blue')
    plt.grid(True)
    plt.show()
