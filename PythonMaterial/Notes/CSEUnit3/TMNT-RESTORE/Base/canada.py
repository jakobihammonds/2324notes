#Importing module with name "t"

import turtle as t
#put into window
wn = t.Screen()

wn.addshape('leef.gif')

#turt Program
#object = module.Constructor() - makes 1 turt
turt = t.Turtle()
turt.speed(0)
turt.shape('turtle')
leef = t.Turtle()
leef.shape('leef.gif')
leef.hideturtle()
leef.penup()
leef.goto(50,-100)


turt.goto(-200,0)

turt.fillcolor("red") 
turt.begin_fill() 

for i in range(2):
    turt.fd(150)
    turt.rt(90)
    turt.fd(350)
    turt.rt(90)  
turt.end_fill() 

turt.fd(350)
turt.rt(90)
turt.fd(350)
turt.rt(90)
turt.fd(200)
turt.rt(90)
turt.fd(350)

turt.fillcolor("red") 
turt.begin_fill() 
turt.rt(90)
turt.fd(350)
turt.rt(90)
turt.fd(350)
turt.rt(90)
turt.fd(150)
turt.rt(90)
turt.fd(350)
leef.goto(50,-175)
leef.showturtle()



turt.end_fill() 
turt.hideturtle()





#last line
wn.mainloop()