#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("avikannan13@gmail.com","kannan10")
message="tanku mam"
s.sendmail("avikannan13@gmail.com","suhail0rahim@gmail.com", message)
print("success")
s.quit()
