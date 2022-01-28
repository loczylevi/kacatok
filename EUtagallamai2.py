'''Ausztria;1995.01.01'''

#1-2.feladat _______________________________________________________

with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3.feladat _______________________________________________________
        
print(f"3.feladat: EU tagállamainka száma: {len(lista)} db.")

#4.feladat _______________________________________________________

szamlalo = 0
for sor in lista:
    if sor[1][0:4] == "2007":
        szamlalo += 1
        
print(f"4.feladat: 2007-ben {szamlalo} ország csatlakozott")


#5.feladat _______________________________________________________

datum = ""
for sor in lista:
    if sor[0] == "Magyarország":
        datum = sor[1][0:10]
        
print(f"5.feladat: Magyarország csatlakozási dátuma: {datum}")

#6.feladat _______________________________________________________

majusba_volt_e = False

for sor in lista:
    if sor[1][5:7] == '05':
        majusban_volt_e = True
        
if majusban_volt_e:
    print(f"6.feladat: Májusban volt csatlakozás!")
else:
    print(f"6.feladat: Májusban nem volt csatlakozás!")

#7.feladat _______________________________________________________
    
legnagyobb = 0

for sor in lista:
    if int(sor[1][0:4]) > legnagyobb:
        legnagyobb = int(sor[1][0:4])
        orszag = sor[0]
        
print(f"7.feladat: Legutoljára csatlakozott ország: {orszag}")
orszag11 = ""
legkisebb = 10000000000000000000000000000000000000
for sor in lista:
    if int(sor[1][0:4]) < legkisebb:
        legkisebb = int(sor[1][0:4])
        orszag11 = sor[0]
        
print(f"+1 apu.feladat: Elöször csatlakozott ország: {orszag11}")