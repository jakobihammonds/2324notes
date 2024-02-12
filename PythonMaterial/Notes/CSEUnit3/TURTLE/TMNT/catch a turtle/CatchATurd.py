#---import statements---
import turtle as t
import random as r
import Leaderboard as lb
import time as c




#---global variables and objects---
#---game configuration--
wn=t.Screen()
wn.addshape("turtle.gif")
score=0
timer=15
interval=1000
screenClicks = -1
gameOn = False
FILENAME="db.txt"
#    tuple("font style",fontSize,"font type - bold, italic, normal")
fontSetup=("Times New Roman",30,"normal")

trent = t.Turtle()
trent.shape("turtle.gif")
trent.shapesize(4)
trent.speed(0)
trent.penup()

scoreKeeper = t.Turtle()
scoreKeeper.penup()
scoreKeeper.teleport(100,200)
scoreKeeper.pendown()
scoreKeeper.speed(0)
scoreKeeper.hideturtle()   #still writes, but can't see the turtle

timeKeeper = t.Turtle()
timeKeeper.penup()
timeKeeper.teleport(-100,200)
timeKeeper.pendown()
timeKeeper.speed(0)
timeKeeper.hideturtle()   #still writes, but can't see the turtle

#
start = t.Turtle()
start.teleport(-100,200)
start.pendown()
start.speed(0)
start.hideturtle()
start.write(f"Click to start",font=fontSetup)
#---functions---
def trentClicked(x,y):
     # print(x,y)
     moveTrent()
     updateScore()

def moveTrent():
     # width,height=t.screensize()
     # print(width,height)
     newX=r.randint(-300,300)
     newY=r.randint(-300,300)
     trent.goto(newX,newY)
          
     

def updateScore():
     global score
     score+=1
     #write the score to the screen
     scoreKeeper.clear()
     scoreKeeper.write(f"Score: {score}",font=fontSetup)  #drawing the score

def screenClicked(x,y):
     global screenClicks
     wn.bgcolor("red")  #this runs anytime the screen or turt is clicked
     c.sleep(.3)
     wn.bgcolor("white")
     screenClicks += 1
     global gameOn
     gameOn = True
     start.clear()
     #


     
#game over function............
def manageLeaderboard():
     global score
     namesList=lb.getNames("db.txt")
     scoresList=lb.getScores("db.txt")
     #if the current score is in the leaderboard
     if score >= int(scoresList[-1]):                  #[-1] grabs last item in list
     #    update the leaderboard
          playerName=input("Congrats, you made the leader board!\n\tName Please:")
          lb.updateLeaderboard("db.txt",namesList,scoresList,playerName,score)
     #draw the leaderboard
     lb.draw_leaderboard(False,namesList,scoresList,scoreKeeper,10)

def updateTimer():
     global timer
     #subtract one from the time
     timeKeeper.clear()
     if gameOn == True:
          timer-=1
     #draw the time to the screen
          
          if timer<=0:
               timeKeeper.write("Time's Up!",font=fontSetup)
               trent.hideturtle()
               manageLeaderboard()
          else:
               timeKeeper.write(f"Time: {timer}",font=fontSetup)
               timeKeeper.getscreen().ontimer(updateTimer,interval)        #example of recursion


     
#---events---   Gold Block from MIT Event Handlers
#object.method(command)
trent.onclick(trentClicked)    
wn.onclick(screenClicked)
wn.ontimer(updateTimer,interval)
#in turtle, all objects are clickable 

#

#--main loop---
wn.mainloop()


'''
     Features List:
     1. Click a turtle
     2. Move turtle randomly
     3. Score
     4. Timer
     5. High Score
'''