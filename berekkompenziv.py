"""Név;Neme;Részleg;Belépés;Bér"""
#Beri Dániel;férfi;beszerzés;1979;222943

#1-2 feladat:


class Berek:
    def __init__(self,sor):
        sor = sor.strip().replace(",",".").split(";")
        self.nev = str(sor[0])
        self.neme = str(sor[1])
        self.reszleg = str(sor[2])
        self.belepes = int(sor[3])
        self.ber = int(sor[4])
        
with open("berek2020.txt","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Berek(sor) for sor in f]
    
#3 feladat:
    
print(f"3:feladat: Dolgozók száma: {len(lista)} fő")

#4 feladat:

atlag_berek = [sor.ber for sor in lista]
ossz = sum(atlag_berek)
atlag = ossz / len(lista)
vegeredmeny = atlag / 1000

print(f"4:feladat: Bérek átlaga: {vegeredmeny:.1f} eFt")

#5 feladat:

bekeres = input("5.feladat: Kérem egy részleg nevét:\t")

#6 feladat:

legnagyobb = 0
for sor in lista:
    if bekeres == sor.reszleg:
        if sor.ber > legnagyobb:
            legnagyobb = sor.ber
            nev = sor.nev
            neme = sor.neme
            belepes = sor.belepes
            ber = sor.ber
    else:
        print("6.feladat: A megadott részleg nem létezik a cégnél")
        break
