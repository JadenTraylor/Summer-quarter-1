def RPS():
    print("Welcome to Rock Paper Scissors!")


    player1 = input("PLayer 1, please enter name:")
    player2 = input("PLayer 2, plaese enter your name:")

    p1_Choice = input(f"{player1}, choose between Rock, Paper & Scissors.").lower()
    
    while not IsValidMove(p1_Choice):
        print("Invalid Move! Please try again")
        p1_Choice = input(f"{player1}, choose between Rock, Paper & Scissors.").lower()
    
    p2_Choice = input(f"{player2}, choose between Rock, Paper & Scissors.").lower()
    while not IsValidMove(p2_Choice):
        print("Invalid Move! Please try again")
        p2_Choice = input(f"{player2}, choose between Rock, Paper & Scissors.").lower()
    
    
    if p1_Choice == "rock" and p2_Choice == "scissors":
        print(f"Rock beats scissors, {player1} wins!")
    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"paper beats rock, {player1} wins!")
    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"scissors beats paper, {player1} wins!")


    elif p2_Choice == "rock" and p1_Choice == "scissors":
        print(f"Rock beats scissors, {player2} wins!")
    elif p2_Choice == "paper" and p1_Choice == "rock":
        print(f"paper beats rock, {player2} wins!")
    elif p2_Choice == "scissors" and p1_Choice == "paper":
        print(f"scissors beats paper, {player2} wins!")


def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]

    if playerMove.lower()in validMoves:
        return True
    else:
        return False


RPS()