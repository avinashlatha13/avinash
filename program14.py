#!/usr/bin/python3
n = int(input("Enter a integer: "))
print("the divisor of the number are:")
for i in range(1,n):
 	  if(n%i==0):
 	      print(i)
