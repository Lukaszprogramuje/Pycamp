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
#print(liczby_do_losowania)
liczby = set(random.sample(liczby_do_losowania, 6))
print(f"moje liczby {moje}")
print(f"wylosowane liczby {liczby}")
ile_trafionych = 0
for i in moje:
    if i in liczby:
        print(f'trafione {i}')
        ile_trafionych += 1
if ile_trafionych == 6:
    print("brawo wylosowałeś wszystkie 6 liczb")
    wygrana += szostka
if ile_trafionych == 5:
    print("brawo masz 5")
    wygrana += piatka
    ile_piatek += 1
if ile_trafionych == 4:
    print("brawo masz 4")
    wygrana += czworka
    ile_czworek += 1
if ile_trafionych == 3:
    print("brawo masz 3")
    wygrana += trojka
    ile_trojek += 1
