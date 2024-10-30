

#linear convolution  from circular conv

import numpy as np
import matplotlib.pyplot as plt

def linear_conv(x, h):
    N = len(x) + len(h) - 1
    y = np.zeros(N)
    for n in range(N):
        for m in range(len(x)):
            if n - m >= 0 and n - m < len(h):
                y[n] += x[m] * h[n - m]
    return y

def circ_conv(x, h):
    N = len(x) + len(h) - 1
    x = np.pad(x, (0, N - len(x)))
    h = np.pad(h, (0, N - len(h)))
    y = np.zeros(N)
    for n in range(N):
        for m in range(N):
            y[n] += x[m] * h[(n - m) % N]
    return y


x = np.array([1, 2, 3, 4])
h = np.array([5, 6, 7, 8])

y_linear = linear_conv(x, h)

y_circ = circ_conv(x, h)

print("Linear Convolution Result:", [i for i in y_linear])
print("Circular Convolution Result:", [i for i in y_circ])
print("Equality Check:", np.allclose(y_linear, y_circ))

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(y_linear)
plt.title("Linear Convolution")


plt.subplot(2, 1, 2)
plt.stem(y_circ)
plt.title("Circular Convolution")

plt.show()