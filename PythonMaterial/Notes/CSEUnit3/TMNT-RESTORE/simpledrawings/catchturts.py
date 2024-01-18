#
import turtle as t
import random as r
#
wn = t.Screen()
trent = t.Turtle()
trent.shape("turtle")
trent.shapesize(2)
trent.fillcolor("purple")
trent.speed(0)
#
def trentClicked(x,y):
    print("Trent was clicked.")
    print(x,y)
    moveTrent()
#
def moveTrent():
   # width,height=t.screensize()
   # print(width,height)
    newX=r.randint(-300,300) 
    newY=r.randint(-300,300)
    trent.goto(newX,newY)
    
trent.onclick(trentClicked)
#
#
wn.mainloop()
#