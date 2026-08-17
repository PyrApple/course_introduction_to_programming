# %%

# import
from math import floor
import numpy as np
import sounddevice as sd
from scipy.signal import square, sawtooth
import librosa

# Audio Synthetiser class
class Synthetiser:

    # constructor
    def __init__(self, fs):
        
        # locals
        self.fs = fs
        self.note_duration = 0.05 # in sec
        self.num_harmonics = 3
        self.set_wave_shape("sine")

        # envelope
        self.set_envelope_params(0.05, 0.01, 0.75, 0.1)

    # define wave shape
    def set_wave_shape(self, shape):

        # discard if waveform not supported
        if shape not in ["sine", "sawtooth", "square"]:
            raise ValueError("unexpected wave shape")

        # update locals
        self.shape = shape

    # define envelope parameters
    def set_envelope_params(self, attack = 0.05, decay = 0.01, sustain = 0.75, release = 0.1):
        
        # normalise to sum 1
        sum = attack + decay + sustain + release

        # update locals
        self.attack = attack / sum
        self.decay = decay / sum
        self.sustain = sustain / sum
        self.release = release / sum

    # returns envelope array (to multiply with audio waveform)
    def get_envelope(self):

        # get overall length
        n = self.note_duration * self.fs

        # define segments
        attack = np.linspace(0, 1, floor(n * self.attack))
        decay = np.linspace(1, 0.8, floor(n * self.decay))
        sustain = np.linspace(0.6, 0.6, floor(n * self.sustain))
        release = np.linspace(0.6, 0, floor(n * self.release))

        # concatenate segments
        return np.concatenate((attack, decay, sustain, release))

    # return note ready to play
    def get_note(self, freq):
        
        # define time vector 
        t = np.arange(int(self.fs * self.note_duration)) / self.fs
        v = 2 * np.pi * freq * t

        # generate wave
        wave = np.zeros(len(v))
        match self.shape:
            case "sine":
                for iHarm in range(self.num_harmonics):
                    wave += np.sin( (iHarm+1) * v)
            case "square":
                wave = square(2 * np.pi * freq * t)
            case "sawtooth":
                wave = sawtooth(2 * np.pi * freq * t, width=0.5)

        # create envelope
        envelope = self.get_envelope()

        # adjust length
        envelope = np.concatenate( (envelope, np.zeros( int(len(t) - len(envelope))) ))
        
        # apply envelope
        wave *= wave * envelope

        # norm
        wave /= np.max(np.abs(wave))

        return wave

    # play a note
    def play_note(self, freq):

        # get note
        note = self.get_note(freq)

        # play note
        sd.play(note, self.fs)
        

# init locals
fs = 44100

# create synthetiser
synth = Synthetiser(fs)
synth.set_wave_shape("sine")

# create note sequence
note_sequence = ['E4', 'A4', 'E4', 'B4', 'E4', 'G4', 'A4', 'E4', 'C5', 'E4', 'D5', 'E4', 'B4', 'C5', 'E4', 'B4', 'E4', 'A4', 'E4', 'B4', 'E4', 'G4', 'A4']
freq_sequence = librosa.note_to_hz(note_sequence)

# play note sequence
for freq in freq_sequence:
    synth.play_note(freq)
    sd.wait()

