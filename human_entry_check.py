from game_stat import game_statis
'''
This module validates the entered coordinates.
The data to be entered is two charecters first is a letter A, B, C and second is number 1,2,3.
The letter indicates the row, the number indicates the column - both is called coordinates
If the entered value is incorrect then an error message appears.

You always have the option to stop application by entering the word quit
'''
def move_human(indicator_rows, indicator_colums, board_moves, board_status, player_current, game_statistic_table):
    humne_check = True
    while humne_check == True:
        player_move = input('Plese enter the coordinates the folowing format letter number - example > A1 < \n ! The letter only A, B, C and number only 1, 2, 3 :\n ! You can exit game typing quit\n ! Your coardinates is > ')
        print()
        if player_move.lower() != "quit":
            if not player_move or len(player_move) != 2:
              print("-" * 126)
              print(f'! Your entry > {player_move} < is wrong try again')
              print("-" * 126)
              humne_check == False
            elif player_move[0].upper() not in indicator_rows or player_move[1] not in indicator_colums:
                print("-" * 126)
                print(f' ! Please look what you have entered > {player_move} <.\n ! Your entry is wrong. Again availlable lettres are: A, B, C Numbers are: 1, 2, 3\n ! Try again: ' )
                print("-" * 126)
                humne_check == False
            else:
                for i in range(len(board_moves)):
                    if player_move.upper() == board_moves[i] and board_status[i] == '.':
                        board_status[i] = player_current[0]
                        return (board_status, False)
                print("-" * 126)
                print(' ! This place is occupied, try again')
                print("-" * 126)
                humne_check == False
        else:
            print("\n! See you next time !")
            print("-" * 126)
            game_writ_stat = [str(game_statistic_table[0]),str(game_statistic_table[1]), str(game_statistic_table[2]), str(game_statistic_table[3]), str(game_statistic_table[4]), str(game_statistic_table[5])]
            game_statis(game_writ_stat)
            print(f"The application was used {game_statistic_table[0]} times already\n\t{game_statistic_table[1]} times win 'X'\n\t{game_statistic_table[2]} times win 'O'\n\t{game_statistic_table[3]} times win Human\n\t{game_statistic_table[4]} times win Computer\n\t{game_statistic_table[5]} was Draw")
            print("-" * 126)
            exit()
  