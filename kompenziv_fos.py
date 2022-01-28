'''Ausztria;1995.01.01'''
#1-2.feladat_____________________________________________________________

with open("EUcsatlakozas.txt", "r",encoding="latin2") as f:
    lista= []
    for sor in f:
        lista.append(sor.strip().split(";"))

#3.feladat_________________________________________________________________

print(f"3.feladat: EU tagállamainak száma: {len(lista)} db")
    
#4.feladat_________________________________________________________________

eu2007 = [sor for sor in lista if sor[1][0:4]=="2007"]
eu2007_hany = len(eu2007)

print(f"4.feladat: 2007-ben {eu2007_hany} ország csatlakozott")

#5.feladat_________________________________________________________________

magyarorszag = [sor[1][0:12] for sor in lista if sor[0]== "Magyarország"]

print(f"5.feladat: Magyarország csatlakozási dátuma: {magyarorszag[0]}")

#6.feladat_________________________________________________________________

majusban = [sor for sor in lista if sor[1][5:7] == "05"]
if majusban:
    print("6.feladat: Májusban volt csatlakozás")
else:
    print("6.feladat: Májusban nem volt csatlakozás")

#7.feladat_________________________________________________________________
















