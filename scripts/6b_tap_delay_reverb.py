# %%

# import 
from pathlib import Path
import soundfile as sf
import numpy as np
import sounddevice as sd

# load audio file
filePath = Path("../assets/drumloop.wav")
audioIn, fs = sf.read(filePath)
# audioIn = audioIn[0 : 2*fs] # debug: reduce loop duration

# define reverb configs (delays in ms)
# reverb = {"gains":[1], "delays": [0]}
# reverb = {"gains":[1, 0.7], "delays": [0, 100]} 
reverb = {"gains":[1, 0.7, 0.5, 0.3, 0.1], "delays": [0, 20, 30, 40, 50]} 

# convert delays to number of samples
reverb["delays"] = [int(fs * x/1000) for x in reverb["delays"]]

# init locals
audioOut = np.zeros( len(audioIn) + max(reverb["delays"]) )

# loop over tap delays
for iTap in range(len(reverb["delays"])):

    # get delay and gain
    n = reverb["delays"][iTap]
    g = reverb["gains"][iTap]
    
    # add tap to output
    audioOut[n:n+len(audioIn)] += g * audioIn

# normalise output gain
audioOut /= max(1, np.max(np.abs(audioOut)))

# playback
sd.play(audioOut, fs)
sd.wait()