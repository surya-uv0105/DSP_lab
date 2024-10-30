

import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    else:
        xe = x[0::2]  
        xo = x[1::2] 
        Xe = fft(xe)
        Xo = fft(xo)
        wn = np.exp(-2j * np.pi * np.arange(N // 2) / N)
        X = np.concatenate((Xe + wn * Xo, Xe - wn * Xo))
        return X

x = np.array([1, -1, 2, 4])
r = fft(x)
print("FFT:", r)