from random import random

def flip_coin():
    # generate random numbers
    r = random()
    if r > 0.5:
        return 'Heads'
    else:
        return 'Tails'
print(flip_coin())    
