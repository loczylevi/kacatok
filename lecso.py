import random
lista = ["tank","cámá",]
tipp = 0
kivalaszt = random.choice(lista)
c = len(kivalaszt)
eredmeny = []

while True:
  bekeres = input("kérek egy betüt!\t")
  kereso = [szo for szo in kivalaszt if bekeres == szo]
  if len(kereso) == 0:
      print("Nincs ilyen betű a szóban!")
      kereso = '000000'
  for betu in kivalaszt:
    if kereso[0] == betu:
     eredmeny.append(betu)
     tipp = tipp + 1
     print(f"Ez a betű: {bekeres} szerepel a szóban!\nEredmeny: {eredmeny}")
     if c == tipp:
       print(f"Gratulálok! kitaláltad a szót! : {kivalaszt} ")
       break

