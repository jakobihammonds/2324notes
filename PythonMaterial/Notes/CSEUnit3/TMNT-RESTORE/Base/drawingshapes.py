#Importing module with name "t"

import turtle as t
import random

#Turtle Program
#object = module.Constructor() - makes 1 turtle
fartSmella = t.Turtle()

fartSmella.shape('square')
fartSmella.speed(0)

#put into window
wn = t.Screen()
wn.addshape('image.gif')




#fartSmella.fd(100)
#fartSmella.rt(90)
#fartSmella.fd(100)
#fartSmella.rt(90)
#fartSmella.fd(100)
#fartSmella.rt(90)
#fartSmella.fd(100)
#fartSmella.rt(90)

#for i in range(4):
#    fartSmella.fd(50)
#    fartSmella.lt(90)
#for i in range(4):
#    fartSmella.lt(90)
#   fartSmella.fd(25)
#for i in range(4):
#    fartSmella.rt(90)
#    fartSmella.fd(200)

#for i in range(5):
#    fartSmella.fd(100)
#    fartSmella.lt(72)

#for i in range(8):
#    fartSmella.fd(150)
#   fartSmella.rt(45)

def drawapoly(sides):
    fartSmella.pensize(10)
    for i in range(sides):
        fartSmella.color((r: random.random(0,255),
                          g: random.random(0,255),
                          b: random.random(0,255)))
        fartSmella.fd(50)
        fartSmella.rt(360/sides)  


fartSmella.penup()
fartSmella.goto(-250,200)
fartsmella.pendown()
drawapoly(8)
fartSmella.goto(-300,375)
drawapoly(27)

for i in range(360):
    fartSmella.fd(1)
    fartSmella.lt(1)

fartSmella.shape('image.png')
fartSmella.goto(400,-400)
#last line


wn.mainloop()