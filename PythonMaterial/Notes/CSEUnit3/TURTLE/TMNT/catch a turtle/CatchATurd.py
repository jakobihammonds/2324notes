import turtle as t
import random as r
import Leaderboard as lb

#---global variables and objects---
#---game configuration--
wn = t.Screen()
score = 0
timer = 15
interval = 1000
total_clicks = 0
FILENAME = "db.txt"
fontSetup = ("Times New Roman", 30, "normal")

trent = t.Turtle()
trent.shape("turtle")
trent.shapesize(2)
trent.fillcolor("purple")
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

timeKeeper = t.Turtle()
timeKeeper.penup()
timeKeeper.teleport(-100, 200)
timeKeeper.pendown()
timeKeeper.speed(0)
timeKeeper.hideturtle()


#---functions--
def clickAccuracy():
     global total_clicks
     total_clicks +=1
     updateAccuracy()
     updateScore()

def trentClicked(x, y):
  global score, trent_size
  if trent_size > 0.5:
    trent_size *= 0.5
    trent.shapesize(trent_size)
  else:
    trent_size = 2
    trent.shapesize(trent_size)
  trent.penup()
  trent.setpos(x, y)
  trent.pendown()
  if trent_size == 2:
       trent.circle(20)
  elif trent_size ==1:
       trent.circle(10)
  elif trent_size==.5:
       trent.circle(5)
  moveTrent()
  

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


#
def updateAccuracy():
  scoreKeeper.teleport(170, 185)
  accuracy = score / total_clicks * 100
  accuracy = round(accuracy, 2)
  scoreKeeper.write(f"Accuracy: {accuracy}%", align="center")


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
  lb.drawLeaderboard(False, namesList, scoresList, scoreKeeper, 10)


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
trent.onclick(trentClicked)
wn.onscreenclick(clickAccuracy)
wn.listen()
wn.ontimer(startGame, 1000)

#--main loop---
wn.mainloop()

# Call drawLeaderboard function when timer reaches 0
if timer <= 0:
  leader_names = lb.getNames(FILENAME)
  leader_scores = lb.getScores(FILENAME)
  lb.drawLeaderboard(False, leader_names, leader_scores, scoreKeeper, score)
