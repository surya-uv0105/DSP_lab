import numpy as np
import matplotlib.pyplot as plt

def convolve(x, h):
    N = len(x) + len(h) - 1
    y = np.zeros(N)
    for i in range(N):
        for j in range(len(h)):
            if i-j >= 0 and i-j < len(x):
                y[i] += x[i-j] * h[j]
    return y

def overlap_save(x, h, N):
    y = np.zeros(len(x) + len(h) - 1)
    for i in range(0, len(x), N):
        block = x[i:i+N]
        convolved_block = convolve(block, h)
        y[i:i+len(convolved_block)] = convolved_block
    return y

x = np.array([1, 2, 3, 4, 5])
h = np.array([0.5, 1, 0.5])
N = 4

y = overlap_save(x, h, N)

plt.plot(x, label='Input Signal')
plt.plot(h, label='Filter')
plt.plot(y, label='Convolved Signal')
plt.legend()
plt.show()