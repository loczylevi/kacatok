import math
from math import sqrt
import random
import turtle
wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Monte Carro Szimuláció")
alex = turtle.Turtle()
alex.penup()
alex.shape("circle")
alex.speed(100)
szamlalo = 0
for szam in range(100000):
    vx = random.randint(-400,400)
    vy = random.randint(-400,400)
    alex.goto(vx,vy)
    d = math.sqrt(vy**2 + vx**2)
    if d > 400:
        alex.color("blue")
        alex.stamp()
    else:
        alex.color("red")
        szamlalo = szamlalo + 1
        alex.stamp()
        
pi = 4 * szamlalo / szam