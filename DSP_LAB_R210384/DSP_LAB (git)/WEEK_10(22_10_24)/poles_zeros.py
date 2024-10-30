import numpy as np
import matplotlib.pyplot as plt

num_zeros = int(input("Enter the number of zeros: "))
zeros = [complex(input(f"Enter zero {i + 1} (e.g., 1+2j): ")) for i in range(num_zeros)]

num_poles = int(input("Enter the number of poles: "))
poles = [complex(input(f"Enter pole {i + 1} (e.g., 1+2j): ")) for i in range(num_poles)]

w = np.linspace(-10, 10, 1000)

numerator = np.prod([(1 - (1j * w / zero)) for zero in zeros], axis=0) if zeros else np.ones_like(w)
denominator = np.prod([(1 - (1j * w / pole)) for pole in poles], axis=0) if poles else np.ones_like(w)
H_w = numerator / denominator

magnitude_H = np.abs(H_w)
phase_H = np.angle(H_w)

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
