import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
z = sp.symbols('z')

# Define sequence
sequence = [1, 2, 3, 4]

# Compute Z-transform
z_transform = sum(s * z**(-i) for i, s in enumerate(sequence))

# Simplify Z-transform expression
z_transform = sp.simplify(z_transform)

print("Z-transform:", z_transform)

# Define transfer function
H_z = z_transform

# Find poles and zeros
poles = sp.solve(sp.denom(H_z), z)
zeros = sp.solve(sp.numer(H_z), z)

print("Poles of the system:", poles)
print("Zeros of the system:", zeros)

# Plot zeros and poles
zeros = np.array([complex(zero) for zero in zeros], dtype=np.complex128)
poles = np.array([complex(pole) for pole in poles], dtype=np.complex128)

plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.scatter(zeros.real, zeros.imag, s=100, c='b', marker='o', label='Zeros')
plt.scatter(poles.real, poles.imag, s=100, c='r', marker='x', label='Poles')

unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)

plt.title('Zeros and Poles in the Z-Plane')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()