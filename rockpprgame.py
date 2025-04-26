# List of game choices
# Random choice for computer
# User input
# Check winner
import random as rd
game_list=["rock","paper","scissor"]
computer=rd.choice(game_list)

user=input("Choose rock-paper-scissor:")
if(user not in game_list):
    print("invalid choice")
    exit()
else:
    print(f"Computer's choice is:{computer}")    


if (computer==user):
    print("tie")
elif (user=="rock" and computer == "scissor") or \
     (user=="paper" and computer == "rock") or \
      (user=="scissor " and computer == "paper") :
    print("Congratulations! You win!!") 
else:
    print("Computer won!! you lose")

    