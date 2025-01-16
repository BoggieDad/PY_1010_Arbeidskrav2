"""
Created on Tue Jan 14 19:23:58 2025

@author: Borgar Stenseth
e-post: borgar.stenseth@gmail.com
Revision: Rev01
"""

#%% Oppgave nummer 1

year_reference = 2024

year_born = int(input("Hvilket år blei du født? "))
year_old = year_reference - year_born
print("Du er", year_old, " år gammel i", year_reference, "når du er født i år", year_born)


#%% Oppgave nummer 2

import math

antall_elever = int(input('Skriv inn antall elever:'))

pizza = antall_elever / 4
print ("Antall pizza'er vi har behov for når det kommer", antall_elever, "elevr er", math.ceil(pizza), "stykk pizza'er")


#%% Oppgave nummer 3

import numpy as np

v_grad = float(input("Skriv inn gradtallet:"))
v_rad = v_grad*np.pi/180
print("Når vi har ", round(v_grad), "grader tilsvarer det", round(v_rad, 2), "radianer")

#%% Oppgave nummer 4a

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

#%% Oppgave nummer 4b

# Be brukeren om å skrive inn et av de listede landene

valgt_land = (input("Skriv inn landet Norge, England, Frankrike eller Italia: "))
land = data[valgt_land]
hovedstad = land[0]
innb = land[1]

print(hovedstad, "er hovedstaden i", valgt_land, "og det er", innb, "mill. innbyggere i", hovedstad,".")
# Alternativ printout
print(f"{hovedstad}, er hovedstaden i {valgt_land} og det er {innb} mill. innbyggere i {hovedstad}")

#%%Oppgave 4C

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

# Funksjon for å legge til data i biblioteket
def legg_til_data():
    while True:
        nytt_land = input("Skriv inn et land (eller 'stopp' for å avslutte): ")
        if nytt_land.lower() == 'stopp':
            break
        if nytt_land in data:
            print(f"{nytt_land} finnes allerede i biblioteket med hovedstaden {data[nytt_land][0]} og {data[nytt_land][1]} millioner innbyggere.")
        else:
            hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
            innbyggere = float(input(f"Skriv inn antall innbyggere (i millioner) i {nytt_land}: "))
            data[nytt_land] = [hovedstad, innbyggere]
            print(f"{nytt_land} er nå lagt til i biblioteket, med følgende parametre, {data[nytt_land][0]} og {data[nytt_land][1]} millioner innbyggere.")
            #print(hovedstad, "er hovedstaden i", valgt_land, "og det er", innb, "mill. innbyggere i", hovedstad, ".")

# Kall funksjonen for å begynne å legge til data
legg_til_data()


#%% Oppgave 5

import math


katet_1 = int(input("skriv inn det korteste katetet i en rettvinklet trekant: "))
katet_2 = int (input("skriv inn det lengste katetet i en rettvinklet trekant: "))

# Formel areal sirkel som i oppgaven
areal_sirk = math.pi*((katet_1/2)**2)
print("arealet av en halvsirkel er: ", round(areal_sirk,2))

# Formel omkrets av en sirkel som i oppgaven

omk_sirk = math.pi*2*(katet_1/2)
print("Omkretsen av en halvsirkel er: ", round(omk_sirk,2))

# Formel areal av trekant
areal_trek = (katet_1*katet_2)/2
print("arealet av en trekant i denne oppgaven er: ", round(areal_trek,2))

# Formel omkrets av trekant basert på at vi vet minste katet

katet_2_omk = math.sqrt(katet_1*3)
hypot = 2*katet_1

omk_trek = katet_1 + katet_2_omk + hypot
print("arealet av en trekant i denne oppgaven er: ", round(omk_trek,2))

# Summary of the different kalkulasjonene over

tot_areal = areal_sirk + areal_trek
tot_omk = omk_sirk + omk_trek

print("")
print("Basert på utregningene over har vi følgende utregninger")
print("Samlet areal for trekant og halvsirkel i denne oppgaven er: ", round(tot_areal, 2),".")
print("Samlet omkrets for trekant og halvsirkel i denne oppgaven er: ", round(tot_omk, 2),".")

#%% Oppgave 6

import numpy as np
import matplotlib.pyplot as plott

x = np.linspace(-10,10,200)

print(x)

f_x = -x**2-5
plott.plot(f_x)
plott.show()