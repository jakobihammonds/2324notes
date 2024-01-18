from turtle import *

#

horiTurds=[]
vertTurds=[]

#

turtleShapes = ["arrow","turtle","circle","square","triangle","classic"]
horiColors = ["red","blue","green","orange","purple","gold"]
vertColors = ["darkred","darkblue","lime","salmon","indigo","brown"]
#
spacing = 50
for eachShape in turtleShapes:
    ht = Turtle(shape=eachShape)
    ht.speed(0)
    ht.penup()
    ht.fillcolor(horiColors.pop())
    ht.setheading(0)
    ht.goto(-250,spacing)
    horiTurds.append(ht)
    
    vt = Turtle(shape=eachShape)
    vt.speed(0)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.setheading(270)
    vt.goto(-spacing,250)
    vertTurds.append(vt)
    
    spacing+=25
#

def checkForCollision(h,v,collisionDistance):
    if (abs(v.xcor()-h.xcor()) < collisionDistance):
        if(abs(v.ycor() - h.ycor()) < collisionDistance):
            horiTurds.remove(h)
            vertTurds.remove(v)
            h.fillcolor("gray")
            v.fillcolor("gray")
    h.xcor()
    h.ycor()
    
    
distanceToMove = 1
for step in range(100):
    for eachH in horiTurds:
        for eachV in vertTurds:
            eachH.fd(distanceToMove)
            eachV.fd(distanceToMove)
            checkForCollision(eachH,eachV,5)
#
wn = Screen()
wn.mainloop()