import random

def rollDice():
    return random.randint(1, 6)
def Rolling():
    Rolls = [rollDice() for _ in range(10)]
    Score = sum(Rolls)
    return Score