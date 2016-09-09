__author__ = 'Luka'
import os
import requests
import csv

def shrani(naslov, ime_dat):
    r = requests.get(naslov)
    try:
        with open(ime_dat , 'w', encoding= 'UTF8') as dat:
            dat.write(r.text)
    except:
        os.makedirs(ime_dat)
        with open(ime_dat , 'w', encoding= 'UTF8') as dat:
            dat.write(r.text)

def slovar_csv(sez,ime_dat,kluci):
    with open (ime_dat, 'w') as csvfile:
        vrsta = csv.DictWriter(csvfile,fieldnames=kluci)
        vrsta.writeheader()
        for line in sez:
            vrsta.writerow(line)
