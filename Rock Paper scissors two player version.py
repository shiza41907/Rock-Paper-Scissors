# Input
player_one = input("Choose from rock, paper, or scissors: ")
possible_actions = ["rock", "paper", "scissors"]
player_two = input("Choose from rock, paper, or scissors: ")

# Processing
possible_actions = ["rock", "paper", "scissors"]
if player_one == player_two:
    print("Tie!")
elif player_one == "rock":
    if player_two == "scissors":
        print("Player one wins!")
    elif player_two == "paper":
        print("Player two wins!")    
elif player_one == "paper":
    if player_two == "scissors":
        print("Player two wins!")
    elif player_two == "rock":
        print("Player one wins!")
elif player_one == "paper":
    if player_two == "rock":
        print("Player one wins!")
    elif player_two == "scissors":
        print("Player two wins!")