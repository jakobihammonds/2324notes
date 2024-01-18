'''
you got this bruh
'''
Win = 0
Ret = "\n"
def TTT():
  
  test = False
  while test != True:
    global Win
    
    import os
    import sys
    import random
    
    Re = ""

    B = Re
    #Definers
    Win = 0
    
    #
    
    nullist = ["","","","","","","","",""]
    
    moves = [" ", " "," "," "," "," "," "," "," "]
    def tictactoe(moves):
      print("\n")
      print("\t     |     |")
      print("\t  {}  |  {}  |  {}".format(moves[0], moves[1], moves[2]))
      print('\t_____|_____|_____')
      print("\t     |     |")
      print("\t  {}  |  {}  |  {}".format(moves[3], moves[4], moves[5]))
      print('\t_____|_____|_____')
      print("\t     |     |")
      print("\t  {}  |  {}  |  {}".format(moves[6], moves[7], moves[8]))
      print("\t     |     |")
      print("\n                ")
    

    # odd numbers are x's, evens are o's
    
    #Player Registration
    p1 = input("Hi Player 1, do you want X or O")
    p2 = "null"
    while p2 != 'O' or p2 != 'X':
      if p1 == 'X' or p1 == 'x' :
        p2 = 'O'
        break
      elif p1 == 'O' or p1 == 'o':
        p2 = 'X'
        break
      else:
        print("Not an option")
        p1 = input("Hi Player 1, do you want X or O")
    
    if p1 == 'x':
      p1 = 'X'
    if p1 == 'o':
      p1 = 'O'
      
    
    print("Player 1 is " + p1)
    print("Player 2 is " + p2)
    

      
    #Wincheck
  
 
    test = False
 

   
  
    def Wincheck1():
      global Win
      global test
      test = False
      while test == False:
        if moves[0] and moves[1] and moves[2] == p1:
          Win = 1
          test == True
          return
        elif moves[3] and moves[4] and moves[5] == p1:
          Win = 1
          test == True
          return
        elif moves[6] and moves[7] and moves[8] == p1:
          Win = 1
          test == True
          return
        elif moves[0] and moves[3] and moves[6] == p1:
          Win = 1
          test == True
          return
        elif moves[1] and moves[4] and moves[7] == p1:
          Win = 1
          test == True
          return
        elif moves[2] and moves[5] and moves[8] == p1:
          Win = 1
          test == True
          return
        elif moves[2] and moves[4] and moves[6] == p1:
          Win = 1
          test == True
          return
        elif moves[0] and moves[4] and moves[8] == p1:
          Win = 1
          test == True
          return
        elif moves[0] and moves[1] and moves[2] == p2:
          Win = 2
          test == True
          return
        elif moves[3] and moves[4] and moves[5] == p2:
          Win = 2
          test == True
          return
        elif moves[6] and moves[7] and moves[8] == p2:
          Win = 2
          test == True
          return
        elif moves[0] and moves[3] and moves[6] == p2:
          Win = 2
          test == True
          return
        elif moves[1] and moves[4] and moves[7] == p2:
          Win = 2
          test == True
          return
        elif moves[2] and moves[5] and moves[8] == p2:
          Win = 2
          test == True
          return
        elif moves[2] and moves[4] and moves[6] == p2:
          Win = 2
          test == True
          return
        elif moves[0] and moves[4] and moves[8] == p2:
          Win = 2
          test == True
          return
        else:
          return
    
    
    #Game Moves # odd numbers are player 1's, evens are player 2's
    
    optins = "\n\n"
    options = ["TopLeft","TopMid","TopRight","MidLeft","MidMid","MidRight","BottomLeft","BottomMid","BottomRight"]
    optouts = "\n\n"
    
    print("\nYour options are: \n")
    
    print(options)
    
    # First Move + Its Loop
    move1 = ""
    move1 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    while move1 != 'TopLeft' or move1 != 'TopMid' or move1 != 'TopRight' or move1 != 'MidLeft' or move1 != 'MidMid' or move1 != 'MidRight' or move1 != 'BottomLeft' or move1 != 'BottomMid' or move1 != 'BottomRight':
      if move1 == 'TopLeft':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move1 == 'TopMid':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move1 == 'TopRight':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move1 == 'MidLeft':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move1 == 'MidMid':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move1 == 'MidRight':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move1 == 'BottomLeft':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move1 == 'BottomMid':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move1 == 'BottomRight':
        moves[8] = p1
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = " "
          break
      else:
        print("Not a choice, make sure you use two capitals.")
        move1 = input("\nPlayer 1's Turn\n\nWhat is your move?")
      
    os.system('cls')
    print(tictactoe(moves))
      #Move 2
    print("\nYour options are: \n")
    
    
    print(str(options))
    
    # Second Move + Its Loop
    move2 = ""
    move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    while move2 != 'TopLeft' or move2 != 'TopMid' or move2 != 'TopRight' or move2 != 'MidLeft' or move2 != 'MidMid' or move2 != 'MidRight' or move2 != 'BottomLeft' or move2 != 'BottomMid' or move2 != 'BottomRight':
      if move2 == 'TopLeft':
        moves[0] = p2
        if move1 == 'TopLeft':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move2 == 'TopMid':
        moves[1] = p2
        if move1 == 'TopMid':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move2 == 'TopRight':
        moves[2] = p2
        if move1 == 'TopRight':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move2 == 'MidLeft':
        moves[3] = p2
        if move1 == 'MidLeft':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move2 == 'MidMid':
        moves[4] = p2
        if move1 == 'MidMid':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move2 == 'MidRight':
        moves[5] = p2
        if move1 == 'MidRight':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move2 == 'BottomLeft':
        moves[6] = p2
        if move1 == 'BottomLeft':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move2 == 'BottomMid':
        moves[7] = p2
        if move1 == 'BottomMid':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move2 == 'BottomRight':
        moves[8] = p2
        if move1 == 'BottomRight':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = ""
          break
      
      else:
        print("Not a choice, make sure you use two capitals.")
        move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    
    os.system('cls')
    print(tictactoe(moves))
    
    #Move 3 ( P1 )
    
    print(options)
    
    move3 = ""
    move3 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    while move3 != 'TopLeft' or move3 != 'TopMid' or move3 != 'TopRight' or move3 != 'MidLeft' or move3 != 'MidMid' or move3 != 'MidRight' or move3 != 'BottomLeft' or move3 != 'BottomMid' or move3 != 'BottomRight':
      if move3 == 'TopLeft':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move3 == 'TopMid':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move3 == 'TopRight':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move3 == 'MidLeft':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move3 == 'MidMid':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move3 == 'MidRight':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move3 == 'BottomLeft':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move3 == 'BottomMid':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move3 == 'BottomRight':
        moves[8] = p1
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = " "
          break
      else:
        print("Not a choice, make sure you use two capitals.")
        move3 = input("\nPlayer 1's Turn\n\nWhat is your move?")
      
    os.system('cls')    

    print(tictactoe(moves))
    
    #
    
    
    # 4th Move
    
    print(options)
    move4 = ""
    move4 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    while move4 != 'TopLeft' or move4 != 'TopMid' or move4 != 'TopRight' or move4 != 'MidLeft' or move4 != 'MidMid' or move4 != 'MidRight' or move4 != 'BottomLeft' or move4 != 'BottomMid' or move4 != 'BottomRight':
      if move4 == 'TopLeft':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move4 == 'TopMid':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move4 == 'TopRight':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move4 == 'MidLeft':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move4 == 'MidMid':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move4 == 'MidRight':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move4 == 'BottomLeft':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move4 == 'BottomMid':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move4 == 'BottomRight':
        moves[8] = p2
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = ""
          break
           
      else:
        print("Not a choice, make sure you use two capitals.")
        move4 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    
    os.system('cls')    

    print(tictactoe(moves))
    
    #5th Move
    
    print(options)
    
    move5 = ""
    if Win != 0:
      break
    move5 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    while move5 != 'TopLeft' or move5 != 'TopMid' or move5 != 'TopRight' or move5 != 'MidLeft' or move5 != 'MidMid' or move5 != 'MidRight' or move5 != 'BottomLeft' or move5 != 'BottomMid' or move5 != 'BottomRight':
      if move5 == 'TopLeft':
        moves[0] = p1 
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move5 == 'TopMid':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move5 == 'TopRight':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move5 == 'MidLeft':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move5 == 'MidMid':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move5 == 'MidRight':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move5 == 'BottomLeft':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move5 == 'BottomMid':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move5 == 'BottomRight':
        moves[8] = p1
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = " "
          break
      else:
        print("Not a choice, make sure you use two capitals.")
        move5 = input("\nPlayer 1's Turn\n\nWhat is your move?")
      
    os.system('cls')    

    print(tictactoe(moves))
    
    #First wincheck
    Wincheck1()


    
    
    
    #6th Move
    print("\n" + str(options))
    move6 = ""
    if Win != 0:
      break
    move6 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    while move6 != 'TopLeft' or move6 != 'TopMid' or move6 != 'TopRight' or move6 != 'MidLeft' or move6 != 'MidMid' or move6 != 'MidRight' or move6 != 'BottomLeft' or move6 != 'BottomMid' or move6 != 'BottomRight':

      if move6 == 'TopLeft':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move6 == 'TopMid':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move6 == 'TopRight':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move6 == 'MidLeft':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move6 == 'MidMid':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move6 == 'MidRight':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move6 == 'BottomLeft':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move6 == 'BottomMid':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move6 == 'BottomRight':
        moves[8] = p2
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = ""
          break
      elif test == True:
        break     
      else:
        print("Not a choice, make sure you use two capitals.")
        move6 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    
    os.system('cls')
    print(tictactoe(moves))
    
    # 2nd Winchecks
    Wincheck1()
    
    #
    # Move 7
    
    print(options)
    
    move7 = ""
    if Win != 0:
      break
    move7 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    
    while move7 != 'TopLeft' or move7 != 'TopMid' or move7 != 'TopRight' or move7 != 'MidLeft' or move7 != 'MidMid' or move7 != 'MidRight' or move7 != 'BottomLeft' or move7 != 'BottomMid' or move7 != 'BottomRight':
  
      if move7 == 'TopLeft':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move7 == 'TopMid':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move7 == 'TopRight':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move7 == 'MidLeft':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move7 == 'MidMid':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move7 == 'MidRight':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move7 == 'BottomLeft':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move7 == 'BottomMid':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move7 == 'BottomRight':
        moves[8] = p1
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = " "
          break
      elif test == True:
        break
      else:
        print("Not a choice, make sure you use two capitals.")
        move7 = input("\nPlayer 1's Turn\n\nWhat is your move?")
      
    os.system('cls')
    print(tictactoe(moves))
    
    # 3rd Winchecks
    Wincheck1()
  
    
    #8th move 
    print(options)
    move8 = ""
    if Win != 0:
      break
    move8 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    
    while move8 != 'TopLeft' or move8 != 'TopMid' or move8 != 'TopRight' or move8 != 'MidLeft' or move8 != 'MidMid' or move8 != 'MidRight' or move8 != 'BottomLeft' or move8 != 'BottomMid' or move8 != 'BottomRight':

      if move8 == 'TopLeft':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move8 == 'TopMid':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move8 == 'TopRight':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move8 == 'MidLeft':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move8 == 'MidMid':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move8 == 'MidRight':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move8 == 'BottomLeft':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move8 == 'BottomMid':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move8 == 'BottomRight':
        moves[8] = p2
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = ""
          break
      else:
        print("Not a choice, make sure you use two capitals.")
        move8 = input("\nPlayer 2's Turn\n\nWhat is your move?")
    
    
    
    os.system('cls')
    
    print(tictactoe(moves))
    
    # 4th Winchecks
    Wincheck1()
    
