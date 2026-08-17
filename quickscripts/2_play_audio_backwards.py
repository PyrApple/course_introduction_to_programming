# %%

# import 
from pathlib import Path
import soundfile as sf
import numpy as np
import sounddevice as sd

# load audio file
filePath = Path("../assets/drumloop.wav")
audioIn, fs = sf.read(filePath)

# init locals
audioOut = np.zeros(len(audioIn))

# loop over samples
for i_sample in range(len(audioIn)):
    audioOut[i_sample] = audioIn[len(audioIn)-i_sample-1]

# play
sd.play(audioOut, fs)
sd.wait()
