# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:26:11 2019

@author: Kunal-work
"""

import random 

def display_board(board):
    print('\n'*100)
    # clear_output()
    print(board[7]+' '+'|'+ ' '+board[8]+' '+'|'+ ' ' +board[9]) 
    print(board[4]+' '+'|'+ ' ' +board[5]+' '+'|'+ ' ' +board[6])
    print(board[1]+' '+'|'+ ' ' +board[2]+' '+'|'+ ' ' +board[3])

def player_input():
    marker = ''
    
    #KEEP ASKING PLAYER 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        
    #ASSIGN PLAYER 2, the opposite marker
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, marker):
    #checking all rows, columns and diagnols
    if (board[7] == board[8] == board[9] == marker) or (board[4] == board[5] == board[6] == marker) or (board[1] == board[2] == board[3] == marker):
        return True
    elif (board[7] == board[4] == board[1] == marker) or (board[8] == board[5] == board[2] == marker) or (board[9] == board[6] == board[3] == marker):
        return True
    elif (board[7] == board[5] == board[3] == marker) or (board[9] == board[5] == board[1] == marker):
        return True
    
    return False

def choose_first():
    
    flip = random.randint(0,1) #will return a random number from 0 or 1
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1, 10):   #starting from 1 and upto but not including 10
        if space_check(board, i):
            return False
        
    return True

def player_choice(board):
    
    position = 0
    
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    
    
    return position

def replay():
    
    choice = input("Play again? Enter Y or N ")
    
    return choice == 'Y'

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')

while True:
    
    the_board = [' ']*10
    player1, player2 = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Enter Y or N ')
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        
    ##GAMEPLAY
    while game_on:
        
        if turn == 'Player 1':
            
            #SHOW THE BOARD
            display_board(the_board)
            
            # CHOOSE A POSITION
            position = player_choice(the_board)
            
            # PLACE THE MARKER ON THE POSITION
            place_marker(the_board, player1, position)
            
            # CHECK IF THEY WON
            if win_check(the_board, player1):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 2'    # NO TIE AND NO WIN? THEN NEXT PLAYER'S TURN
        else:
            
            #SHOW THE BOARD
            display_board(the_board)
            
            # CHOOSE A POSITION
            position = player_choice(the_board)
            
            # PLACE THE MARKER ON THE POSITION
            place_marker(the_board, player2, position)
            
            # CHECK IF THEY WON
            if win_check(the_board, player2):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'    # NO TIE AND NO WIN? THEN NEXT PLAYER'S TURN
            

    if not replay():
        break

