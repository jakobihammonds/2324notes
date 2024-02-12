#Importing module with name "t"

import turtle as t
import random

#turt Program
#object = module.Constructor() - makes 1 turt
turt = t.Turtle()

turt.shape('turtle')

turt.goto(-200,0)

turt.fillcolor("green") 
turt.begin_fill() 

for i in range(2):
    turt.fd(150)
    turt.rt(90)
    turt.fd(350)
    turt.rt(90)  
turt.end_fill() 

turt.fd(300)
turt.rt(90)
turt.fd(350)
turt.rt(90)
turt.fd(150)
turt.rt(90)
turt.fd(350)

turt.fillcolor("orange") 
turt.begin_fill() 
turt.rt(90)
turt.fd(300)
turt.rt(90)
turt.fd(350)
turt.rt(90)
turt.fd(150)
turt.rt(90)
turt.fd(350)




turt.end_fill() 




#put into window
wn = t.Screen()



#last line
wn.mainloop()