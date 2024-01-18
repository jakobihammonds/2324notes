#import statements


#global var
artboards='''
    |   |        \t|\t|\t
_____________    -*20
    |   |        \t|\t|\t
_____________    -*20
    |   |        \t|\t|\t
'''

gameBoard=[[" "," "," "],
           [" "," "," "],
           [" "," "," "]]

#functions
def printboard(board):
    for row in range(3):
        print(f"{board[row][0]}|{board[row][1]}|{board[row][2]}")
        if row!=2:
            print("-"*25)
            
def checkForWinner(board):
    #horizontal checking
    for r in range(len(board)):
        #if leftOne == middleOne and middleOne == rightOne and leftOne not " "
        if(board[r][0]==board[r][1==board[r] and board[r][1]==board[r][2] and board[r][0]!=" "]):
           #TODO: You should look at making this more dynamic............
           print("winner winner chicken dinner")
           printBoard(board)
           return True



    #vertical checking

    #diagonally

def checkForCAT(board):
    #CAT or Tie or Scratch
    #if there are no more " " in each row
    for row in board:
        if " " in row:
                return False
    return True
    
def userTurn():
    pass
    
def spotIsTaken(symbol,board,row,col):
    if board[row][col] == " ":
        board[row][col]=symbol
        return False
    return True
    #game loop
print("Welcome to Tic Tac Toe!")

symbol="X"
#keep looping until a winner is found or a tie
while(symbol!="Q"):
    #print the gameboard
    printboard(gameBoard)


    goodSpot=False  #goodSpot will determine if valid input and spot not taken
    while not goodSpot:
        row=int(input("row: "))-1
        col=int(input("col: "))-1
        if row in range(3) and col in range(3):
            #check if spot taken
            if spotIsTaken(symbol,gameBoard,row,col):
                print("Spot Taken")
            else:
                goodSpot=True

    
    #check for a winner or CAT
    if checkForWinner(gameBoard) or checkForCAT(gameBoard):
        symbol="Q"

    #swap turns
    if symbol=="X":
        symbol="O"
        print("O's turn")
    elif symbol=="O":
        symbol="X"
        print("X's turn")