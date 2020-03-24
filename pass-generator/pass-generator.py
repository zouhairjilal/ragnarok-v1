from random import randint
import os
clear = lambda: os.system("clear")
clear()
print ('\n\033[1;36;48m' "                                     ██    ██                                    ")
print ('\033[1;36;48m ' "                                  ▄██████████▄                                 ")
print ('\033[1;36;48m ' "                                 ████ ████ ████                                ")
print ('\033[1;36;48m ' "                                  ▀█▀██████▀█▀                                 ")
print ('\033[1;36;48m ' "                                   ██▄▄▄▄▄▄██                                  ")
print ('\033[1;36;48m ' "                                    Fsociety                                   ")
print ('\033[1;36;48m ' "                   ============================================                  ")
print ('\033[1;36;48m ' "==================| Welcome To Zouhair Program, Please Sign In |==================")
print ('\033[1;36;48m ' "                   ============================================                  ")

soso1 = randint(125, 163)
soso2 = randint(125, 163)
soso4 = randint(1990, 2020)
lol1 = randint(20, 34)
lol2 = randint(125, 163)
lol3 = randint(234, 315)
lol4 = randint(1990, 2020)
inputer = input("Enter Your Password : ")

print ("")
print ("Low Security ####>", inputer ,"_" ,lol1 )
print ("Medium security ####>", inputer, "_", lol2 )
print ("High Security ####>", soso1 , "#", inputer, "#", lol3 )
print ("Ultra High Security ####>","=>" ,soso4 , "@_.", inputer ,"._&", lol4 ,"<=" )
print ("")
inputer = input ('To Exit Click [ENTER >]')
lol = os.system("cd /home/zouhair/Desktop/zouhair/ && python3 center.py")
if inputer == "" :
    print (lol)







