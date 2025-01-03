import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("enter rock,paper or scissors ")
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("match tie")
    elif player == "rock":
        if computer == "scissors":
            print("you lost")
        if computer == "paper":
            print("you win")
    elif player == "paper":
        if computer == "scissors":
            print("you lost")
        if computer == "rock":
            print("you win")

    elif player == "scissors":
        if computer == "paper":
            print("you win")
        if computer == "rock":
            print("you lost")
    play_again = input("want to play again (yes/no): ")
    if play_again != "yes":
        break
print("bye")
#print(computer)
