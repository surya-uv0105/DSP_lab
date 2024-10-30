import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num_zeros = int(input("Enter the number of zeros: "))
zeros = [complex(input(f"Enter zero {i + 1} (e.g., 1+2j): ")) for i in range(num_zeros)]

num_poles = int(input("Enter the number of poles: "))
poles = [complex(input(f"Enter pole {i + 1} (e.g., 1+2j): ")) for i in range(num_poles)]

w, h = signal.freqz_zpk(zeros, poles, 1)  # important

magnitude_H = np.abs(h)
phase_H = np.angle(h)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(w, magnitude_H, 'b')
plt.title('Magnitude of H(w)')
plt.xlabel('Frequency (w)')
plt.ylabel('|H(w)|')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(w, phase_H, 'r')
plt.title('Phase of H(w)')
plt.xlabel('Frequency (w)')
plt.ylabel('Phase of H(w) (radians)')
plt.grid()

plt.tight_layout()
plt.show()
