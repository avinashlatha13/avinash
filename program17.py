#!/usr/bin/python3
from random import randint
t= ["stone","paper","scissors"]
computer = t[randint(0,2)]
player = str(input("enter the choice:"))

if player ==computer:
         print("draw") 
elif player =="paper":
            if computer =="scissors":
                print("lose","computer has",computer);
            else:
                print("won","computer has",computer)
elif player =="scissors":
            if computer =="stone":
               print("lose","computer has",computer)
            else:
                print("won","computer has",computer)
elif player =="stone" :
             if computer =="paper":
                 print("lose","computer has",computer)
             else:
                 print("won","computer has",computer)               
