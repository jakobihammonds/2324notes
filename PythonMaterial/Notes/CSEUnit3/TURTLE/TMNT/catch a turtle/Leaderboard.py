# Contains functions fo manage the leaderboard
FILENAME = "CatchATurd.txt"

# Get the name from the user
def getNames(FILENAME):
    # open the db
    file = open(FILENAME, "r")
    # loop through each line of file
    names = []
    for line in file:
        # get the names from each line
        names.append(line.split(",")[0].rstrip())

    file.close()
    # return the names
    return names

# Get scores
def getScores(FILENAME):
    # open the db
    file = open(FILENAME, "r")
    # loop through each line of file
    scores = []
    for line in file:
        # get the scores from each line
        scores.append(line.split(",")[1].rstrip())

    file.close()
    # return the scores
    return scores

# Update leaderboard
def update_leaderboard(FILENAME, leader_names, leader_scores, player_name, player_score):
    player_leaderboard_position = len(leader_scores)
    # check if current score is in the leader_scores range
    for i in range(len(leader_scores)):
        if player_score >= int(leader_scores[i]):
            player_leaderboard_position = i
            break

    # insert the player info
    leader_names.insert(player_leaderboard_position, player_name)
    leader_scores.insert(player_leaderboard_position, player_score)

    # ensure only five players
    while (len(leader_names) > 5):
        leader_names.pop()
        leader_scores.pop()

    # save to the db
    file = open(FILENAME, "w")
    # loop through the lists and save each list to the file
    for i in range(len(leader_names)):
        file.write(f"{leader_names[i]},{leader_scores[i]}\n")
    file.close()

# Draw leaderboard
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
     #high_scorer is a boolean to tell if the current user is a high_scorer
     
     # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
     font_setup = ("Arial", 20, "normal")
     turtle_object.clear()
     turtle_object.teleport(-160,100)
     turtle_object.hideturtle()
     
     index = 0
     # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
     while (index < len(leader_scores)):
          turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
          turtle_object.teleport(-160,int(turtle_object.ycor())-50)
          index = index + 1
     
     # move turtle to a new line
     turtle_object.teleport(-160,int(turtle_object.ycor())-50)
     
     #TODO:  Display message about player making the leaderboard
     
     # move turtle to a new line
     turtle_object.goto(-160,int(turtle_object.ycor())-50)

  # TODO: Display gold/silver/bronze medals
