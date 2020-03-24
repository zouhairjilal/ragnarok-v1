import os
import zox
from getpass import getpass

def login():
    clear = lambda : os.system("clear")
    clear()
    namer = "zouhair"
    passer = "jilal"
    namer1 = "admin"
    passer1 = "admin123"
    Name = input("enter your name: ")
    Pass = getpass("enter your password: ")

    if Name == namer and Pass == passer or Name == namer1 and Pass == passer1 :
        print("Name And Password Is Correct")
        zox.logo()
        zox.nember()
        
    else:
        print("Try Again")
        login()

login()

