# import
import random

# local function
def should_i_win(my_luck = 0.5):
    return random.random() <= my_luck


# define class 
class Enemy:

    # constructor
    def __init__(self, health):
        self.health = health
    
    # take damage
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)


class AnnoyingEnemy(Enemy):

    # constructor
    def __init__(self, health, luck):
        super().__init__(health)
        self.luck = luck

    # take damage
    def take_damage(self, damage):
        
        # lucky 
        if( should_i_win(self.luck) ):
            self.boast()
        
        # not lucky
        else:
            super().take_damage(damage)
        
    # boast
    def boast(self):
        print("weak blow!")