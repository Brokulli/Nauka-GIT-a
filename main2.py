def wypisz_koszatniczki(imie1, imie2):
    print("{0} {1}". format(imie1, imie2))

def ilosc_koszakow(ilosc):
    MAX = 2
    if ilosc > MAX:
        return False
    else:
        return True

if __name__=="__main__":
    gatunek = "koszatniczka"
    rodzaj = "ssak"
    ilosc = 2
    imie1 = "Bazyl"
    imie2 = "Pixel"
    print(gatunek + " to " + rodzaj)

    if ilosc < 1:
        print("Za malo zwierzakow")
    else:
        print("Wystarczajaco duzo zwierzakow")
