import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.color("darkorchid")
painter.goto(20,180)

for loop in range(4):
     # draw flower
     painter.color("darkorchid")
     painter.goto(20,180-loop*20)

     #petal is a local variable
     for petal in range(18):
          if petal % 2 == 1:           #alternating
               painter.color("red")
          else:
               painter.color("black")
          #painter.right(20)
          painter.forward(30-8*loop)
          painter.stamp()
  
#wn is a turtle.screen obj
wn = trtl.Screen()
wn.mainloop()