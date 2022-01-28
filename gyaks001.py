"""Ausztria;1995.01.01"""

#1-2.feladat____________________________________________________________

with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3.feladat____________________________________________________________        
        
print(f"3.feladat: EU tagállamainak száma: {len(lista)}")

#4.feladat____________________________________________________________        

szamlalo = 0

for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo += 1
        
print(f"4.feladat: 2007-ben {szamlalo} ország csatlakozott")

#5.feladat____________________________________________________________        

taroltsor = ""
for sor in lista:
    if sor[0] == "Magyarország":
        taroltsor = sor[1]
        
print(f"5.feladat: Magyarország csatlakozási dátuma: {taroltsor}")

#6.feladat____________________________________________________________        

majusban = False

for sor in lista:
    if sor[1][5:7] == "05":
        majusban = True
        
if majusban:
    print("6.feldat: Volt májusban csatlakozás!")
else:
    print("6.feladat: Nem volt májusban csatlakozás!")
    
#7.feladat____________________________________________________________        

legutso = 0
for sor in lista:
    if int(sor[1][0:4]) > legutso:
        legutso = int(sor[1][0:4])
        orszag = sor[0]
        
print(f"7.feladat: Legutoljára csatlakozott ország: {orszag}")