#
    # Move 9 ( LAST ONE )
    print(options)
    
    move9 = ""
    if Win != 0:
      break
    move9 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    while move9 != 'TopLeft' or move9 != 'TopMid' or move9 != 'TopRight' or move9 != 'MidLeft' or move9 != 'MidMid' or move9 != 'MidRight' or move9 != 'BottomLeft' or move9 != 'BottomMid' or move9 != 'BottomRight':
      if move9 == 'TopLeft':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move9 == 'TopMid':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move9 == 'TopRight':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move9 == 'MidLeft':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move9 == 'MidMid':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move9 == 'MidRight':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move9 == 'BottomLeft':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move9 == 'BottomMid':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move9 == 'BottomRight':
        moves[8] = p1
        if moves[8] == 'X' or moves[8] == 'x' or moves[8] == 'O' or moves[8] == 'o':
          options[8] = " "
          break

      else:
        print("Not a choice, make sure you use two capitals.")
        move9 = input("\nPlayer 1's Turn\n\nWhat is your move?")
      
    os.system('cls')
    print(tictactoe(moves))
    
   #
    
    Wincheck1()
  
    # last winchecks
    os.system('cls')
    break
TTT()
if Win == 1:
  print("Player 1 Wins")
  print("Rerun to play again.")
if Win == 2:
  print("Player 2 Wins")
  print("Rerun to play again.")
if Win == 0:
    print("Its a draw!") 
    print("Rerun to play again.")