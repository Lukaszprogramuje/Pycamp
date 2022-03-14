import random

koszt_zakladu = 3
koszt_calkowity = 0
wygrana = 0
tygodnie = 0
trojka = 10
ile_trojek = 0
czworka = 170
ile_czworek = 0
piatka = 5300
ile_piatek = 0
szostka = 2000000
losowanie = set()
moje = {10, 13, 18, 23, 35, 42}
#6 liczb od 1 do 49
# co tydzien 1 losowanie, porównujemy ze swoimi
# ile tygodni trzeba grać aby wylosować 6

liczby_do_losowania = set()
for i in range(1, 50):
    liczby_do_losowania.add(i)

def losowanie(liczby_do_losowania):
    wylosowane = set(random.sample(liczby_do_losowania, 6))
    return wylosowane

def sprawdzanie_wynikow(moje, wylosowane):
    trafione = 0
    for i in moje:
        if i in wylosowane:
            trafione += 1
    return trafione

wynik = 0
while wynik < 6:
    wylosowane = losowanie(liczby_do_losowania)
    wynik = sprawdzanie_wynikow(moje, wylosowane)
    koszt_calkowity += koszt_zakladu
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

print(f"trojek = {ile_trojek}")
print(f"czworek = {ile_czworek}")
print(f"piatek = {ile_piatek}")
print(f"calkowity koszto = {koszt_calkowity}")
print(f"wygrana = {wygrana}")
print(f"ile losowan = {koszt_calkowity/koszt_zakladu}")

