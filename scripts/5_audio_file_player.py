# %%

# import 
from pathlib import Path
import soundfile as sf

# load audio file
filePath = Path("../assets/drumloop.wav")
audioIn, fs = sf.read(filePath)

# play
sd.play(audioIn, fs)
sd.wait()
