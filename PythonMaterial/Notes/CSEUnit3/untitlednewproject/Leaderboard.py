FILENAME="db.txt"
names=[]
scores=[]
#names
def getName(FILENAME):
     file1=open(FILENAME,"r")
     global names
     names=[]
     for eachLine in file1:
          index=0
          name=""
          while(eachLine[index]!=","):
               eachLetter = eachLine[index]
               name+= eachLetter
               index+=1
          names.append(name)
     return names
#scores
def getScore(FILENAME):
     file1=open(FILENAME,"r")
     global scores
     scores=[]
     for eachLine in file1:
          data=eachLine.split(",")
          number=data[1].rstrip()
          scores.append(number)
     return scores



#draw leaderboard
def draw_leaderboard( leader_names, leader_scores):
     
     index = 0
     while (index < len(leader_scores)):
          print(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]))
          index = index + 1
getName(FILENAME)
getScore(FILENAME)
#AV SCORE
total=sum(scores)
amount=len(scores)
average= total/amount

high=max(scores)
low=min(scores)

highscorer=names[scores.index(high)]
lowscorer=names[scores.index(low)]

print(high,highscorer)
print(low,lowscorer)
print(average)