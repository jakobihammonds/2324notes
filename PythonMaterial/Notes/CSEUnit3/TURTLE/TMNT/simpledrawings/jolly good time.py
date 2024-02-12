#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
# parallel list is when two list are same length and the items coorelate
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]*2
turtle_colors = ["red", "green", "blue", "orange", "purple", "gold"]*2
#for loop creates all of the turtle
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  newColor = turtle_colors.pop(0)   #grabs the last color from the list and removes it
  t.color(newColor)
  my_turtles.append(t)

#original spot  
startx = 0
starty = 0

#moves the turtles to final starting location
h=45
d=50
for t in my_turtles:
  t.teleport(startx,starty)#t.goto(startx, starty)
  t.right(h)     
  t.forward(d)
  h+=45
  d+=5
  
     #adding 50 to the original spot for the next turtle	
  startx = t.xcor()#startx + 50
  starty = t.ycor()#starty + 50


#    FOLLOW THE LEADER
while True:
          #nextX and nextY need to come from the next turtle in the list
     for i in range(len(my_turtles)-1):
          nextX=my_turtles[i+1].xcor()
          nextY=my_turtles[i+1].ycor()
          my_turtles[i].teleport(nextX,nextY)

wn = trtl.Screen()
wn.mainloop()