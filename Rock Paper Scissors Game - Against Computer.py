# Input
player_one = input("Choose from rock, paper, or scissors: ")
#computer_action = input("choose from rock, paper, or scissors: ")

# Processing
import random
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if player_one ==  computer_action:
    print("Tie!")
elif player_one == "rock":
    if computer_action == "scissors":
        print("Player one wins!")
    elif  computer_action == "paper":
        print("You lost!")    
elif player_one == "paper":
    if  computer_action == "scissors":
        print("You lost")
    elif  computer_action == "rock":
        print("Player one wins!")
elif player_one == "paper":
    if  computer_action == "rock":
        print("Player one wins!")
    elif  computer_action == "scissors":
        print("You lost!")

print(computer_action)
