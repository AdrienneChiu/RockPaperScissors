from random import randint

#This game is case-sensitive!

#player choices
m = ["Scissors", "Paper", "Rock"]

#assign random move for computer
com = m[randint(0,2)]

#set player false
player = False

while player == False:

# Set player true
    player = input("Choose Rock, Paper, or Scissors \nYou entered: ")

# When player enters a tie
if player == com:
    print("Tie!")

# when player plays rock
elif player == "Rock":
    if com == "Paper":
        print("Computer entered: Paper\nYou lose!", com, "covers", player)
    else:
        print("You win!", player, "smashes", com)

# When player plays paper
elif player == "Paper":
    if com == "Scissors":
        print("Computer entered: Scissors\nYou lose!", com, "cut", player)
    else:
        print("You win!", player, "covers", com)

# When player plays scissors
elif player == "Scissors":
    if com == "Rock":
        print("Computer entered: Rock\nYou lose!", com, "smashes", player )
    else:
        print("You win!", player, "cut", com)

# When player enters wrong choice
else:
    print("Invalid play, try again")

#Set player back to false to continue the loop
player = False
com = m[randint(0,2)]