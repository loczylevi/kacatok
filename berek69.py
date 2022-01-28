"""     Név;   Neme; Részleg; Belépés; Bér"""
'''Beri Dániel;férfi;beszerzés;1979;222943'''
'''     0         1       2      3     4    '''

class Berek2020:
    def __init__(self,sor):
        s = sor.strip().replace(",",".").split(";")
        self.nev = str(s[0])
        self.neme = str(s[1])
        self.reszleg = str(s[2])
        self.belepes = int(s[3])
        self.ber = int(s[4])
        
#1-2-feladat____________________________________________________

with open("berek2020.txt","r",encoding="UTF-8") as f:
    elso_sor = f.readline()
    lista = [Berek2020(sor) for sor in f]
    
#3-feladat____________________________________________________

print(f"3.feladat: Dolgozók száma: {len(lista)} fő ")

#4-feladat____________________________________________________

atlag = [sor.ber for sor in lista]
ossz = sum(atlag)
atlag3 = ossz / len(atlag)
atlag4 = atlag3 / 1000

print(f"4.feladat Bérek átlaga: {atlag4:.1f} eFt")

#5-feladat____________________________________________________

bekeres = input("5.feladat: Kérem egy részleg nevét:")

#6-feladat____________________________________________________

maxber = 0
for sor in lista:
    if bekeres == sor.belepes:
        if  sor.ber > maxber:
            nagyobb = sor.ber
            if nagyobb > sor.ber:
                nagyobb = sor.ber
    elif bekeres != sor.belepes:
        print("6.feladat: A megadott részleg nem létezik a cégnél!")
        break

                

        


        