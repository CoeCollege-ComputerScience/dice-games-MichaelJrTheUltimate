# import random

# def rollDice():
#     return random.randint(1, 6)
# def main():
#     Player1Score = 0
#     Player2Score = 0
#     Player1Rolls = []
#     Player2Rolls = []
#     Player1Rolling = rollDice()
#     print(f"Player 1 rolled: {Player1Rolling}")
#     Player1Hold = int(input("Player 1, Are you holding? yes/no: "))
#     if Player1Hold == "yes":
#         Player1Score += Player1Rolling
#     elif Player1Hold == "no":
#         Player1Rolling = rollDice()
#         print(f"Player 1 rolled: {Player1Rolling}")
#     else:
#         Player1Rolls.append(Player1Rolling)
#     if Player1Rolling == 1:
#         print("Player 1 loses their turn")
#     Player2Rolling = rollDice()
#     print(f"Player 2 rolled: {Player2Rolling}")
#     Player2Hold = int(input("Player 2, Are you holding? yes/no: "))
#     if Player2Hold == "yes":
#         Player2Score += Player2Rolling
#     elif Player2Hold == "no":
#         Player2Rolling = rollDice()
#         print(f"Player 2 rolled: {Player2Rolling}")
#     else:
#         Player2Rolls.append(Player2Rolling)
#     if Player2Rolling == 1:
#         print("Player 2 loses their turn")
#     if Player1Score >= 100:
#         print("Player 1 wins!")
#     elif Player2Score >= 100:
#         print("Player 2 wins!")
#     elif Player1Score < Player2Score:
#         print("Player 1 wins!")
#     elif Player2Score < Player1Score:
#         print("Player 2 wins!")
#     else:
#         print("It's a tie!")
#     print(f"Player 1's score: {Player1Score}")
#     print(f"Player 2's score: {Player2Score}")
#     print(f"Player 1's rolls: {Player1Rolls}")
#     print(f"Player 2's rolls: {Player2Rolls}")
#     print(f"Player 1's total score: {sum(Player1Rolls)}")
#     print(f"Player 2's total score: {sum(Player2Rolls)}")
#     return Player1Score, Player2Score
# main()
#original code was organized wrong & had some trouble with hold command
import random

def rollDice():
    return random.randint(1, 6)

def main():
    Player1Score = 0
    Player2Score = 0
    Player1Rolls = []
    Player2Rolls = []

    while Player1Score < 100 and Player2Score < 100:
        # Player 1's turn
        turn_over = False
        while not turn_over:
            Player1Rolling = rollDice()
            print(f"Player 1 rolled: {Player1Rolling}")
            if Player1Rolling == 1:
                print("Player 1 loses their turn")
                turn_over = True
            else:
                Player1Rolls.append(Player1Rolling)
                Player1Hold = input("Player 1, Are you holding? yes/no: ").strip().lower()
                if Player1Hold == "yes":
                    Player1Score += sum(Player1Rolls)
                    Player1Rolls = []
                    turn_over = True
                elif Player1Hold == "no":
                    continue
                else:
                    print("Invalid input, please enter 'yes' or 'no'.")

        # Check if Player 1 wins
        if Player1Score >= 100:
            print("Player 1 wins!")
            break

        # Player 2's turn
        turn_over = False
        while not turn_over:
            Player2Rolling = rollDice()
            print(f"Player 2 rolled: {Player2Rolling}")
            if Player2Rolling == 1:
                print("Player 2 loses their turn")
                turn_over = True
            else:
                Player2Rolls.append(Player2Rolling)
                Player2Hold = input("Player 2, Are you holding? yes/no: ").strip().lower()
                if Player2Hold == "yes":
                    Player2Score += sum(Player2Rolls)
                    Player2Rolls = []
                    turn_over = True
                elif Player2Hold == "no":
                    continue
                else:
                    print("Invalid input, please enter 'yes' or 'no'.")

        # Check if Player 2 wins
        if Player2Score >= 100:
            print("Player 2 wins!")
            break

    print(f"Player 1's score: {Player1Score}")
    print(f"Player 2's score: {Player2Score}")
    print(f"Player 1's rolls: {Player1Rolls}")
    print(f"Player 2's rolls: {Player2Rolls}")

main()