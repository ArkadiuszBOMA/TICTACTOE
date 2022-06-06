from game_stat import game_statis
from screen_deposit import screen_title
import time
import os

from screen_deposit import screen_title
'''
This module sets the game parameters:
First you choose who is playing. You have 4 options
  1- Human    against   Computer
  2- Computer against   Human
  3- Human    against   Human
  4- Computer against   Computer
above is driven by def select_palyers

Depending user choice def asigne_players if his/her choice was 1, 2 or 4, user must also choose the computer difficulty level.
this is driven by def asigne_difficulty
You have 3 options
  1- Easy   - then the computer chooses randomly from among the available free fields
  2- Medium - the computer tries to pick the square that gives it a win
You always have the option to stop application by entering the word quit
'''
def select_palyers(players_availlable, player_1, player_2, players_availlable_difficulty,game_statistic_table):
    while True:
        select_players = input(f'! You can determine who play the game please enter \n  1- for Human    vs  Computer\n  2- for Computer vs  Human\
            \n  3- for Human    vs  Human\n  4- for Computer vs  Computer\n  You can also exit the game typing quit.\n\n  What is Your choice? -> ')
        if select_players.lower() != "quit":
            if select_players not in players_availlable:
                screen_title()
                print(f'! Your have entered > {select_players} <. It is wrong !')
                print("-" * 126)
            else:
                screen_title()
                print(f'! You have chosen > {select_players} < so {players_availlable[select_players][0]} will paly against {players_availlable[select_players][1]}\n')
                player_1[2] = players_availlable[select_players][0]
                player_2[2] = players_availlable[select_players][1]
                asigne_players(select_players, player_1, player_2, players_availlable_difficulty,game_statistic_table)
                print("-" * 126)
                time.sleep(1)
                return False
        else:
            game_writ_stat = [str(game_statistic_table[0]),str(game_statistic_table[1]), str(game_statistic_table[2]), str(game_statistic_table[3]), str(game_statistic_table[4]), str(game_statistic_table[5])]
            screen_title()
            game_statis(game_writ_stat)
            print("! See you next time !")
            print("-" * 126)
            print(f"The game was played {game_statistic_table[0]} times already\n\t{game_statistic_table[1]} times win 'X'\n\t{game_statistic_table[2]} times win 'O'\
                \n\t{game_statistic_table[3]} times win Human\n\t{game_statistic_table[4]} times win Computer\n\t{game_statistic_table[5]} was Draw")
            print("-" * 126)
            exit()

def asigne_players(select_players, player_1, player_2, players_availlable_difficulty,game_statistic_table):
    if select_players == "1":
        screen_title()
        player_1[1] = "USER"
        print(f"! You start, please assign difficulty for your opponent the Computer")
        player_2[1] = asigne_difficulty(players_availlable_difficulty,game_statistic_table)
    elif select_players == "2":
        screen_title()
        print(f"! Please assign difficulty level for your opponent the Computer that begin the game")
        player_1[1] = asigne_difficulty(players_availlable_difficulty,game_statistic_table)
        player_2[1] = "USER"
    elif select_players == "3":
        player_1[1] = "USER"
        player_2[1] = "USER"
    else:
        screen_title()
        print("! Please assign difficulty level for Computer 1")
        player_1[1] = asigne_difficulty(players_availlable_difficulty,game_statistic_table)
        time.sleep(2)
        print("! Please assign difficulty level for Computer 2")
        player_2[1] = asigne_difficulty(players_availlable_difficulty,game_statistic_table)
        time.sleep(2)

def asigne_difficulty(players_availlable_difficulty,game_statistic_table):
    while True:
        game_level = input(f'You can choose among \n  1- for EASY\n  2- for HARD\
            \nYou can also exit the game typing quit.\n\n  Your choice is -> ')
        if game_level.lower() != "quit":
            if game_level not in players_availlable_difficulty:
                screen_title()
                print(f'! Your have entered > {game_level} <. It is wrong !')
                print("-" * 126)
            else:
                screen_title()
                print(f'! You have chosen > {game_level} <\n so Computer will play {players_availlable_difficulty[game_level]} ')
                print("-" * 126)
                return players_availlable_difficulty[game_level]
        else:
            screen_title()
            print("! See you next time !")
            print("-" * 126)
            print(f"The game was played {game_statistic_table[0]} already\n\t{game_statistic_table[1]} times win 'X'\n\t{game_statistic_table[2]} times win 'O'\
                \n\t{game_statistic_table[3]} times win Human\n\t{game_statistic_table[1]} times win Computer\n\t{game_statistic_table[1]} was Draw")
            print("-" * 126)  
            exit()