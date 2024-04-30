# --- import section
import turtle as t
import random as r
import time

# --- global variables or objects or game config
delay = 0.1
p1Body = []
p2Body = []
# Screen Set Up
wn = t.Screen()
wn.title("Snake")
wn.setup(width=600, height=600)
wn.bgcolor("black")
# Main Menu
main_menu = t.Turtle()
main_menu.speed(0)
main_menu.color("white")
main_menu.penup()
main_menu.hideturtle()
main_menu.goto(0, 50)
main_menu.write("Snake Game", align="center", font=("Courier", 24, "normal"))
main_menu.goto(0, 0)
main_menu.write("Press '1' for Single Player", align="center", font=("Courier", 16, "normal"))
main_menu.goto(0, -50)
main_menu.write("Press '2' for mpSetUp", align="center", font=("Courier", 16, "normal"))
# Player 1 Setup
headPlayer1 = t.Turtle(shape="square")
headPlayer1.speed(0)
headPlayer1.penup()
headPlayer1.direction = "stop"
headPlayer1.color("red")  # Set the initial color for Player 1
# Player 2 Setup
headPlayer2 = t.Turtle(shape="square")
headPlayer2.speed(0)
headPlayer2.penup()
headPlayer2.direction = "stop"
headPlayer2.color("blue")  # Set the initial color for Player 2
# Food Turtle
food = t.Turtle(shape="turtle")
food.speed(0)
food.penup()
food.goto(100, 100)  # Set the initial position of food for both players
food.color("red")

# Functions
def up(player):
    if player.direction != "down":
        player.direction = "up"

def down(player):
    if player.direction != "up":
        player.direction = "down"

def left(player):
    if player.direction != "right":
        player.direction = "left"

def right(player):
    if player.direction != "left":
        player.direction = "right"

# Move the head forward for both players
def movePlayer(player):
    if player.direction == "up":
        player.sety(player.ycor() + 20)
    elif player.direction == "down":
        player.sety(player.ycor() - 20)
    elif player.direction == "left":
        player.setx(player.xcor() - 20)
    elif player.direction == "right":
        player.setx(player.xcor() + 20)

def updateBodyParts(player, bodyParts):
    if len(bodyParts) > 0:
        newX = player.xcor()
        newY = player.ycor()
        tail = bodyParts[-1]
        tail.goto(newX, newY)
        bodyParts.insert(0, tail)
        bodyParts.pop()

def hideTheBodyParts(player, bodyParts):
    for eachBodyPart in bodyParts:
        eachBodyPart.goto(1000, 1000)
    bodyParts.clear()

# --- events
def spSetUp():
    global delay
    main_menu.clear()
    headPlayer1.color("red")
    headPlayer2.hideturtle()
    food.color("red")
    p2Body.delete()
    delay = 0.1
    wn.onkeypress(lambda: up(headPlayer1), "w")
    wn.onkeypress(lambda: down(headPlayer1), "s")
    wn.onkeypress(lambda: left(headPlayer1), "a")
    wn.onkeypress(lambda: right(headPlayer1), "d")
    runGame()

def mpSetUp():
    global delay
    main_menu.clear()
    headPlayer1.color("red")
    headPlayer2.color("blue")
    food.color("red")
    delay = 0.1
    wn.onkeypress(lambda: up(headPlayer1), "w")
    wn.onkeypress(lambda: down(headPlayer1), "s")
    wn.onkeypress(lambda: left(headPlayer1), "a")
    wn.onkeypress(lambda: right(headPlayer1), "d")
    wn.onkeypress(lambda: up(headPlayer2), "Up")
    wn.onkeypress(lambda: down(headPlayer2), "Down")
    wn.onkeypress(lambda: left(headPlayer2), "Left")
    wn.onkeypress(lambda: right(headPlayer2), "Right")
    runGame()
def togglePause():
    global delay
    if delay == 0:
        delay = 0.1
    else:
        delay = 0
# --- key bindings
wn.onkeypress(spSetUp, "1")
wn.onkeypress(mpSetUp, "2")
# Print directions for the user in the console
print("Player 1 controls: W (Up), S (Down), A (Left), D (Right), Q (Quit), P (Pause)")
print("Player 2 controls: Arrow Up, Arrow Down, Arrow Left, Arrow Right")
# --- main loop
def runGame():
    global delay
    # --- main loop
    while True:
        wn.update()
        # Check for wall collision for Player 1
        if (
            headPlayer1.ycor() > 290
            or headPlayer1.ycor() < -290
            or headPlayer1.xcor() < -290
            or headPlayer1.xcor() > 290
        ):
            hideTheBodyParts(headPlayer1, p1Body)
        # Check for wall collision for Player 2
        if (
            headPlayer2.ycor() > 290
            or headPlayer2.ycor() < -290
            or headPlayer2.xcor() < -290
            or headPlayer2.xcor() > 290
        ):
            hideTheBodyParts(headPlayer2, p2Body)
        # Check for food collision for Player 1
        if headPlayer1.distance(food) < 20:
            food.goto(r.randint(-290, 290), r.randint(-290, 290))
            bodyPart = t.Turtle(shape="square")
            bodyPart.speed(0)
            bodyPart.penup()
            bodyPart.color("red")  # Set the color for Player 1
            p1Body.append(bodyPart)
        # Check for food collision for Player 2
        if headPlayer2.distance(food) < 20:
            food.goto(r.randint(-290, 290), r.randint(-290, 290))
            bodyPart = t.Turtle(shape="square")
            bodyPart.speed(0)
            bodyPart.penup()
            bodyPart.color("blue")  # Set the color for Player 2
            p2Body.append(bodyPart)
        # Move the body parts for Player 1
        for i in range(len(p1Body) - 1, 0, -1):
            newX = p1Body[i - 1].xcor()
            newY = p1Body[i - 1].ycor()
            p1Body[i].goto(newX, newY)
        # Move the neck to the head for Player 1
        if len(p1Body) > 0:
            newX = headPlayer1.xcor()
            newY = headPlayer1.ycor()
            neck = p1Body[0]
            neck.goto(newX, newY)
        # Move the body parts for Player 2
        for i in range(len(p2Body) - 1, 0, -1):
            newX = p2Body[i - 1].xcor()
            newY = p2Body[i - 1].ycor()
            p2Body[i].goto(newX, newY)
        # Move the neck to the head for Player 2
        if len(p2Body) > 0:
            newX = headPlayer2.xcor()
            newY = headPlayer2.ycor()
            neck = p2Body[0]
            neck.goto(newX, newY)
        # Move the head forward for both players
        movePlayer(headPlayer1)
        movePlayer(headPlayer2)
        # Check for body collision for Player 1
        for eachBodyPart in p1Body:
            if headPlayer1.distance(eachBodyPart) < 10:
                hideTheBodyParts(headPlayer1, p1Body)
        # Check for body collision for Player 2
        for eachBodyPart in p2Body:
            if headPlayer2.distance(eachBodyPart) < 10:
                hideTheBodyParts(headPlayer2, p2Body)
        #  Speeds up as you eat food
        delay -= 0.005
        # Ensure delay is non-negative
        if delay <= 0:
            delay = 0.1  # Set it to a default positive value
        # Hard mode - Food teleports every {soManySeconds} seconds
        if int(time.time()) % 10 == 0:  # Teleport food every 10 seconds in this example
            food.goto(r.randint(-290, 290), r.randint(-290, 290))
# game loop
wn.listen()
wn.mainloop()