# Generate a random number
# User input
# Check if random number == user input
# If yes, exit
# If guess is large -> print too high
# If guess is low -> print too low
import random as rd
rand_no= rd.randint(1,10)# generate a random no
print("Guess The Number Game!\nYou have 5 attampts \nAll the bestt!!!\n")
attampts=5

while(attampts>0):
    user_no=int(input("Guess the random number betwen the range 1-10:"))#user input
    if (rand_no==user_no):
        print("correct guess!!")
        break
    elif(rand_no<user_no):
        print("no is too high")
       
    elif(rand_no>user_no):
        print("no is too low") 
       
    else:
        print("invalid input")
    attampts=attampts-1   
    print(f"Attempts remaining: {attempts}")

print("The number was:",rand_no)    
