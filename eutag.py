#Ausztria;1995.01.01
with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3feladat
print(f"3.feladat: EU agállamainak száma: {len(lista)} db")

#4 feladat
szamlalo = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo += 1

print(f"4.feladat: 2007-ben {szamlalo} ország csatlakozott")
    
for sor in lista:
    if sor[1][5:7] == "05":
        alap = sor[1][5:7]
        
print(alap)

# 5 .feladat
for sor in lista:
    if sor[0][0:12] == "Magyarország" :
        datum = sor[1][0:9]
        
print(f"5.feladat: Magyarország csatlakozási dátuma: {datum}")

#6 feladat
zaszlo = False
for sor in lista:
    if sor[1][5:7] == "05":
        zaszlo = True
if zaszlo:
    print("6.feladat: Májusban volt csatlakozás!")
else:
    print("6.feladat: Májusban nem volt csatlakozás!")


print("\"")

