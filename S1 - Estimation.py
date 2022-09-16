from random import randint


mean = lambda vector : sum(vector) / len(vector)



def game():
    dice_roll = randint(1, 6)
    gain = dice_roll
    
    while dice_roll > 3:
        dice_roll = randint(1, 6)
        gain += dice_roll
    
    return gain



def estimation(game, times=10000):
    gains = [game() for time in range(times)]
    return mean(gains)