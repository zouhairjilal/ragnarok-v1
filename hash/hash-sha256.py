import hashlib

def hashing_method( passwd_hash ) :
    hash1 = hashlib.sha256 ( passwd_hash )
    print '\n\033[1;36;48m' '                                                    .::!!!!!!!:.               '
    print '                 .!!!!!:.                        .:!!!!!!!!!!!!                '
    print '                 ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$                '
    print '                     :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P                '
    print '                     $$$$$##WX!:      .<!!!!UW$$$$   $$$$$$$$#                 '
    print '                     $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*                   '
    print '                     ^$$$B  $$$$      $$$$$$$$$$$$   d$$R*                     '
    print '                       **$bd$$$$       *$$$$$$$$$$$o+#                         '
    print '                            ****          *******                              '
    print '                                Fsociety                                       '
    print '\033[1;32;48m ' '                 ============================================                  '
    print '================| Welcome To Zouhair Program, Please Sign In |================='
    print '                 ============================================                  '
    print 'your hashed password is: ', hash1.hexdigest() 

def main():
    print 'Password hashing script'
    passwd_hash = raw_input ('enter your password : ')
    hashing_method(passwd_hash)
if __name__ == '__main__':
        main()

inputer = raw_input ('To Exit Click [ENTER >]')
lol = os.system("cd /home/zouhair/Desktop/zouhair/ && python3 center.py")
if inputer == "" :
    print lol