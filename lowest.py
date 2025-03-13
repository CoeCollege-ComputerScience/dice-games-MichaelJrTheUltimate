# import random

# def rollDice():
#     return random.randint(1,6)
# def scoring():
#     LowestRolls = []
#     Dice1 = rollDice()
#     Dice2 = rollDice()
#     Dice3 = rollDice()
#     Dice4 = rollDice()
#     Dice5 = rollDice()
#     print(f"Dice1: {Dice1}")
#     print(f"Dice2: {Dice2}")
#     print(f"Dice3: {Dice3}")
#     print(f"Dice4: {Dice4}")
#     print(f"Dice5: {Dice5}")
#     LowRoll = min(Dice1, Dice2, Dice3, Dice4, Dice5)
#     LowestRolls.append(LowRoll)
#original code didn't seem promising & seemed like it was going to be tedious
import random

def rollDice():
    return random.randint(1, 6)

def scoring():
    dice_rolls = [rollDice() for _ in range(5)]
    LowestRolls = []

    for i in range(5):
        print(f"Dice{i + 1}: {dice_rolls[i]}")

    while dice_rolls:
        LowRoll = min(dice_rolls)
        LowestRolls.append(LowRoll)
        dice_rolls.remove(LowRoll)

    print(f"Lowest Rolls: {LowestRolls}")
    Score = sum(LowestRolls)
    print(f"Score: {Score}")
    return Score
def main():
    Player1Score = scoring()
    Player2Score = scoring()
    if Player1Score >= 20:
        print("Player 2 wins!")
    elif Player2Score >= 20:
        print("Player 1 wins!")
    elif Player1Score < Player2Score:
        print("Player 1 wins!")
    elif Player2Score < Player1Score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

main()