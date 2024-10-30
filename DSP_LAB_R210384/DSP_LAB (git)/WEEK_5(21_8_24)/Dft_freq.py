import numpy as np
from matplotlib import pyplot as plt

def dft(x, N):
    X = []
    for k in range(0, N):
        s = 0
        for n in range(0, N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    return X

n = np.arange(0, 1000)
h = np.array([1, 2, 3, 4])
N = len(n)
X = np.cos(2 * np.pi * 200 * n / N)
x = dft(X, N)
mag = np.abs(x)
ang = np.angle(x)

sample_rate = 1000  
k_max = np.argmax(mag) 
frequency = k_max * sample_rate / N

print("peak:",np.max(mag))
print("k:",k_max)     
print("Frequency:", frequency)

plt.subplot(2, 1, 1)
plt.stem(mag)
plt.subplot(2, 1, 2)
plt.stem(ang)
plt.show()