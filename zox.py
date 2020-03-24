import os
import sys
clear = lambda : os.system("clear")

def logo():
    clear()
    print ('\n\033[1;36;48m' "      ██████╗   █████╗   ██████╗  ███╗  ██╗  █████╗  ██████╗   █████╗  ██╗  ██╗    ")
    print ('\033[1;36;48m ' "     ██╔══██╗ ██╔══██╗ ██╔════╝  ████╗ ██║ ██╔══██  ██╔══██╗ ██╔══██╗ ██║ ██╔╝    ")
    print ('\033[1;36;48m ' "     ██████╔╝ ███████║ ██║  ▄▄▄  ██╔██╗██║ ███████║ ██████╔╝ ██║  ██║ █████═╝     ")
    print ('\033[1;36;48m ' "     ██╔══██╗ ██╔══██║ ██║   ██╗ ██║╚████║ ██╔══██║ ██╔══██╗ ██║  ██║ ██╔═██╗     ")
    print ('\033[1;36;48m ' "     ██║  ██║ ██║  ██║ ╚██████╔╝ ██║ ╚███║ ██║  ██║ ██║  ██║ ╚█████╔╝ ██║ ╚██╗    ")
    print ('\033[1;36;48m ' "     ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚══╝ ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚════╝  ╚═╝  ╚═╝    ")
    print ('\033[1;36;48m ' "                 ============================================                  ")
    print ('\033[1;36;48m ' "================| Welcome To Zouhair Program, Please Sign In |=================")
    print ('\033[1;36;48m ' "                 ============================================                  ")

def nember():
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "1" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ' , "Secure Password Generator") 
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "2" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Facebooker")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "3" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Hash-Md5")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "4" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Hash-sha1")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "5" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Hash-sha224")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "6" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Hash-sha256")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "7" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "Hash-sha384")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "8" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "9" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "10" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "")
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "11" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ', "")
    #----------------------------00) Exit------------------------------#
    print ('\033[1;32;48m ' , "[" , "\033[1;35;48m " , "00) Exit" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ')
    inputer = int(input("####> "))
    
    if inputer == 1 :
        one = os.system("cd /home/zouhair/Desktop/zouhair/tools/pass-generator && python3 pass-generator.py")
        print(one)
        sys.exit(43)
    elif inputer == 2 :
        two = os.system("cd /home/zouhair/Desktop/zouhair/tools/facebooker && perl facebooker.pl")
        print(two)
        sys.exit(43)
    elif inputer == 3 :
        three = os.system("cd /home/zouhair/Desktop/zouhair/tools/hash && python hash-md5.py")
        print(three)
        sys.exit(43)
    elif inputer == 4 :
        four = os.system("cd /home/zouhair/Desktop/zouhair/tools/hash && python hash-sha1.py")
        print(four)
        sys.exit(43)
    elif inputer == 5 :
        five = os.system("cd /home/zouhair/Desktop/zouhair/tools/hash && python hash-sha224.py")
        print(five)
        sys.exit(43)
    elif inputer == 6 :
        six = os.system("cd /home/zouhair/Desktop/zouhair/tools/hash && python hash-sha256.py")
        print(six)
        sys.exit(43)
    elif inputer == 7 :
        seven = os.system("cd /home/zouhair/Desktop/zouhair/tools/-hash && python hash-sha384.py")
        print(seven)
        sys.exit(43)
    elif inputer == 8 :
        eight = os.system("")
        print(eight)
        sys.exit(43)
    elif inputer == 9 :
        nine = os.system("")
        print(nine)
        sys.exit(43)
    elif inputer == 10 :
        ten = os.system("")
        print(ten)
        sys.exit(43)
    
    elif inputer ==  00:
        print ('\033[1;33;48m ' , "[" , "\033[1;35;48m " , "+" , '\033[1;32;48m ' , "]" , '\033[1;33;48m ' , "Thanks for using Ragnarok\n" , '\033[1;33;48m ' , "[" , "\033[1;35;48m " , "+" , '\033[1;32;48m ' , "]" , '\033[1;33;48m '"Good By....." )
        print (sys.exit(43))
    else:
        logo()
        nember()




    
 















