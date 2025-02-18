# Lesson 9
from random import choice

invalid = True
player = '' #initializing the variable 

while invalid:
    player = input("Enter a choice of rock, paper, or scissor ")
    
    if player in{'rock', 'paper', 'scissor'}: #checks if these words are found in the input (if its valid or not)
        #use in operator with sets because faster excution speed
        invalid = False

cpu = choice (['rock', 'paper', 'scissor']) #data type set, chooses a random from this list
print(f"The CPU chose {cpu}")
#game logic
if player == cpu:
    print("Game is Tied")
else: 
    if player == 'rock':
        if cpu == 'paper':
            print("The CPU has won the game")
        else:
            print("The player has won the game")
    elif player == 'paper':
        if cpu == 'scissor':
            print ("The CPU has won the game")
        else:
            print("The player has won the game")
    else: #choice left is scissor 
        if cpu == "rock":
            print("The CPU has won the game")
        else: 
            print("The player has won the game")


    