#bekeres = input("Adj meg egy változot")
valtozo = "Zorglub"
pacekos_valtozo = None
hossz = len(valtozo) - 1
lista = []
while True:
  pacekos_valtozo = valtozo[hossz]
  lista.append(pacekos_valtozo)
  hossz = hossz - 1
  if hossz == -1:
    break

uj = ""
hossz2 = len(valtozo) - 1
while True:
  uj = lista[hossz2] + uj
  hossz2 = hossz2- 1
  if hossz2 == -1:
    break
  
print(uj)



