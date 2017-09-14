#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("press r to roll dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("ur random number",r)
		print("ur on",count)
	if count==8:
		count=37
		print("u have climbed to",count)
	elif count==13:
		count=34
		print("u have climbed to",count)
	elif count==40:
		count=68
		print("u have climbed to",count)
	elif count==52:
		count=81
		print("u have climbed to",count)
	elif count==76:
		count=97
		print("u have climbed to",count)
	elif count==11:
		count=2
		print("u have down to",count)
	elif count==25:
		count=4
		print("u have down to",count)
	elif count==38:
		count=9
		print("u have down to",count)
	elif count==65:
		count=46
		print("u have down to",count)
	elif count==89:
		count=70
		print("u have down to",count)
	elif count==93:
		count=64
		print("u have down to",count)
	elif count>=100:
		print("u have won")