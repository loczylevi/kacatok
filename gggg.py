"""�v;Elem;Vegyjel;Rendsz�m;Felfedez�"""

#1-2.feladat_______________________________________________
class Kemia:
  def __init__(self,sor):
    s = sor.strip().split(";")
    self.ev = s[0]
    self.elem = s[1]
    self.vegyjel = s[2]
    self.rendszam = int(s[3])
    self.felfedezo = s[4]


with open("felfedezesek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Kemia(sor) for sor in f]

#3.feladat_______________________________________________

#print(f"3.feladat: Az elemek száma: {len(lista)}")
    
#4.feladat_______________________________________________
'''
okor = [sor.ev for sor in lista if sor.ev == "Ókor"]

print(f"4.feladat: Felfedezések az ókorban: {len(okor)}")
'''
#5.feladat_______________________________________________


bekeres = input('5. feladat: Kérek egy vegyjelet: ')
        

"""�v;Elem;Vegyjel;Rendsz�m;Felfedez�"""
#6.feladat_______________________________________________
print("6.feladat: Keresés")
"""
lista2 = []
for sor in lista:
    if bekeres == sor[2]:
     ev = sor[0]
     elem = sor[1]
     vegyjel = sor[2]
     felfedezo = sor[4]
     rendszam = sor[3]
     lista2.append(elem)
     lista2.append(vegyjel)
     lista2.append(felfedezo)
     lista2.append(rendszam)

    
    
if len(lista2) == 0:
  print("6.feladat: Nincs ilyen elem az adatforrásban")
else:
  print(f'''  Az elem vegyjele: {vegyjel}'
             Az elem neve: {elem}
             Rendszáma: {rendszam}
             Felfedezés éve: {ev}
             felfedezo : {felfedezo}
             ''')

"""

evek = [ int(sor.ev) for sor in lista if sor.ev != "Ókor"]
duf = [ evek[i+1] - evek[i] for i, ev in enumerate(evek) if i < len(evek)-1]
print('7. feladat:', max(duf), 'év volt a leghosszabb időszak két elem felfedezése között.' )



