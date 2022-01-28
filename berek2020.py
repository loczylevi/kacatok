

''' indexelés miatt: Név;Neme;Részleg;Belépés;Bér'''
p2v = lambda x:x.replace('.',',')
#1.es feladat - 2 es feladat
with open("berek2020.txt", "r",encoding="utf-8") as f:
    elso_sor = f.readline()
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))

#3. feladat
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")
#4.es feladat

bersum = []
for sor in lista:
    bersum.append(int(sor[-1]))
    atlag = f'{(sum(bersum) / len(bersum)) / 1000:.1f}'
print(f"4.feladat: Bérek átlaga: {p2v(atlag)} efr")
    


#5
reszleg = input("5.feladat: Kérem egy részleg nevét: ")
#6
maxber = 0
taroltsor = ''
for sor in lista:
    if reszleg in sor:
        ber = int(sor[-1])
        if ber > maxber:
            maxber = ber
            taroltsor = sor
print("Feladat 6")
if taroltsor:
    print(f"                Név: {taroltsor[0]}")
    print(f"                Neme: {taroltsor[1]}")
    print(f"                Belépés: {taroltsor[3]}")
    print(f"                bér: {taroltsor[-1]} forint ")
else:
    print("6.feladat: A megadott részleg nem létezik a cégnél!")
                