from random import randint
import json


def computerhand():
    rand = randint(0,2)
    comphand = ""
    if rand == 0:
        comphand = "rock"
    if rand == 1:
        comphand = "paper"
    if rand == 2:
        comphand = "scissors"
    return comphand

def check_winner(player1, player2):
    winner = ""
    if player1 == "rock":
        if player2 == "rock":
            winner = "tie"
        elif player2 == "paper":
            winner = "player 2"
        elif player2 == "scissors":
            winner = "player 1"
    if player1 == "paper":
        if player2 == "rock":
            winner = "player 1"
        elif player2 == "paper":
            winner = "tie"
        elif player2 == "scissors":
            winner = "player 2"
    if player1 == "scissors":
        if player2 == "rock":
            winner = "player 2"
        elif player2 == "paper":
            winner = "player 1"
        elif player2 == "scissors":
            winner = "tie"

    return (winner)

def playerhand():
    while True:
        playerhand = str(input("Rock, paper or scissors? ")).lower()
        if playerhand != "rock" and playerhand != "paper" and playerhand != "scissors":
            print("That an invalid input, please try again.")
        else:
            break
    return (playerhand)

def rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

def paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

def scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def show_image(imageinput):
    if imageinput == "rock":
        rock()
    elif imageinput == "paper":
        paper()
    elif imageinput == "scissors":
        scissors()

def playwithcomp():
    while True:
        winner = ""
        player = playerhand()
        show_image(player)
        computer = computerhand()
        show_image(computer)
        winner = check_winner(player, computer)

        print ("The computer chose %s" %(computer))
        if winner == "tie":
            print("It's a tie, please try again.")
        elif winner == "player 1":
            print("Congratulations you have won! You are way smarter than a computer :D")
            winner = "player"
            break
        elif winner == "player 2":
            print("You lost, the computer was too smart for you.")
            winner = "computer"
            break
    return (winner)

def play_against_computer_repetition():
    compwin = 0
    playerwin = 0
    while True:
        winner = playwithcomp()
        if winner == "player":
            playerwin += 1
        elif winner == "computer":
            compwin += 1
        print("")
        print("Wins: ")
        print("Player: %s" %(playerwin))
        print("Computer: %s" %(compwin))
        print("")
        if not str(input("Do you want to play again (type 'yes')? ")).lower() == "yes":
            break

def play_against_computer_best_of_3():
    print ("You are going to play a best of three Rock, Paper, Scissors against this computer")
    print ("Good Luck!")
    print ("")
    entirewinner = ""
    compwin = 0
    playerwin = 0
    while True:
        winner = playwithcomp()
        if winner == "player":
            playerwin += 1
        elif winner == "computer":
            compwin += 1
        print("")
        print("Wins: ")
        print("Player: %s" %(playerwin))
        print("Computer: %s" %(compwin))
        print("")
        if compwin == 2:
            print("The computer beat you in this best of three!")
            entirewinner = "computer"
            break
        elif playerwin == 2:
            print("Congratulations! You defeated the computer in this best of three!")
            entirewinner = "player"
            break
    return (entirewinner)

def add_all_stats(filename, game):
    with open(filename, "r") as f:
        dict = json.load(f)

    if game == "player":
        dict["player"] += 1
    elif game == "computer":
        dict["computer"] += 1

    with open(filename, "w") as f:
        json.dump(dict, f)


add_all_stats("RPSStats.json", play_against_computer_best_of_3())
