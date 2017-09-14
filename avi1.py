#!/usr/bin/python3
from random import randint

t = ["stone", "Paper", "Scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
#set player to False
player = False
 
while player == False:
#set player to True
    player = input("stone, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "stone":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "stone":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
            print("won the game")
    