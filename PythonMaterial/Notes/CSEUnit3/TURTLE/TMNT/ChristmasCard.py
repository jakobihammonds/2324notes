#Importing module with name "t"

import turtle as t
import random as r


#turt Program
wn = t.Screen()
wn.bgcolor("white")
wn.screensize(1000,1000)
snow = 0
#picture
santa = t.Turtle()
wn.addshape('image.gif')
santa.shape('image.gif')
#object = module.Constructor() - makes 1 turt
turt = t.Turtle()

turt.shape('circle')
turt.pendown()
for turtles in range(60):
    snow = t.Turtle()
    snow.shape("circle")
    snow.color("gray")
    snow.teleport(x=(r.randint(-500,500)),y=(r.randint(-500,500)))
#put into window




#last line
wn.mainloop()