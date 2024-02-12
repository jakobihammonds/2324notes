import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)


# change pen
painter.penup()
painter.shape("square")
painter.turtlesize(2)


for loop in range(1):
     # draw flower
     painter.color("darkorchid")
    
    
     painter.goto(-160,160-loop*20)

     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("black")
          else:
               painter.color("red")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()
          
     painter.goto(-160,120-loop*20)
          
     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("red")
          else:
               painter.color("black")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()
    
     painter.goto(-160,80-loop*20)

     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("black")
          else:
               painter.color("red")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()
          
     painter.goto(-160,40-loop*20)
          
     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("red")
          else:
               painter.color("black")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()     

    
     painter.goto(-160,0-loop*20)

     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("black")
          else:
               painter.color("red")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()
          
     painter.goto(-160,-40-loop*20)
          
     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("red")
          else:
               painter.color("black")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()     


    
     painter.goto(-160,-80-loop*20)

     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("black")
          else:
               painter.color("red")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()
          
     painter.goto(-160,-120-loop*20)
          
     for petal in range(8):
          if petal % 2 == 1:           #alternating
               painter.color("red")
          else:
               painter.color("black")
          #painter.right(20)
          painter.forward(40)
          painter.stamp()     




#wn is a turtle.screen obj
wn = trtl.Screen()
wn.mainloop()