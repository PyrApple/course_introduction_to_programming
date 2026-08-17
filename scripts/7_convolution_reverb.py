# %%

# import 
from pathlib import Path
import soundfile as sf
from scipy.signal import fftconvolve

# load audio file
filePath = Path("../assets/drumloop.wav")
audioIn, fs = sf.read(filePath)
audioIn = audioIn[0 : 2*fs] # reduce loop duration

# init locals
# irFileName = "ir_mono.wav"
irFileName = "ir_binaural.wav"

# load impulse response
filePath = Path("../assets/" + irFileName)
ir, fs_ir = sf.read(filePath)

# mono
if( ir.ndim == 1 ):

    # convolve
    audioOut = fftconvolve(audioIn, ir)

# stereo
else: 

    # convolve each channel
    audioOut_left  = fftconvolve(audioIn, ir[:, 0])
    audioOut_right = fftconvolve(audioIn, ir[:, 1])
    audioOut = np.column_stack((audioOut_left, audioOut_right))

# play
sd.play(audioOut, fs)
sd.wait()
