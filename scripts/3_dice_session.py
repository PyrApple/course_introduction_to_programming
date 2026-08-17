# %%

# import modules
import random

# init locals
score_blue = 0
nFaces = 6
nTrials = 10

# loop over trials
for iTrial in range(nTrials):

    # throw dices
    blue = random.randint(1, nFaces)
    red = random.randint(1, nFaces)

    # log    
    print(f"trial {iTrial}: blue {blue}, red: {red}")

    # increment score
    if( blue > red ):
        score_blue += 1

print(f"blue success rate: {100 * score_blue / nTrials:0.0f}%")