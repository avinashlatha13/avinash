Python 3.6.2 (default, Jul 20 2017, 08:43:29) 
[GCC 6.3.0 20170406] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: /home/cl215/avinash_python_program/program11.py ==========
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
5 10 15 20
6 12 18 24
7 14 21 28
8 16 24 32
9 18 27 36
10 20 30 40
>>> #! /usr/bin/python3
import smtplib
s = smtplib.SMPT('smpt.gmail.com' ,587)
s.starttls()
s.login("avikannan13@gmail.com","kannan10")
message="how r u??"
s.sendmail("avikannan13@gmail.com","ashokmbl1999@gmail.com", message)
s.quit()
