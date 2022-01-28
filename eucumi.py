#1-2 feladat
"""Ausztria;1995.01.01"""
with open("EUcsatlakozas.txt", "r") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3. feladat: EU agállamainak száma - db.
print(f"3. feladat: EU agállamainak száma {len(lista)} db.")


#4. feladat: 2007-ben - ország csatlakozott

szamlalo = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo += 1
        
print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott")

#5. feladat: Magyarország csatlakozási dátuma: -
taroltdatum = None
for sor in lista:
    if sor[0] == "Magyarország":
        taroltdatum = sor[1][0:10]
        
print(f"5. feladat: Magyarország csatlakozási dátuma: {taroltdatum}")


#6. feladat: Májusban volt csatlakozás
volt_e = False
for sor in lista:
    if sor[1][5:7] == "05":
        volt_e = True
print(sor[1][5:7])
        
if volt_e:
    print(f"6. feladat: Májusban volt csatlakozás")
else:
    print(f"6. feladat: Májusban nem volt csatlakozás")
