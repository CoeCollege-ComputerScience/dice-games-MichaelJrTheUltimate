import random

def rollDice():
    return random.randint(1, 6)
def Rolling():
    Rolls = [rollDice() for _ in range(3)]
    Score = sum(Rolls)
    return Score
# def Main():
#     Player1Wins = 0
#     Score = Rolling()
#     print(f"Score: {Score}")
#     Player1Guess = input("Player 1, enter your guess (Over/Under): ")
#     Player1Score = Rolling()
#     if Player1Guess == "Over" and Player1Score > Score:
#         Player1Wins += 1
#         print(f"Correct! Guess: {Player1Score}, Score: {Score}")
#     elif Player1Guess == "Under" and Player1Score < Score:
#         Player1Wins += 1
#         print(f"Correct! Guess: {Player1Score}, Score: {Score}")
#     else: 
#         print(f"Wrong Guess: {Player1Score}, Score: {Score}")
#     return Player1Score


# Main()
#my code before needing help on swapping between 2 players
def Main():
    Player1Wins = 0
    Player2Wins = 0
    round = 0

    while Player1Wins < 5 and Player2Wins < 5:
        if round % 2 == 0:
            # Player 1 rolls, Player 2 guesses
            Score = Rolling()
            print(f"Player 1 rolled a score of: {Score}")
            Player2Guess = input("Player 2, enter your guess (Over/Under): ")
            Player2Score = Rolling()
            if Player2Guess == "Over" and Player2Score > Score:
                Player2Wins += 1
                print(f"Correct! Player 2 guessed: {Player2Score}, Player 1's score: {Score}")
            elif Player2Guess == "Under" and Player2Score < Score:
                Player2Wins += 1
                print(f"Correct! Player 2 guessed: {Player2Score}, Player 1's score: {Score}")
            else:
                print(f"Wrong Guess! Player 2 guessed: {Player2Score}, Player 1's score: {Score}")
        else:
            # Player 2 rolls, Player 1 guesses
            Score = Rolling()
            print(f"Player 2 rolled a score of: {Score}")
            Player1Guess = input("Player 1, enter your guess (Over/Under): ")
            Player1Score = Rolling()
            if Player1Guess == "Over" and Player1Score > Score:
                Player1Wins += 1
                print(f"Correct! Player 1 guessed: {Player1Score}, Player 2's score: {Score}")
            elif Player1Guess == "Under" and Player1Score < Score:
                Player1Wins += 1
                print(f"Correct! Player 1 guessed: {Player1Score}, Player 2's score: {Score}")
            else:
                print(f"Wrong Guess! Player 1 guessed: {Player1Score}, Player 2's score: {Score}")
        
        round += 1 #help on having rounds continue until either player got 5 wins

    print(f"Final Scores: Player 1 Wins: {Player1Wins}, Player 2 Wins: {Player2Wins}")

Main()