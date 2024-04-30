with open("highscores.csv","r") as file:
    f=file.readlines()
    theFile=[]
    for eachLine in f:
        theFile.append(eachLine.rstrip().split(","))


names = []
scores = []

for eachLine in theFile:
    try:
        scores.append(int(eachLine[1]))
        names.append(eachLine[0])
    except:
        print("bad data", eachLine)

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