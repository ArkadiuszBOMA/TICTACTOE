import os
import time
from screen_deposit import screen_title, game_help, game_signes, game_titele
'''
This module is used for:
def display_board   print the board
def status_empty    check availlable moves 
def status          check winning status
'''

def display_board(board):
    print(f'\t   1   2   3  ')
    print(f'\tA  {board[0]} | {board[1]} | {board[2]} ')
    print(f'\t  ---+---+---')
    print(f'\tB  {board[3]} | {board[4]} | {board[5]} ')
    print(f'\t  ---+---+---')
    print(f'\tC  {board[6]} | {board[7]} | {board[8]} ')
    print(f'\t  ---+---+---')
    print("-" * 126)

def status(board, player, game_statistic_table):
    if (board[0] == player[0] and board[1] == player[0] and board[2] == player[0]) or\
        (board[3] == player[0] and board[4] == player[0] and board[5] == player[0]) or\
        (board[6] == player[0] and board[7] == player[0] and board[8] == player[0]) or\
        (board[0] == player[0] and board[3] == player[0] and board[6] == player[0]) or\
        (board[1] == player[0] and board[4] == player[0] and board[7] == player[0]) or\
        (board[2] == player[0] and board[5] == player[0] and board[8] == player[0]) or\
        (board[0] == player[0] and board[4] == player[0] and board[8] == player[0]) or\
        (board[2] == player[0] and board[4] == player[0] and board[6] == player[0]):
        if player[2] == "Human":
            game_statistic_table[3] += 1
        else:
            game_statistic_table[4] += 1
        if player[0] == "X":
            game_statistic_table[1] += 1
        else:
            game_statistic_table[2] += 1
        screen_title()
        print(f'\t!! CONGRATULATION !! \n\t{player[1]} {player[2]} using signe\n{player[3]}\n\t      wins')
        display_board(board)
        print('\t!   Thanks for the game   !' )
        print("-" * 126)
        input('\t! Press ENTER to continue !')
        game_status = False                    
        return game_status, game_statistic_table
    else:
        game_status = True
        return game_status

def status_empty(board_status, board_availlable):
    board_availlable = []
    for i in range(len(board_status)):
        if board_status[i] != "X" and board_status[i] != "O":
            board_availlable.append(i)
    return board_availlable