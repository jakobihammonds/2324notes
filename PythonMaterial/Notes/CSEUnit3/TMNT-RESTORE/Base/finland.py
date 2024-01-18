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



turt.goto(-250,37)




turt.fillcolor("blue") 
turt.begin_fill() 
turt.fd(500)
turt.rt(90)
turt.fd(75)
turt.rt(90)
turt.fd(500)
turt.rt(90)
turt.fd(75)
turt.rt(90)

turt.end_fill() 
turt.penup()
turt.goto(-100,0)
turt.pendown()
turt.fillcolor("blue") 
turt.begin_fill() 

turt.goto(-150,0)
turt.lt(90)
turt.fd(150)
turt.rt(90)
turt.fd(75)
turt.rt(90)
turt.fd(300)
turt.rt(90)
turt.fd(75)
turt.rt(90)
turt.fd(150)

turt.end_fill() 

turt.penup()
turt.goto(-250,150)
turt.pendown()
turt.rt(90)
turt.fd(500)
turt.rt(90)
turt.fd(300)
turt.rt(90)
turt.fd(500)
turt.rt(90)
turt.fd(300)

turt.hideturtle()





#last line
wn.mainloop()