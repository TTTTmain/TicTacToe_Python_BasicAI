import random

starter = [0,1]
playerVal = 0

def coin_toss():

    outcome = random.choice(starter)

    if outcome == 0:
        print("You go first")
        playerVal = 0

    elif outcome == 1:
        print("Computer goes first")
        playerVal = 1
