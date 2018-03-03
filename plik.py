#! /usr/bin/python

import re # wyrazenia regularne
import os # import os
import sys

x=sys.argv[1] # chodzi o uniwersalnosc programu, aby zmienne definiowac w konsoli
                #dziala po wpisaniu w konsoli ./plik.py lorem.txt

print 'ala ma kota'
plik="lorem.txt"

# liczymy linie, ktore zawieraja dane slowo

marzec=0

for linia in file(plik):
    if linia.find("bash")>=0:
        marzec=marzec+1
print marzec

# kolejny warunek, liczymy linie o okreslonej dlugosci (80)

y=0

for w in file(plik):
    if len(linia)==80: # za pomoca len liczymy
        y=y+1
print y

# za pomoca wyrazen regularnych liczymy linie, w ktorych sa liczby

x=0

for lin in file(plik):
    if re.search("[0-9]+", lin): # nalezy zaimportowac re
        x=x+1
print x

# czy program wygenerowal okreslony plik, czy plik instnieje

if os.path.exists(plik): # sprawdza czy plik istnieje, aby uzyc nalezy zaimportowac os
    print "plik istnieje"
else:
    print "plik nie istnieje"

if os.path.exists("jakis_nieistniejacy_plik.txt"):
    print "plik istnieje"
else:
    print "plik nie istnieje"
