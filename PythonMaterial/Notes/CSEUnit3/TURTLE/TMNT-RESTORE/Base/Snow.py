#Snow.py
import turtle as t
import random as r
#
wn = t.Screen()
wn.bgcolor("sky blue")
#
snowFlakes = []
#Create Turtles
for i in range(10):
    snowFlakes.append(t.Turtle(shape='turtle'))
print(snowFlakes)
#
#Save Turtles

#
#Iterate through list

#
#Move Turtles
for s in snowFlakes:
    s.teleport(r.randint(-300,300),r.randint(0,300))
while True:
    for s in snowFlakes:
        speedX, speedY = r.randint(-10,10),r.randint(-10,0)
        newX=s.xcor()-speedX
        newY=s.ycor()-speedY
        s.teleport(newX,newY)
        if s.ycor() < -300:
            s.color("red")
            s.stamp()
            s.teleport(r.randint(-300,300),r.randint(0,300))
            s.color("black")





wn.mainloop()

