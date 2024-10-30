import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5  # Frequency of the sine wave (Hz)
decay_rate = 1  # Rate of decay (1/s)
fs = 100  # Sampling frequency (samples per second)
t = np.arange(0, 2, 1/fs)  # Time vector for 2 seconds

# Generate the original signal (sine wave)
original_signal = np.sin(2 * np.pi * frequency * t)

# Multiply by exponential decay
decayed_signal = original_signal * np.exp(-decay_rate * t)

# Compute FFT
fft_result = np.fft.fft(decayed_signal)
n = len(decayed_signal)  # Number of samples
frequencies = np.fft.fftfreq(n, 1/fs)  # Frequency bins

# Calculate magnitude
magnitude = np.abs(fft_result)

# Plot the original and decayed signals
plt.figure(figsize=(12, 8))

# Plot original signal
plt.subplot(3, 1, 1)
plt.plot(t, original_signal)
plt.title('Original Signal (Sine Wave)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot decayed signal
plt.subplot(3, 1, 2)
plt.plot(t, decayed_signal)
plt.title('Decayed Signal (Sine Wave * Exponential Decay)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot the FFT results (magnitude)
plt.subplot(3, 1, 3)
plt.plot(frequencies[:n//2], magnitude[:n//2])  # Only positive frequencies
plt.title('FFT of the Decayed Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, fs/2)  # Limit to positive frequencies

plt.tight_layout()
plt.show()

