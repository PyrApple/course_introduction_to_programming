# %%

# import
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# init locals
fs = 44100 # Hz
duration = 1 # secs
f1, f2, f3 = 440, 660, 880

# generate sine waves
t = np.arange(int(fs * duration)) / fs
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)
x3 = np.sin(2 * np.pi * f3 * t)

# mix audio
y = 1.0*x1 + 0.5*x2 + 0.2*x3

# normalise gain
y /= np.max(np.abs(y))

# play sound
sd.play(y, fs)
sd.wait()

# plot (time)
n = int(0.005 * fs)
plt.subplot(2, 1, 1)
plt.plot(t[:n], x1[:n], label=f"{f1} Hz")
plt.plot(t[:n], x2[:n], label=f"{f2} Hz")
plt.plot(t[:n], x3[:n], label=f"{f3} Hz")
plt.plot(t[:n], y[:n], label="Sum")

# format plot
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# fft
Y = np.fft.rfft(y)
freq = np.fft.rfftfreq(len(y), 1/fs)

# plot (freq)
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(Y))

# format plot
plt.xlim(0, 1200)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

# show plot
plt.tight_layout()
plt.show()
