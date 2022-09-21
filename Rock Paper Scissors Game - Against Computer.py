# Input
player_action = input("Choose from rock, paper, or scissors: ")
#computer_action = input("choose from rock, paper, or scissors: ")

# Processing
import random
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)


print(computer_action)