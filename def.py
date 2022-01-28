import math
def cuccmok(x,y):
    gyokvonas = math.sqrt(x**2 + y**2)
    return gyokvonas

def cuccmok2(x,y,z):
    gyokvonas2 = math.sqrt(x**2 + y**2 + z**2)
    return gyokvonas2

def cuccmok3(x,y,z,n):
    gyokvonas3 = math.sqrt(x**2 + y**2 + z**2 + n**2)
    return gyokvonas3

x = int(input("kérek egy számot\t"))
y = int(input("kérek egy másik számot\t"))
z = int(input("kérem a 3. számot\t"))
n = int(input("kérem a 4. számot\t"))
t = cuccmok(x,y)
print(f"A két szám: {x} és {y} eredménye: {t}")
t2 = cuccmok2(x,y,z)
print(f"A három szám: {x} és {y} meg a {z} eredménye: {t2}")
t3 = cuccmok3(x,y,z,n)
print(f"A négy szám: {x} és {y} meg a {z} és a {n} eredménye: {t3}")
