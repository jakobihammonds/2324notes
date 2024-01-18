import turtle as t
import random

mikey = t.Turtle()
mikey.shape("square")
mikey.speed(0)   #0 == 'fastest' and 0 is faster than 1-9

wn = t.Screen()
#import image of Mariah
wn.addshape('image.gif')  #will load in an image from a file in your directory

mariah = t.Turtle()
mariah.shape('image.gif')
mariah.speed(1)

def drawAPoly(sides):
     mikey.pendown()
     mikey.pensize(10)
     for i in range(sides):
          mikey.color(random.random(),
                      random.random(),
                      random.random())
          mikey.fd(50)
          mikey.rt(360/sides)
     mikey.penup()

#moves mikey without the trail
def moveMikey(x,y):
     mikey.penup()
     mikey.goto(x,y)
     mikey.pendown()

mikey.penup()
mikey.goto(-250,200)
mikey.pendown()
drawAPoly(8)
mikey.goto(-300,375)
drawAPoly(27)

#laser firing from the death star thing
moveMikey(-225,125)
mikey.fillcolor("green")
mikey.color("green")
mikey.begin_fill()
mikey.circle(25)
mikey.end_fill()

#a turtle to say "run away!"
writer=t.Turtle()
writer.penup()
writer.goto(0,200)
writer.write("Run Away!",font=('segoe script',50,'normal'))

mariah.goto(400,-400)

mikey.goto(400,-400)
mikey.shapesize(30,30)



wn.mainloop()