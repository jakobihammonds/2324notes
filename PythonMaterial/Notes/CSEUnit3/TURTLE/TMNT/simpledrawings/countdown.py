
import turtle as t


wn=t.Screen()
timer=10
interval=1000
fontSetup=("times New Roman",30,"normal")

timeKeeper = t.Turtle()
timeKeeper.penup()
timeKeeper.teleport(100,200)
timeKeeper.pendown()
timeKeeper.speed(0)
timeKeeper.hideturtle()


#functions
def updateTimer():
    global timer
    #subtract one from the time
    time-=1
    #draw the time to the screen
    timeKeeper.clear()
    timeKeeper.write(f"Time: {timer}",font=fontSetup)
    #iterate our loop
    #turtleobject, get the screen you are on, and get the timer and run this command after this interval
    #example recursion
    timeKeeper.getscreen().ontimer(updateTimer,interval)

#events
#object.method()
#wn.ontime(command, how oftenToRun)
wn.ontimer(updateTimer, interval)

#mainloop
wn.mainloop()