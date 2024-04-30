import Leaderboard as lb

def manageLeaderboard():
  global score
  namesList = lb.getNames("db.txt")
  scoresList = lb.getScores("db.txt")
  lb.drawLeaderboard(False, namesList, scoresList)
  
manageLeaderboard()
