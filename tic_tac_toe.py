from players import select_palyers
from human_entry_check import move_human
from computer_moves import move_easy, move_medium
from board import display_board, status, status_empty
from game_stat import game_statis, get_game_statistic_stat
from screen_deposit import screen_title, game_help, game_signes
import sys
import time
import os

SIGN_SCREEN_START = '\033[3;32;40m'
SIGN_SCREEN_END = '\033[0;37;40m'

game_statistic_table = [0,0,0,0,0,0]

def get_game_statistic():
    global game_statistic_table
    with open("game_statistic.txt", "r", encoding='utf8') as gs_file:
        lines = gs_file.readlines()
        gs_file.seek(0)
        for number, line in enumerate(lines):
            game_statistic_table[number] = int(line.strip('\n'))


game_command = ['play', 'quit', 'help','stat']

board_status = ['.','.','.','.','.','.','.','.','.']
board_winning = ['.','.','.','.','.','.','.','.','.']
board_moves = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
indicator_rows =['A','B','C']
indicator_colums =['1','2','3']
board_availlable = []

players_availlable = {'1':['Human', 'Computer'],'2':['Computer', 'Human'], '3':['Human', 'Human'], '4':['Computer', 'Computer']}
players_availlable_difficulty = {'1':'EASY','2': 'HARD'}
player_1 =['X','','', game_signes[0]]
player_2 =['O','','', game_signes[1]]

player_current = []

game_status = True


def game_start():
    get_game_statistic()
    os.system("cls")
    try:
        if len(sys.argv) <= 1:
            game_initiation()
        else:
            if sys.argv[1] == game_command[0]:                                 # agrv - to ważna komenda - anmienia linie poleceń na listę, którą można ITEROWAĆ
                screen_title()
                the_game(board_status, board_winning, players_availlable,  player_1,  player_2, players_availlable_difficulty, game_status, board_availlable)
                game_initiation()
            elif sys.argv[1] == game_command[2]:
                screen_title()
                print(game_help)
                print("-" * 126)
            elif sys.argv[1] == game_command[3]:
                screen_title()
                get_game_statistic_stat()
                print("-" * 126)
            else:
                os.system("cls")
                game_initiation()
    except ValueError:
            os.system("cls")
            game_initiation()


def game_initiation():
    global board_status
    global player_1
    global player_2
    global game_status
    global game_statistic_table
    game_status_begining = True
    while game_status_begining == True:
        board_status = ['.','.','.','.','.','.','.','.','.']
        player_1 =['X','','', game_signes[0]]
        player_2 =['O','','', game_signes[1]]
        screen_title()
        command_choice_input = input('Choose from following options\n\tplay - to start the game\n\tquit - to exit application\n\thelp - to display game instruction\n -> ')
        command_choice = command_choice_input.lower()
        if command_choice in game_command:
            if command_choice == game_command[0]:
                game_statistic_table[0] += 1
                screen_title()
                the_game(board_status, board_winning, players_availlable,  player_1,  player_2, players_availlable_difficulty, game_status, board_availlable)
                game_status_begining = True
            elif command_choice == game_command[1]:
                screen_title()
                print("\n! See you next time !")
                print("-" * 126)
                game_writ_stat = [str(game_statistic_table[0]),str(game_statistic_table[1]), str(game_statistic_table[2]), str(game_statistic_table[3]), str(game_statistic_table[4]), str(game_statistic_table[5])]
                game_statis(game_writ_stat)
                print(f"The application was used {game_statistic_table[0]} times already\n\t{game_statistic_table[1]} times win 'X'\n\t{game_statistic_table[2]} times win 'O'\n\t{game_statistic_table[3]} times win Human\n\t{game_statistic_table[4]} times win Computer\n\t{game_statistic_table[5]} was Draw")
                print("-" * 126)
                game_status_begining = False
            elif command_choice == game_command[2]:
                screen_title()
                print(game_help)
                print("-" * 126)
                if input('\t! Press ENTER to continue !'):
                    game_status_begining == True
            else:
                screen_title()
                print("\n! it is wrong choice !")
                print("-" * 126)
                if input('\t! Press ENTER to continue !'):
                    game_status_begining == True
        else:
            screen_title()
            print("\n! it is wrong choice !")
            print("-" * 126)
            if input('\t! Press ENTER to continue !'):
                game_status_begining == True


def signe_change(player_current):
    if player_current == player_1:
        player_current = player_2
        return player_current
    else:
        player_current = player_1
        return player_current


def the_game(board_status, board_winning, players_availlable,  player_1,  player_2, players_availlable_difficulty, game_status, board_availlable):
    select_palyers(players_availlable,  player_1,  player_2, players_availlable_difficulty, game_statistic_table)
    player_current = player_1
    time.sleep(1)
    screen_title()
    print(f'THE BATTEL\n\t{player_1[1]} {player_1[2]} with sign\t\t{player_1[3]}\nagainst\n\t{player_2[1]} {player_2[2]} with sign\t\t{player_2[3]}')
    print("-" * 126)
    time.sleep(1)
    
    while game_status == True:
        board_availlable = status_empty(board_status, board_availlable)
        if len(board_availlable) == 0:
            game_statistic_table[5] += 1
            screen_title()
            display_board(board_status)
            print('\t!!        D R A W        !!')
            print('\t!   Thanks for the game   !' )
            print("-" * 126)
            input('\t! Press ENTER to continue !')
            game_status = False
        else:
            if player_current[2] == 'Human':
                time.sleep(1)
                screen_title()
                print(f'\n! Now {player_current[1]} {player_current[2]} sign')
                print(SIGN_SCREEN_START+player_current[3]+SIGN_SCREEN_END)
                display_board(board_status)
                move_human(indicator_rows, indicator_colums, board_moves, board_status, player_current, game_statistic_table)
                game_status = status(board_status, player_current, game_statistic_table)
                player_current = signe_change(player_current)
            else:
                if player_current[1] == 'EASY':
                    time.sleep(1)
                    screen_title()
                    print(f'\n! Now {player_current[1]} {player_current[2]} sign')
                    print(SIGN_SCREEN_START+player_current[3]+SIGN_SCREEN_END)
                    move_easy(board_availlable,board_status, player_current)
                    display_board(board_status)
                    game_status = status(board_status, player_current, game_statistic_table)
                    player_current = signe_change(player_current)
                else:
                    time.sleep(1)
                    screen_title()
                    print(f'\n! Now {player_current[1]} {player_current[2]} sign')
                    print(SIGN_SCREEN_START+player_current[3]+SIGN_SCREEN_END)
                    move_medium(player_current, player_1, player_2, board_availlable, board_status, board_winning)
                    display_board(board_status)
                    game_status = status(board_status, player_current, game_statistic_table)
                    player_current = signe_change(player_current)

if __name__ == "__main__":
    game_start()