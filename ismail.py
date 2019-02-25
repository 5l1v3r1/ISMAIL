#!/usr/bin/python
########################################
# Script : ismail                      #
#    JOB : Verify Email Address Checker#
# CodedBy: Oseid Aldary                #
########################################
#
#Colors#
#
rd="\033[1;31m"
gr="\033[1;32m"
yl="\033[1;33m"
wi="\033[1;37m"
#
#
#Libraries#
try:
    from os import system as sy; import mechanize,socket,optparse 
    sy("")
except ImportError:
    print(rd+"\n["+yl+"!"+rd+"] "+yl+"Error: Please Install [ "+gr+"Mechanize"+yl+" ] "+rd+" !!!"+wi)
    print(wi+"["+gr+"*"+wi+"] Use This Command:>"+gr+" pip install mechanize"+wi)
    exit(1)
#
# Check Internet Connection #
def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False
#
#Check-Email-Function#
#

def ISMAIL(email):
    global br
    try:
        br.open("https://verifyemailaddress.com/")
        br.select_form(nr=0)
        br["email"]=email
        res = br.submit()
        if "is valid" in res.get_data():
            print(wi+"["+gr+"+"+wi+"] Email["+gr+email+wi+"] STATUS["+gr+" Found "+wi+"]")
        else:
            print(yl+"["+rd+"-"+yl+"] Email["+rd+email+yl+"] STATUS["+rd+" Not Found "+yl+"]"+wi)
    except(KeyboardInterrupt,EOFError):
        print(wi+" ")
        exit(1)

parse = optparse.OptionParser("""
USAGE: python ./ismail.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------                                                           
    |  -s --single [Email]                 ::> Check Single Email   
    |--------
    |  -m --many   [Email,Email2,etc]      ::> Check Many Emails
    |--------
    |  -f --file   [Email_file]            ::> Check All Emails From File
-------------
Examples:
        |
     |--------
     | python ismail.py -s oseid@gmail.com
     |--------
     | python ismail.py -m Oseid@gmail.com,ahmad.m@gmail.com,Omar@hotmail.com
     |--------
     | python ismail.py -f emails.txt
     |--------
""")
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_robots(False)
def Main():
    parse.add_option('-s','-S','--single','--SINGLE', dest="Smail",type="string")
    parse.add_option('-m','-m','--many','--MANY', dest="Mmail",type="string")
    parse.add_option('-f','-F','--file','--FILE', dest="Fmail",type="string")
    (opt,args) = parse.parse_args()
    if opt.Smail !=None:
        if cnet() !=True:
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Please Check Your Internet Connection "+rd+"!!!"+wi)
            exit(1)
        email = opt.Smail
        if not email.strip() or "@" not in email:
            print(yl+"\n["+rd+"!"+yl+"] Invalid Email["+rd+email+yl+"] STATUS["+rd+" SKIPPED "+yl+"]"+wi)
            exit(1)
        email = email.strip()
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        ISMAIL(email)
    elif opt.Mmail !=None:
        if cnet() !=True:
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Please Check Your Internet Connection "+rd+"!!!"+wi)
            exit(1)
        many_email = opt.Mmail
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        if ',' in many_email:
            emails = many_email.split(",")
        else:
            print(yl+"\n["+rd+"!"+yl+"] Error: Please Use[ "+wi+","+yl+" ] To Split The Emails"+rd+" !!!"+wi)
            exit(1)
        try:
            for email in emails:
                if not email.strip() or "@" not in email: continue
                email = email.strip()
                ISMAIL(email)
        except (KeyboardInterrupt,EOFError):
            print(wi+" ")
            exit(1)
            
    elif opt.Fmail !=None:
        emails_file = opt.Fmail
        print(gr+"["+yl+"~"+gr+"]"+yl+" Checking....\n"+wi)
        try:
            fop = open(emails_file, "r")
        except IOError:
            print(yl+"\n["+rd+"!"+yl+"]"+yl+" No Such File: "+rd+emails_file+wi)
            exit(1)
        try:
            for email in fop:
                if not email.strip() or "@" not in email: continue
                email = email.strip()
                ISMAIL(email)
            fop.close()
        except (KeyboardInterrupt,EOFError):
            print(wi+" ")
            exit(1)
    else:
        print(parse.usage)
        exit(1)

if __name__=="__main__":
    Main()

##############################################################
##################### 		        ##########################
##################### END OF SCRIPT ##########################
#####################               ##########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye
