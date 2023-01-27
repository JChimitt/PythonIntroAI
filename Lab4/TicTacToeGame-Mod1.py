"""
Game:  Tic-Tac-Toe using MiniMax
Adopted from:  https://github.com/javacodingcommunity/TicTacToeAI-with-Minimax
"""

import sys

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

board4 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 
            5: ' ', 6: ' ', 7: ' ', 8: ' ', 
            9: ' ', 10: ' ', 11: ' ', 12: ' ',
            13: ' ', 14: ' ', 15: ' ', 16: ' ',}

board5x5 = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 
            6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 
            11: ' ', 12: ' ',13: ' ', 14: ' ', 15: ' ', 
            16: ' ', 17: ' ',18: ' ', 19: ' ', 20: ' ',
            21: ' ', 22: ' ',23: ' ', 24: ' ', 25: ' ',}




    
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')    
    print(board[7] + '|' + board[8] + '|' + board[9])
     
    print("\n")
    
def printBoard4(board4):
    print(board4[1] + '|' + board4[2] + '|' + board4[3] + '|' + board4[4])
    print('-+-+-+-')
    print(board4[5] + '|' + board4[6] + '|' + board4[7] + '|' + board4[8])
    print('-+-+-+-')    
    print(board4[9] + '|' + board4[10] + '|' + board4[11] + '|' + board4[12])
    print('-+-+-+-')  
    print(board4[13] + '|' + board4[14] + '|' + board4[15] + '|' + board4[16])
    print("\n")
    
def printBoard5x5(board5):
    print(board[1] + '|' + board[2] + '|' + board[3] + '/' + board[4] + '/' + board[5])
    print('-+-+-+-+-')  
    print(board[6] + '|' + board[7] + '|' + board[8] + '/' + board[9] + '/' + board[10])
    print('-+-+-+-+-')      
    print(board[11] + '|' + board[12] + '|' + board[13] + '/' + board[14] + '/' + board[15])
    print('-+-+-+-+-')  
    print(board[16] + '|' + board[17] + '|' + board[18] + '/' + board[19] + '/' + board[20])
    print('-+-+-+-+-')  
    print(board[21] + '|' + board[22] + '|' + board[23] + '/' + board[24] + '/' + board[25])
    print("\n")
    

# chck if board position is free - a space
def spaceIsFree(position):
    if(board[position] == ' '):
        return True
    else:
        return False
def spaceIsFree4(position):
    if(board4[position] == ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False    # if there are empty spaces then still can play
    return True             # it is a draw
def checkDraw4():
    for key in board4.keys():
        if board4[key] == ' ':
            return False    # if there are empty spaces then still can play
    return True  
        
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7]== board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def checkForWin4x4():
    if (board4[1] == board4[2] and board4[1] == board4[3] and board4[1] == board4[4] and board4[1] != ' '):
        return True
    elif (board4[5] == board4[6] and board4[5] == board4[7] and board4[5] == board4[8] and board4[5] != ' '):
        return True
    elif (board4[9] == board4[10] and board4[9] == board4[11] and board4[9] == board4[12] and board4[9] != ' '):
        return True
    elif (board4[13] == board4[14] and board4[13] == board4[15] and board4[13] == board4[16] and board4[13] != ' '):
        return True
    elif (board4[1] == board4[5] and board4[1] == board4[9] and board[1] == board4[13] and board4[1] != ' '):
        return True
    elif (board4[2] == board4[6] and board4[2] == board4[10] and board4[2] == board4[14] and board4[2] != ' '):
        return True
    elif (board4[3] == board4[7] and board4[3] == board4[11] and board4[3] == board4[15] and board4[3] != ' '):
        return True
    elif (board4[4] == board4[8] and board4[4] == board4[12] and board4[4] == board4[16] and board4[4] != ' '):
        return True
    elif (board4[1] == board4[6] and board4[1] == board4[11] and board4[1] == board4[16] and board4[1] != ' '):
        return True
    elif (board4[4] == board4[7] and board4[4] == board4[10] and board4[4] == board4[13] and board4[4] != ' '):
        return True
    else:
        return False
    
def checkWhichMarkWon4x4(mark):
    if (board4[1] == board4[2] and board4[1] == board4[3] and board4[1] == board4[4] and board4[1] == mark):
        return True
    elif (board4[5] == board4[6] and board4[5] == board4[7] and board4[5] == board4[8] and board4[5] == mark):
        return True
    elif (board4[9] == board4[10] and board4[9] == board4[11] and board4[9] == board4[12] and board4[9] == mark):
        return True
    elif (board4[13] == board4[14] and board4[13] == board4[15] and board4[13] == board4[16] and board4[13] == mark):
        return True
    elif (board4[1] == board4[5] and board4[1] == board4[9] and board[1] == board4[13] and board4[1] == mark):
        return True
    elif (board4[2] == board4[6] and board4[2] == board4[10] and board4[2] == board4[14] and board4[2] == mark):
        return True
    elif (board4[3] == board4[7] and board4[3] == board4[11] and board4[3] == board4[15] and board4[3] == mark):
        return True
    elif (board4[4] == board4[8] and board4[4] == board4[12] and board4[4] == board4[16] and board4[4] == mark):
        return True
    elif (board4[1] == board4[6] and board4[1] == board4[11] and board4[1] == board4[16] and board4[1] == mark):
        return True
    elif (board4[4] == board4[7] and board4[4] == board4[10] and board4[4] == board4[13] and board4[4] == mark):
        return True
    else:
        return False
    

