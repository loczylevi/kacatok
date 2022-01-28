"""Csapat;Helyezes;Valtozas;Pontszam
Anglia;4;0;1662"""

class Fifa_vilagranglista:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.csapat = str(sor[0])
        self.helyezes = int(sor[1])
        self.valtozas = int(sor[2])
        self.pontszam = int(sor[3])
        
with open("fifa.txt","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Fifa_vilagranglista(sor) for sor in f]
    
#3.feladat
    
print(f"3.feladat: A világranglistán {len(lista)} csapat szerepel")

#4.feladat:

atlag_csapat = [sor.pontszam for sor in lista]

ossz = sum(atlag_csapat)
atlag = ossz / len(lista)

print(f"4.feladat: A csapatok átlagos pontszáma: {atlag:.2f}")

#5.feladat:

legkisebb = 0
for sor in lista:
    if sor.valtozas > legkisebb:
        legkisebb = sor.valtozas
        helyezes = sor.helyezes
        csapat = sor.csapat
        pontszam = sor.pontszam
        
print(f'''
5. feladat: A legtöbbet javító csapat:
        Helyezés: {helyezes}
        Csapat: {csapat}
        Pontszám : {pontszam}
''')

#6.feladat:

magyarorszag = [sor for sor in lista if sor.csapat == "Magyarország"]
van_e = len(magyarorszag)

if van_e == 0:
    print("6.feladat: A csapatok között nincs Magyarország")
else:
    print("6.feladat: A csapatok között van Magyarország")
    

