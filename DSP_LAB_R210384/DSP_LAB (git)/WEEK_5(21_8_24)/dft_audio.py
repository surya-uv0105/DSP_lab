import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

def dft(x, N):
    X = []
    for k in range(0, N):
        s = 0
        for n in range(0, N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    return X

fs, audio = wavfile.read('/home/surya/Downloads/DSP_LAB_R210384/DSP_LAB (git)/WEEK_5(21_8_24)/whisper-trail-2ogg-14429.wav')
audio = audio / (2**15)
N = len(audio)
x = dft(audio, N)
mag = np.abs(x)
ang = np.angle(x)
k_max = np.argmax(mag)
frequency = k_max * fs / N
print("Frequency:", frequency)
plt.subplot(2, 1, 1)
plt.plot(mag)
plt.subplot(2, 1, 2)
plt.plot(ang)
plt.show()
