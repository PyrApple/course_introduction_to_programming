# %%

# imports
import random

# get random number 
max_number = 10
r = random.randint(1, 10)

# init local
you_win = False

# game start 
print(f"# guess number between 1 and {max_number}")
while( you_win == False ):

    # get user input
    v = int(input('your number: '))

    # success
    if( r == v ):
        you_win = True
        print(f'it was {r}, you guessed it!')
    
    # fail
    elif( r > v ):
        print('higher')
    
    else:
        print('lower')
