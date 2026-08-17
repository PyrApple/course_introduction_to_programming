# %%

# import 
from pathlib import Path
import soundfile as sf
import sounddevice as sd
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import control

# function: create lowpass filter
def butter_lowpass(cutoff_freq, fs, order=2):
    return butter(order, cutoff_freq, fs=fs, btype='low', analog=False)

# function: create and apply lowpass filter
def butter_lowpass_filter(data, cutoff_freq, fs, order=2):
    b, a = butter_lowpass(cutoff_freq, fs, order=order)
    y = lfilter(b, a, data)
    return y

# load audio file
filePath = Path("../assets/drumloop.wav")
audioIn, fs = sf.read(filePath)
audioIn = audioIn[0 : 2*fs] # debug: reduce loop duration

# init filter
order = 6
cutoff_freq = 100  # Hz

# get filter
b, a = butter_lowpass(cutoff_freq, fs, order)

# plot filter frequency response
w, h = freqz(b, a, fs=fs, worN=8000)
plt.figure(figsize=(10, 4))
plt.plot(w, np.abs(h), 'b')
plt.plot(cutoff_freq, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff_freq, color='k')
plt.xlim(0, cutoff_freq*2)
plt.ylabel("response")
plt.xlabel('frequency (Hz)')
plt.grid()

# apply filter
audioOut = butter_lowpass_filter(audioIn, cutoff_freq, fs, order)

# # play
# sd.play(audioOut, fs)
# sd.wait()

# fft
audioIn_spectrum = np.fft.rfft(audioIn)
audioOut_spectrum = np.fft.rfft(audioOut)
freq = np.fft.rfftfreq(len(audioOut), 1/fs)

# plot spectrum
plt.figure(figsize=(10, 4))
plt.plot(freq, control.mag2db( np.abs(audioIn_spectrum) ))
plt.plot(freq, control.mag2db( np.abs(audioOut_spectrum) ))

# format plot
plt.xscale('log')
plt.xlim(0, 8000)
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude (dB)")
plt.grid()
plt.show()

# write audio to disk
sf.write("drumloop_filtered.wav", audioOut, fs)
