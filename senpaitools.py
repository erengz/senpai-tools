# senpailegal tarafından derlenip kodlanmıştır.

# compiled and coded by senpailegal.





import os

import time

from termcolor import colored

import requests

import proxybroker

from googlesearch import search

import sys

import warnings

import random

from http import cookiejar



os.system("clear")



#

baslik = "\033[0;31m\033[1m[\033[0;32m\033[1mSenpai-Tools\033[0;31m\033[1m]>\033[1m\033[0;32m "



# Renkler

sifirla = "\033[0m"

kirmizi = "\033[1;31m"

yesil = "\033[1;32m"

cyan = "\033[1;36m"



# Semboller

yildiz = kirmizi + "[" + yesil + "*" + kirmizi + "]" + sifirla

arti = kirmizi + "[" + yesil + "+" + kirmizi + "]" + sifirla

eksi = kirmizi + "[" + yesil + "-" + kirmizi + "]" + sifirla

bulundu = kirmizi + "[" + yesil + "BULUNDU" + kirmizi + "]" + sifirla

bulunamadi = kirmizi + "[" + yesil + "BULUNAMADI" + kirmizi + "]" + sifirla

soru_isareti = kirmizi + "[" + yesil + "?" + kirmizi + "]" + sifirla

unlem = kirmizi + "[" + yesil + "!" + kirmizi + "]" + sifirla



menu = "\033[1m" + """





                             _   _              _     

  ___ ___  _ _   _ __  __ _ (_) | |_  ___  ___ | | ___

 (_-</ -_)| ' \ | '_ \/ _` || | |  _|/ _ \/ _ \| |(_-<

 /__/\___||_||_|| .__/\__,_||_|  \__|\___/\___/|_|/__/

                |_|                                   



                   

\033[0;31m[\033[0;33mWRN USE FOR EDUCATIONAL PURPOSES! \033[0;31m] \033[0;32m\033[1m 

   

\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32m\033[1mAğ Taramasi

\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32m\033[1mSitede Zaafiyet Tespiti

\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32m\033[1mSubDomain Tespiti

\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32m\033[1mBilgi Toplama

\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32m\033[1mFirewall Tespiti

\033[0;31m[\033[0;33mx\033[0;31m]> \033[0;32m\033[1mÇıkış

"""

print(colored(menu, "red"))

