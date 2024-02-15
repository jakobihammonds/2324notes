import turtle as t
import random as r
import Leaderboard as lb

#---global variables and objects---
#---game configuration--
wn = t.Screen()
wn.bgpic("bg.gif")
score = 0
timer = 15
interval = 1000
total_clicks = 0
FILENAME = "db.txt"
fontSetup = ("Times New Roman", 30, "normal")
wn.addshape("gold.gif")
wn.addshape("silver.gif")
wn.addshape("bronze.gif")

bronze=t.Turtle()
bronze.hideturtle()
bronze.teleport(-250,200)
silver=t.Turtle()
silver.hideturtle()
silver.teleport(-250,200)
gold=t.Turtle()
gold.hideturtle()
gold.teleport(-250,200)

trent = t.Turtle()
trent.shape("turtle")
trent.shapesize(2)
trent.speed(0)
trent_size = 2
trent.hideturtle()
trent.penup()

scoreKeeper = t.Turtle()
scoreKeeper.penup()
scoreKeeper.teleport(100, 200)
scoreKeeper.pendown()
scoreKeeper.speed(0)
scoreKeeper.hideturtle()

accKeeper = t.Turtle()
accKeeper.penup()
accKeeper.teleport(100, 200)
accKeeper.pendown()
accKeeper.speed(0)
accKeeper.hideturtle()

timeKeeper = t.Turtle()
timeKeeper.penup()
timeKeeper.teleport(-100, 200)
timeKeeper.pendown()
timeKeeper.speed(0)
timeKeeper.hideturtle()


#---functions--


def trentClicked(x, y):
  global score, trent_size
  trent.fillcolor("white")
  trent.begin_fill()
  trent.stamp()
  trent.end_fill()
  trent.fillcolor("maroon")
  if trent_size > 0.5:
    trent_size *= 0.5
    trent.shapesize(trent_size)
  else:
    trent_size = 2
    trent.shapesize(trent_size)
  trent.penup()
  trent.setpos(x, y)
  trent.pendown()

  moveTrent()
  updateScore()
  updateAccuracy()
  


def moveTrent():
  newX = r.randint(-300, 300)
  newY = r.randint(-300, 300)

  while abs(newX - 100) < 50 or abs(
      newY - 200) < 50:  # Checking for overlap with scoreKeeper
    newX = r.randint(-300, 300)
    newY = r.randint(-300, 300)

  while abs(newX +
            100) < 50 or abs(newY +
                             200) < 50:  # Checking for overlap with timeKeeper
    newX = r.randint(-300, 300)
    newY = r.randint(-300, 300)

  wn.bgcolor("red")
  trent.teleport(newX, newY)
  wn.bgcolor("white")


def updateScore():
  global score
  scoreKeeper.teleport(100, 200)
  score += 1
  scoreKeeper.clear()
  scoreKeeper.write(f"Score: {score}", font=fontSetup)


#
# Add parentheses to function calls in CatchATurd.py to update score and accuracy correctly



#
def updateAccuracy(x,y):
  global total_clicks
  total_clicks += 1
  accKeeper.teleport(170, 185)
  accKeeper.clear()
  accuracy = score / total_clicks * 100
  accuracy = round(accuracy, 2)
  accKeeper.write(f"Accuracy: {accuracy}%", align="center")


def startGame():
  start = wn.textinput("Start Game", "Press Enter to Start")
  if start == "":
    updateTimer()
    trent.showturtle()
  else:
    wn.bye()


def manageLeaderboard():
  global score
  namesList = lb.getNames("db.txt")
  scoresList = lb.getScores("db.txt")
  if score >= int(scoresList[-1]):
    playerName = input("Congrats, you made the leaderboard!\n\tName Please:")
    lb.updateLeaderboard("db.txt", namesList, scoresList, playerName, score)
    if lb.lbPos == 1:
      gold.showturtle()
    elif lb.lbPos == 2:
      silver.showturtle()
    elif lb.lbPos == 3:
      bronze.showturtle()
  lb.drawLeaderboard(False, namesList, scoresList, scoreKeeper, score)
  
  
def updateTimer():
  global timer
  timer -= 1
  timeKeeper.clear()
  if timer <= 0:
    timeKeeper.write("Time's Up!", font=fontSetup)
    trent.hideturtle()
    manageLeaderboard()
  else:
    timeKeeper.write(f"Time: {timer}", font=fontSetup)
    timeKeeper.getscreen().ontimer(updateTimer, interval)

#
#---events---
wn.onscreenclick(updateAccuracy)
trent.onclick(trentClicked)
wn.ontimer(startGame, 1000)


#--main loop---
wn.mainloop()

# Call drawLeaderboard function when timer reaches 0
