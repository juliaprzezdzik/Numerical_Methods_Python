import numpy as np
import matplotlib.pyplot as plt

n = 100 
x = np.linspace(0, 2 * np.pi, n, endpoint=False) 
alpha = 0

f1 = 2 * np.sin(x) + np.sin(2 * x) + 2 * np.sin(3 * x) + alpha
Ms = 5
Mc = 5

a0 = np.array([2/n * np.sum(f1)])
ak = np.array([2/n * np.sum(f1 * np.sin(k * x)) for k in range(1, Ms+1)])
bj = np.array([2/n * np.sum(f1 * np.cos(j * x)) for j in range(1, Mc+1)])

print("wartosci ak:", ak)
print("wartosci bj", bj)

F1 = a0 + sum(ak[k-1] * np.sin(k * x) for k in range(1, Ms+1)) + sum(bj[j-1] * np.cos(j * x) for j in range(1, Mc+1))

plt.figure(figsize=(10, 5)) 
plt.plot(x, f1, label='f1(x)')
plt.plot(x, F1, label='F1(x)', linestyle='dashed') 
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Aproksymacja funkcji $f_1(x)$')
plt.grid(True)
plt.show()