try:

    while True:

        islem = input(baslik)



        if (islem == "1"):



            print("""\033[0;31m[\033[0;33m*\033[0;31m]> \033[1;32mNmap Tarama bölümüne hoş geldiniz.

\033[0;31m[\033[0;33m1\033[0;31m]> \033[0;32mNormal Tarama

\033[0;31m[\033[0;33m2\033[0;31m]> \033[0;32mHızlı Tarama

\033[0;31m[\033[0;33m3\033[0;31m]> \033[0;32mAgresif Tarama

\033[0;31m[\033[0;33m4\033[0;31m]> \033[0;32mAğı Tarama

\033[0;31m[\033[0;33m5\033[0;31m]> \033[0;32mToplu Tarama

\033[0;31m[\033[0;33m6\033[0;31m]> \033[0;32mAğdaki IP Adreslerini Öğrenme

\033[0;31m[\033[0;33m7\033[0;31m]> \033[0;32mServis ve Versiyon Bilgisi

\033[0;31m[\033[0;33m8\033[0;31m]> \033[0;32mİşletim Sistemi Bilgisi

\033[0;31m[\033[0;33m9\033[0;31m]> \033[0;32mAna Menüye Dön

            """)



            try:

                while True:

                    soru = input(baslik)



                    if (soru == "1"):

                        ip = input(yildiz + " Hedef IP: ")

                        os.system("nmap " + ip + " --open")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "2"):

                        ip = input(yildiz + " Hedef IP: ")

                        os.system("nmap " + ip + " -Pn -sS -n -v --top-ports 20 --open")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "3"):

                        ip = input(yildiz + " Hedef IP: ")

                        os.system("nmap " + ip + " -A")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "4"):

                        ip = input(yildiz + " Ağ Adresiniz (ör:192.168.1.0/24): ")

                        os.system("nmap " + ip)

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "5"):

                        liste = input(yildiz + " Hedef IP listeniz (ör:ips.txt): ")

                        os.system("nmap iL" + liste)

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "6"):

                        ip = input(yildiz + " Ağ Adresiniz (ör:192.168.1.0/24): ")

                        os.system("nmap " + ip + " -sn -n -v --open")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "7"):

                        ip = input(yildiz + " Hedef IP: ")

                        os.system("nmap " + ip + " -sS -sV")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "8"):

                        ip = input(yildiz + " Hedef IP: ")

                        os.system("nmap " + ip + " -O | grep OS")

                        print(arti + " Tarama başarıyla tamamlandı.")



                    elif (soru == "9"):

                        print(arti + " Ana menüye dönülüyor...\n")

                        print(colored(menu, "green"))

                        break



                    else:

                        print(unlem + " Geçerli bir işlem seçiniz...")

                        time.sleep(2)



            except KeyboardInterrupt:

                print("""

Çıkış Yapılıyor...

                """)

                exit()



 

        elif (islem == "2"):

            try:

                while True:

                    print(yildiz + " Zaafiyet Tespiti bölümüne hoş geldiniz.")

                    print(yildiz + "Site linkini http://www.hedefsite.com/ şeklinde giriniz.")

                    link = input(yildiz + " Site Linki: ")

                    os.system("nikto -h " + link)

                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")

                    if (soru == "e"):

                        continue

                    elif (soru == "h"):

                        print("\n" + arti + " Ana menüye dönülüyor...")

                        time.sleep(2)

                        print(colored(menu, "green"))

                        break

                    else:

                        print("Geçerli bir işlem seçiniz.")

            except KeyboardInterrupt:

                print("""

Çıkış Yapılıyor...

                """)

                exit()



        elif (islem == "3"):



            try:

                while True:

                    print(yildiz + " Alt Alan Adı tespit bölümüne hoş geldiniz.")

                    hedef = input(yildiz + " Hedef Site (ör:google.com): ")

                    os.system("assetfinder --subs-only " + hedef + " | tee subdomains.txt")

                    print(arti + " Tarama başarıyla tamamlandı.")

                    print(arti + " Sonuçlar subdomains.txt dosyasına kaydedildi.")

                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")

                    if (soru == "e"):

                        continue

                    elif (soru == "h"):

                        print("\n" + arti + " Ana menüye dönülüyor...")

                        time.sleep(2)

                        print(colored(menu, "green"))

                        break

                    else:

                        print("Geçerli bir işlem seçiniz.")



            except KeyboardInterrupt:

                print("""

Çıkış Yapılıyor...

                """)

                exit()



        elif (islem == "4"):

            try:

                while True:

                    print(yildiz + " Bilgi Toplama bölümüne hoş geldiniz.")

                    print(yildiz + " Site linkini siteadi.com şeklinde giriniz.")

                    link = input(yildiz + " Site Linki: ")

                    os.system("dmitry -iwnse " + link)

                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")

                    if (soru == "e"):

                        continue

                    elif (soru == "h"):

                        print("\n" + arti + " Ana menüye dönülüyor...")

                        time.sleep(2)

                        print(colored(menu, "green"))

                        break

                    else:

                        print("Geçerli bir işlem seçiniz.")

            except KeyboardInterrupt:

                print("""

Çıkış Yapılıyor...

                                                """)

                exit()



        elif (islem == "5"):

            try:

                while True:

                    print(yildiz + " Firewall Tespiti bölümüne hoş geldiniz.")

                    print(yildiz + "Site linkini http://www.hedefsite.com/ şeklinde giriniz.")

                    link = input(yildiz + " Site Linki: ")

                    os.system("wafw00f -a -v " + link)

                    soru = input(soru_isareti + " Başka bir işlem yapmak ister misiniz? (e/h)")

                    if (soru == "e"):

                        continue

                    elif (soru == "h"):

                        print("\n" + arti + " Ana menüye dönülüyor...")

                        time.sleep(2)

                        print(colored(menu, "green"))

                        break

                    else:

                        print("Geçerli bir işlem seçiniz.")

            except KeyboardInterrupt:

                print("""

Çıkış Yapılıyor...

                                                """)

                exit()



        elif (islem == "x"):

            print(colored(unlem + " Çıkış Yapılıyor...", "red"))

            exit()



        elif (islem == "clear"):

            os.system("clear")



        elif (islem == "menu"):

            print(colored(menu, "green"))



        else:

            print(colored(unlem + " Geçerli bir işlem seçiniz!", "green"))

except KeyboardInterrupt:

    print(arti + """

Çıkış Yapılıyor...""")

    time.sleep(2)

    exit()