# check which player won
def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7]== board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
    
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        
        if(checkDraw()):
            print("Draw!")
            sys.exit()
            
        if checkForWin():
            if letter == 'X':
                print("X wins!")
                sys.exit()
            else:
                print("O wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return
def insertLetter4(letter, position):
    if spaceIsFree4(position):
        board4[position] = letter
        printBoard4(board4)
        
        if(checkDraw4()):
            print("Draw!")
            sys.exit()
            
        if checkForWin4x4():
            if letter == 'X':
                print("X wins!")
                sys.exit()
            else:
                print("O wins!")
                sys.exit()
        return
    
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter4(letter, position)
        return
player1 = 'O'
player2 = 'X'
bot = 'X'
bot2 = 'O'

# Function to prompt player to enter uppercase letter into board position
# Player will use O in this game
def player1Move():
    position = int(input("Player 1, enter the position for 'O': "))
    insertLetter(player1, position)
    return
def player2Move():
    position = int(input("Player 2, enter the position for 'X': "))
    insertLetter(player2, position)
    return
def player2Move4():
    position = int(input("Player 2, enter the position for 'X': "))
    insertLetter4(player2, position)
    return

# Function to prompt computer to enter uppercase letter into board position
# Computer will  use X in this game
# Will check with minmax algorithm if it is best move.
def compMove():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0      # initialize
    
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)    
    return  
def compMove2():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0      # initialize
    
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot2
            score = minimax(board, 0, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot2, bestMove)    
    return 
def compMove24():
#    position = int(input("Enter the postion for 'O': "))
#    insertLetter(bot, position)
    bestScore = -1 # initialize with any number
    bestMove = 0      # initialize
    
    for key in board.keys():
        if (board4[key] == ' '):
            board4[key] = bot2
            score = minimax(board, 0, False)
            board4[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter4(bot2, bestMove)    
    return 

# Define the minmax function
# computer plays against itself playing the game out
def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):    # check if bot won
        return 1
    elif checkWhichMarkWon(player1):  # check if player won
        return -1
    if checkWhichMarkWon4x4(bot):    # check if bot won
        return 1
    elif checkWhichMarkWon4x4(player1):  # check if player won
        return -1
    elif checkDraw():
        return 0
    
    # if maximizing (playing as computer) take score with highest move value
    if isMaximizing:   
        bestScore1 = -1
        bestScore2 = -1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if(score > bestScore1):
                    bestScore1 = score
        return bestScore1
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot2
                score = minimax(board, 0, False)
                board[key] = ' '
                if(score > bestScore2):
                    bestScore2 = score
        return bestScore2
    else:                       # if you are not maximizing, best score is low score
        bestScore1 = 1
        bestScore2 = 1
        
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player1
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore1):
                    bestScore1 = score
        return bestScore1
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore2):
                    bestScore2 = score
        return bestScore2
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot2
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore1):
                    bestScore1 = score
        return bestScore1
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player2
                score = minimax(board, 0, True)
                board[key] = ' '
                if(score < bestScore1):
                    bestScore1 = score
        return bestScore1
    

menuDecision = input("Enter the number next to one of the following options. \n1 Two Human Players \n2 Two Computer Players \n3 Human vs Computer \n4 Human vs Computer on a 5x5 grid\n\n")
if menuDecision == '1':
    print("\n-------------------\nHuman vs Human")
    printBoard(board)
    while not checkForWin():
       player1Move()
       player2Move()
       
elif menuDecision == '2':
    print("\n-------------------\nComputer vs Computer")    
    counter = 0
    while not checkForWin():
       nextMove = input("\nMake next move (Y/N)? ")
       
       if nextMove == 'Y':
               if(counter % 2 == 0):
                   compMove()
                   counter += 1
                   
               else:
                   compMove2()
                   counter += 1
       else:
           quit()
       
            
elif menuDecision == '3':
    print("\n-------------------\nHuman vs Computer")   
    while not checkForWin():
        compMove()
        player1Move()
        
elif menuDecision == '4':
    print("\n-------------------\nHuman vs Computer 4x4")   
    while not checkForWin4x4():
        player2Move4()
        compMove24()
        
        
                   

    
    
# printBoard(board) 
# print(spaceIsFree(1))
# insertLetter('x',1)

