# Név;Neme;Részleg;Belépés;Bér
p2v = lambda x:x.replace(".",",")
with open("berek2020.txt","r",encoding="utf-8") as f:
    f.readline()
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
#3.feladat
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")
bersum = []
#4.feladat
for sor in lista:
    bersum.append(int(sor[-1]))
    atlag = f"{sum(bersum) / len(bersum) / 1000:.1f}"
print(f"4.feladat: Bérek átlaga: {(p2v(atlag))} efr")

#5 feladat
bekeres = input("5.feladat: Kérem egy részleg nevét!")

#f6eladat
taroltsor = ""
maxber = 0
for sor in lista:
    if bekeres > maxber:
        ber = int(sor[0])
        if ber > maxber:
            maxber = ber
            taroltsor = sor
        
        