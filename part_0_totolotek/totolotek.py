import random

koszt_zakladu = 3
wygrana = 0
licznik_losowan = 0
trojka = 10
ile_trojek = 0
czworka = 170
ile_czworek = 0
piatka = 5300
ile_piatek = 0
szostka = 2000000
moje = {10, 13, 18, 23, 35, 42}
#6 liczb od 1 do 49
# co tydzien 1 losowanie, porównujemy ze swoimi
# ile tygodni trzeba grać aby wylosować 6

liczby_do_losowania = range(1, 50)

def losowanie(liczby_do_losowania):
    wylosowane = set(random.sample(liczby_do_losowania, 6))
    return wylosowane

def test_losowanie():
    #given
    #when
    wylosowane = sorted(list(losowanie(liczby_do_losowania)))
    #then
    assert len(wylosowane) == 6
    assert wylosowane[0] >= 1
    assert wylosowane[-1] <= 49

def sprawdzanie_wynikow(moje, wylosowane):
    trafione = 0
    for i in moje:
        if i in wylosowane:
            trafione += 1
    return trafione

def sprawdzanie_wygranej(wynik):
    global ile_trojek
    global ile_czworek
    global ile_piatek
    global wygrana
    if wynik == 6:
        wygrana += szostka
    if wynik == 5:
        wygrana += piatka
        ile_piatek += 1
    if wynik == 4:
        wygrana += czworka
        ile_czworek += 1
    if wynik == 3:
        wygrana += trojka
        ile_trojek += 1

if __name__ == "__main__":
    wynik = 0
    while wynik < 6:
        wylosowane = losowanie(liczby_do_losowania)
        wynik = sprawdzanie_wynikow(moje, wylosowane)
        sprawdzanie_wygranej(wynik)
        licznik_losowan += 1
    
    koszt_calkowity = licznik_losowan * koszt_zakladu

    print(f"trójek =          {ile_trojek:9}")
    print(f"czwórek =         {ile_czworek:9}")
    print(f"piątek =          {ile_piatek:9}")
    print(f"calkowity koszt = {koszt_calkowity:9,} zł")
    print(f"wygrana =         {wygrana:9,} zł")
    print(f"potrzeba było     {licznik_losowan:9,} losowań")
    if koszt_calkowity > wygrana:
        print(f"straciłeś         {koszt_calkowity - wygrana:9,} zł")
    elif koszt_calkowity < wygrana:
        print(f"zyskałeś          {wygrana - koszt_calkowity:9,}")
    else:
        print("po wszystkim wyszedłeś na 0")
