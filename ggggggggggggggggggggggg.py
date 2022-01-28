import turtle
tabla = turtle.Turtle()
tabla.speed(0)

for i in range(4):
   tabla.forward(400)
   tabla.right(90)
   
a = 0
b = 0
for i in range(8):
    if(b == 0):
      a=1
    else:
      a=0
    for j in range(8):
       tabla.penup()
       tabla.goto(j*50, i*50*(-1))
       tabla.pendown()
       if(a==0):
          tabla.fillcolor('black')
          a=1
       else:
          tabla.fillcolor('white')
          a=0
       tabla.begin_fill()
       for s in range(4):
          tabla.forward(50)
          tabla.right(90)
       tabla.end_fill()
    if(b==0):
        b=1
    else:
        b=0