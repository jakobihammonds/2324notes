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
    options = ["1","2","3","4","5","6","7","8","9"]
    optouts = "\n\n"
    
    print("\nYour options are: \n")
    
    print(options)
    
    # First Move + Its Loop
    move1 = ""
    move1 = input("\nPlayer 1's Turn\n\nWhat is your move?")
    while move1 != '1' or move1 != '2' or move1 != '3' or move1 != '4' or move1 != '5' or move1 != '6' or move1 != '7' or move1 != '8' or move1 != '9':
      if move1 == '1':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move1 == '2':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move1 == '3':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move1 == '4':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move1 == '5':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move1 == '6':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move1 == '7':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move1 == '8':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move1 == '9':
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
    while move2 != '1' or move2 != '2' or move2 != '3' or move2 != '4' or move2 != '5' or move2 != '6' or move2 != '7' or move2 != '8' or move2 != '9':
      if move2 == '1':
        moves[0] = p2
        if move1 == '1':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move2 == '2':
        moves[1] = p2
        if move1 == '2':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move2 == '3':
        moves[2] = p2
        if move1 == '3':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move2 == '4':
        moves[3] = p2
        if move1 == '4':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move2 == '5':
        moves[4] = p2
        if move1 == '5':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move2 == '6':
        moves[5] = p2
        if move1 == '6':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move2 == '7':
        moves[6] = p2
        if move1 == '7':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move2 == '8':
        moves[7] = p2
        if move1 == '8':
          print("Not a choice, make sure you use two capitals.")
          move2 = input("\nPlayer 2's Turn\n\nWhat is your move?")
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move2 == '9':
        moves[8] = p2
        if move1 == '9':
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
    while move3 != '1' or move3 != '2' or move3 != '3' or move3 != '4' or move3 != '5' or move3 != '6' or move3 != '7' or move3 != '8' or move3 != '9':
      if move3 == '1':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move3 == '2':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move3 == '3':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move3 == '4':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move3 == '5':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move3 == '6':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move3 == '7':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move3 == '8':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move3 == '9':
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
    while move4 != '1' or move4 != '2' or move4 != '3' or move4 != '4' or move4 != '5' or move4 != '6' or move4 != '7' or move4 != '8' or move4 != '9':
      if move4 == '1':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move4 == '2':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move4 == '3':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move4 == '4':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move4 == '5':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move4 == '6':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move4 == '7':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move4 == '8':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move4 == '9':
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
    while move5 != '1' or move5 != '2' or move5 != '3' or move5 != '4' or move5 != '5' or move5 != '6' or move5 != '7' or move5 != '8' or move5 != '9':
      if move5 == '1':
        moves[0] = p1 
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move5 == '2':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move5 == '3':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move5 == '4':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move5 == '5':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move5 == '6':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move5 == '7':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move5 == '8':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move5 == '9':
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
    while move6 != '1' or move6 != '2' or move6 != '3' or move6 != '4' or move6 != '5' or move6 != '6' or move6 != '7' or move6 != '8' or move6 != '9':

      if move6 == '1':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move6 == '2':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move6 == '3':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move6 == '4':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move6 == '5':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move6 == '6':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move6 == '7':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move6 == '8':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move6 == '9':
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
    
    while move7 != '1' or move7 != '2' or move7 != '3' or move7 != '4' or move7 != '5' or move7 != '6' or move7 != '7' or move7 != '8' or move7 != '9':
  
      if move7 == '1':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move7 == '2':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move7 == '3':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move7 == '4':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move7 == '5':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move7 == '6':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move7 == '7':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move7 == '8':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move7 == '9':
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
    
    while move8 != '1' or move8 != '2' or move8 != '3' or move8 != '4' or move8 != '5' or move8 != '6' or move8 != '7' or move8 != '8' or move8 != '9':

      if move8 == '1':
        moves[0] = p2
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = ""
          break
      elif move8 == '2':
        moves[1] = p2
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = ""
          break
      elif move8 == '3':
        moves[2] = p2
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = ""
          break
      elif move8 == '4':
        moves[3] = p2
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = ""
          break
      elif move8 == '5':
        moves[4] = p2
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = ""
          break
      elif move8 == '6':
        moves[5] = p2
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = ""
          break
      elif move8 == '7':
        moves[6] = p2
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = ""
          break
      elif move8 == '8':
        moves[7] = p2
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = ""
          break
      elif move8 == '9':
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
    while move9 != '1' or move9 != '2' or move9 != '3' or move9 != '4' or move9 != '5' or move9 != '6' or move9 != '7' or move9 != '8' or move9 != '9':
      if move9 == '1':
        moves[0] = p1
        if moves[0] == 'X' or moves[0] == 'x' or moves[0] == 'O' or moves[0] == 'o':
          options[0] = " "
          break
      elif move9 == '2':
        moves[1] = p1
        if moves[1] == 'X' or moves[1] == 'x' or moves[1] == 'O' or moves[1] == 'o':
          options[1] = " "
          break
      elif move9 == '3':  
        moves[2] = p1
        if moves[2] == 'X' or moves[2] == 'x' or moves[2] == 'O' or moves[2] == 'o':
          options[2] = " "
          break
      elif move9 == '4':
        moves[3] = p1
        if moves[3] == 'X' or moves[3] == 'x' or moves[3] == 'O' or moves[3] == 'o':
          options[3] = " "
          break
      elif move9 == '5':
        moves[4] = p1
        if moves[4] == 'X' or moves[4] == 'x' or moves[4] == 'O' or moves[4] == 'o':
          options[4] = " "
          break
      elif move9 == '6':
        moves[5] = p1
        if moves[5] == 'X' or moves[5] == 'x' or moves[5] == 'O' or moves[5] == 'o':
          options[5] = " "
          break
      elif move9 == '7':
        moves[6] = p1
        if moves[6] == 'X' or moves[6] == 'x' or moves[6] == 'O' or moves[6] == 'o':
          options[6] = " "
          break
      elif move9 == '8':
        moves[7] = p1
        if moves[7] == 'X' or moves[7] == 'x' or moves[7] == 'O' or moves[7] == 'o':
          options[7] = " "
          break
      elif move9 == '9':
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