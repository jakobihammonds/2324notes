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
    turt.fd(500)
    turt.rt(90)
    turt.fd(100)
    turt.rt(90)  
turt.end_fill() 

turt.fillcolor("yellow") 
turt.begin_fill() 
for i in range(2):
    turt.fd(500)
    turt.lt(90)
    turt.fd(100)
    turt.lt(90) 
turt.lt(90)
turt.fd(100)
turt.end_fill() 

turt.fillcolor("red") 
turt.begin_fill() 

turt.fd(100)
turt.rt(90)
turt.fd(500)
turt.rt(90)
turt.fd(100)
turt.end_fill() 


turt.penup()
turt.goto(15,0)
turt.pendown()
turt.rt(18)
turt.fillcolor("black") 
turt.begin_fill() 

for i in range(5):
        turt.backward(100)
        turt.right(144)
turt.end_fill() 



(random.random(),
                      random.random(),
                      random.random())      
    

#put into window
wn = t.Screen()



#last line
wn.mainloop()