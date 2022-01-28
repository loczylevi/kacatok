"""Ausztria;1995.01.01"""

#1-2.feladat

with open("EUcsatlakozas.txt", "r",encoding="latin2") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3.feladat
        
print(f"3.feladat: EU tagállamainak száma: {len(lista)} db")

#4.feladat

hany2007 = [sor for sor in lista if sor[1][0:4] == "2007"]
hany = len(hany2007)

print(f"4.feladat: 2007-ben {hany} ország csatlakozott")

#5.feladat

magyarorszag = [sor[1][0:12] for sor in lista if sor[0] == "Magyarország"]

print(f"5.feladat:Magyarország csatlakozási dátuma: {magyarorszag[0]}")

#6.feladat

majus = [sor for sor in lista if sor[1][5:7] == "05"]

if len(majus) > 0:
    print("6.feladat Májusban volt csatlakozás!!!")
else:
    print("6.feladat Májusban nem volt csatlakozás!!!")

#7.feladat
legkisebb = 0
taroltsor = ""
for sor in lista:
    if int(sor[1][0:4]) > legkisebb:
        legkisebb = int(sor[1][0:4])
        taroltsor = sor[0]
        
print(f"7.feladat: Legutoljára csatlakozott ország: {taroltsor}")

#8.feladat___________________________________________________________

stat = dict()
for sor in lista:
    orszag = sor[1][0:12]
    stat[orszag] = stat.get(orszag, 0) + 1
print("8:feladat: Ország statisztika")
for orszag,darab in stat.items():
    print(f"     {orszag[0:4]} - {darab} db") 






        