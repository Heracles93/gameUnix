# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:52:47 2018

@author: Heracles93
"""




def displayBoard(board):
    """
    Display the board filled with the marker in place.
    <param board> : list of markers
    """
    print("\n"*100)
    print("\t"+board[7]+"|"+board[8]+"|"+board[9])
    print("\t-----")
    print("\t"+board[4]+"|"+board[5]+"|"+board[6])
    print("\t-----")
    print("\t"+board[1]+"|"+board[2]+"|"+board[3])
    print("\n"*3)

def playerInput():
    """
    Determine the players
    <output (player1, player2)> : the players
    """
    marker=""
    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()
        if marker is "X":
            return("X", "O")
        else:
            return("O", "X")

def placeMarker(board, marker, pos):
    """
    Modify the board with the marker in rigth position
    """
    board[pos] = marker
 
def winCheck(board, marker):
    """
    Check if someone win
    """
    # check lignes
    return((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or 
    (board[7] == board[8] == board[9] == marker) or
    # check cols
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or 
    (board[3] == board[6] == board[9] == marker) or
    # check diags
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker))

def chooseFirst():
    import random
    flip = random.randint(0,1)
    if flip is 0:
        return "Player 1"
    else:
        return "Player 2"   

def spaceCheck(board, pos):
    return board[pos] == " "

def fullBoardCheck(board):
    for i in range(1, len(board)):
        if spaceCheck(board, i):
            return False
    return True

def placeChoice(board):
    pos = 0
    while pos not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board, pos):
        pos = int(input("Choose a position (1-9):\t"))
    return pos

def replay():
    choice = input("Play again ? Yes or No\t")
    return choice.lower() == "yes"

def playgame():
    print("\n"*100)
    print(" Welcome to tic tac toe")

    while True:
        # play the game

        ## set everything up (board, whos first, markers, etc)  
        the_board = [" "]*10
        player1Marker, player2Marker = playerInput()
        turn = chooseFirst()
        print(turn+" will go first")
        playGame = input("Ready to play ? y or n\t").lower()
        if playGame == "y":
            gameOn = True 
        else:
            gameOn = False
        ## game play
        while gameOn:
            if turn == "Player 1":
                ### player 1 turn
                displayBoard(the_board)
                pos = placeChoice(the_board)
                placeMarker(the_board, player1Marker, pos)
                if winCheck(the_board, player1Marker):
                    displayBoard(the_board)
                    print("!! PLAYER 1 HAS WON !!")
                    gameOn = False
                else:
                    if fullBoardCheck(the_board):
                        displayBoard(the_board)
                        print("TIE GAME")
                        gameOn = False
                    else: 
                        turn= "Player 2"
            else:
                ### player 2 turn
                displayBoard(the_board)
                pos = placeChoice(the_board)
                placeMarker(the_board, player2Marker, pos)
                if winCheck(the_board, player2Marker):
                    displayBoard(the_board)
                    print("!! PLAYER 2 HAS WON !!")
                    gameOn = False
                else:
                    if fullBoardCheck(the_board):
                        displayBoard(the_board)
                        print("TIE GAME")
                        gameOn = False
                    else: 
                        turn= "Player 1"

        if not replay():
            break

# playgame()