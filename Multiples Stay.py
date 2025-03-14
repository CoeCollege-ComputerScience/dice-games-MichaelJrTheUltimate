import random

def rollDice():
    return random.randint(1, 6)

def Rolling(remaining_rolls, player_name):
    unique_rolls = set()

    Rolls = [rollDice() for _ in range(remaining_rolls)]
    print(f"{player_name} rolled: ", Rolls)
        
    for roll in Rolls:
        if roll in unique_rolls:
            remaining_rolls -= 1
        else:
            unique_rolls.add(roll)
        
        print(f"{player_name} has", remaining_rolls, "rolls left")
    
    return remaining_rolls

def main():
    Player1Rolling = True
    Player2Rolling = False
    remaining_rolls = 10

    while remaining_rolls > 1:
        if Player1Rolling:
            print("Player 1's turn:")
            remaining_rolls = Rolling(remaining_rolls, "Player 1")
            Player1Rolling = False
            Player2Rolling = True
        elif Player2Rolling:
            print("Player 2's turn:")
            remaining_rolls = Rolling(remaining_rolls, "Player 2")
            Player2Rolling = False
            Player1Rolling = True

    if remaining_rolls == 1 or remaining_rolls == 0:
        if Player1Rolling:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

main()