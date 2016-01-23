__author__ = 'Luka'
import os
import requests

def shrani(naslov, ime_dat):
    r = requests.get(naslov)
    try:
        with open(ime_dat , 'w', encoding= 'UTF8') as dat:
            dat.write(r.text)
    except:
        os.makedirs(ime_dat)
        with open(ime_dat , 'w', encoding= 'UTF8') as dat:
            dat.write(r.text)

def pripravi_slovar(ime_dat):
    with open(ime_dat, 'w', encoding= 'UTF8') as dat:
        print('treba se narest')


def vsebina_datoteke(ime_datoteke):
    '''Vrne niz z vsebino datoteke z danim imenom.'''
    with open(ime_datoteke) as datoteka:
        vsebina = datoteka.read()
        return vsebina