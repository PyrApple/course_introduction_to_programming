# %%

# import
import pygame
from pathlib import Path
import time

# get list of files
audioFiles = sorted(Path("../assets/scales").glob("*.mp3"))

# init mixer
pygame.mixer.init()

# define scores (notes are ids, -1 is silence)
exorcist = {
    "notes": [6, -1, 6, -1, 6, -1, -1, 6, 0, 6, 1, 6, 8, 0, 6, 3, 6, 5, 6, 1, 3, 6, 1, 6, 0, 6, 1, 6, 8, 0],
    "ioi": 0.23
} 
scale = { 
    "notes": [2, 4, 6, 7, 8, 0, 1, 3],
    "ioi": 0.3,
}
debug = {
    "notes": [6, -1, -1, 6, -1],
    "ioi": 0.23
} 
score = exorcist

# loop over notes
for noteId in score['notes']:

    # -1 is silence
    if( noteId == -1 ): 
        time.sleep(score["ioi"])
        continue

    # get audio file path
    audioFile = audioFiles[noteId]
    filePath = audioFile.absolute()
    
    # play audio 
    s = pygame.mixer.Sound(filePath)
    s.play()

    # pause
    time.sleep(score["ioi"])
