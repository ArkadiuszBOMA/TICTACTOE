'''
This module provide computer coordinates.
Ther are two options:
1- easy - coordinates randomly taken from availlable unused places
2- medium - first computer check for competitor winning place and if such take this place as coordinates for its move
not necessary to check validity as computer uses only valid places and provide corect data
'''
import random

def move_easy(board_availlable,board_status, player_current):
    a = random.choice(board_availlable)
    board_status[a] = player_current[0]


def move_medium(player_current, player_1, player_2, board_availlable, board_status, board_winning):
    if len(board_availlable) == 9:
        board_status[4] = player_current[0]
    elif len(board_availlable) == 8:
        if board_status[4] == '.':
            board_status[4] = player_current[0]
        elif board_status[0] == '.':
            board_status[0] = player_current[0]
        elif board_status[2] == '.':
            board_status[2] = player_current[0]
        elif board_status[6] == '.':
            board_status[6] = player_current[0]
        elif board_status[8] == '.':
            board_status[8] = player_current[0]
    elif len(board_availlable) == 7:
        if board_status[1] != '.':
            board_status[0] = player_current[0]
        elif board_status[3] != '.':
            board_status[0] = player_current[0]
        elif board_status[5] != '.':
            board_status[3] = player_current[0]
        elif board_status[8] != '.':
            board_status[5] = player_current[0]
        else:
            board_medium_winning = []                                           # sprawdzenie możliwości wygranej
            competitir = player_current
            for i in board_availlable:
                board_winning = board_status
                board_winning[i] = competitir[0]
                if (board_winning[0] == competitir[0] and board_winning[1] == competitir[0] and board_winning[2] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[3] == competitir[0] and board_winning[4] == competitir[0] and board_winning[5] == competitir[0]):                        
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[6] == competitir[0] and board_winning[7] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[0] == competitir[0] and board_winning[3] == competitir[0] and board_winning[6] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[1] == competitir[0] and board_winning[4] == competitir[0] and board_winning[7] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[2] == competitir[0] and board_winning[5] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[0] == competitir[0] and board_winning[4] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[2] == competitir[0] and board_winning[4] == competitir[0] and board_winning[6] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                else:
                    board_winning[i] = "."
            if len(board_medium_winning) == 0:                                  # sprawdzenie możliwości wygranej przeciwnika
                board_medium_winning = []
                if player_current == player_1:
                    competitir = player_2
                else:
                    competitir = player_1
                for i in board_availlable:
                    board_winning = board_status
                    board_winning[i] = competitir[0]
                    if (board_winning[0] == competitir[0] and board_winning[1] == competitir[0] and board_winning[2] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[3] == competitir[0] and board_winning[4] == competitir[0] and board_winning[5] == competitir[0]):                        
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[6] == competitir[0] and board_winning[7] == competitir[0] and board_winning[8] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[0] == competitir[0] and board_winning[3] == competitir[0] and board_winning[6] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[1] == competitir[0] and board_winning[4] == competitir[0] and board_winning[7] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[2] == competitir[0] and board_winning[5] == competitir[0] and board_winning[8] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[0] == competitir[0] and board_winning[4] == competitir[0] and board_winning[8] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    elif (board_winning[2] == competitir[0] and board_winning[4] == competitir[0] and board_winning[6] == competitir[0]):
                        board_medium_winning.append(i)
                        board_winning[i] = "."
                    else:
                        board_winning[i] = "."
                if len(board_medium_winning) == 0:                              # jeżeli przeciwnik w następnym ruchu nie ma wygranej oraz nie ma rychu z możliwością wygranej 
                    move_easy(board_availlable,board_status, player_current)    # weż losowa wartość z dostępnych wolnych pól
                else:
                    a = random.choice(board_medium_winning)                     # istnieje pole w którym przeciwnik może wygrać więc blokuj je wstawiając włąsny znak
                    board_status[a] = player_current[0]
            else:
                a = random.choice(board_medium_winning)                         # istnieje pole z możliwością wygranej weżeje
                board_status[a] = player_current[0]
    else:
        board_medium_winning = []                                           # sprawdzenie możliwości wygranej
        competitir = player_current
        for i in board_availlable:
            board_winning = board_status
            board_winning[i] = competitir[0]
            if (board_winning[0] == competitir[0] and board_winning[1] == competitir[0] and board_winning[2] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[3] == competitir[0] and board_winning[4] == competitir[0] and board_winning[5] == competitir[0]):                        
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[6] == competitir[0] and board_winning[7] == competitir[0] and board_winning[8] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[0] == competitir[0] and board_winning[3] == competitir[0] and board_winning[6] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[1] == competitir[0] and board_winning[4] == competitir[0] and board_winning[7] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[2] == competitir[0] and board_winning[5] == competitir[0] and board_winning[8] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[0] == competitir[0] and board_winning[4] == competitir[0] and board_winning[8] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            elif (board_winning[2] == competitir[0] and board_winning[4] == competitir[0] and board_winning[6] == competitir[0]):
                board_medium_winning.append(i)
                board_winning[i] = "."
            else:
                board_winning[i] = "."
        if len(board_medium_winning) == 0:                                  # sprawdzenie możliwości wygranej przeciwnika
            board_medium_winning = []
            if player_current == player_1:
                competitir = player_2
            else:
                competitir = player_1
            for i in board_availlable:
                board_winning = board_status
                board_winning[i] = competitir[0]
                if (board_winning[0] == competitir[0] and board_winning[1] == competitir[0] and board_winning[2] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[3] == competitir[0] and board_winning[4] == competitir[0] and board_winning[5] == competitir[0]):                        
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[6] == competitir[0] and board_winning[7] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[0] == competitir[0] and board_winning[3] == competitir[0] and board_winning[6] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[1] == competitir[0] and board_winning[4] == competitir[0] and board_winning[7] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[2] == competitir[0] and board_winning[5] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[0] == competitir[0] and board_winning[4] == competitir[0] and board_winning[8] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                elif (board_winning[2] == competitir[0] and board_winning[4] == competitir[0] and board_winning[6] == competitir[0]):
                    board_medium_winning.append(i)
                    board_winning[i] = "."
                else:
                    board_winning[i] = "."
            if len(board_medium_winning) == 0:                              # jeżeli przeciwnik w następnym ruchu nie ma wygranej oraz nie ma rychu z możliwością wygranej 
                move_easy(board_availlable,board_status, player_current)    # weż losowa wartość z dostępnych wolnych pól
            else:
                a = random.choice(board_medium_winning)                     # istnieje pole w którym przeciwnik może wygrać więc blokuj je wstawiając włąsny znak
                board_status[a] = player_current[0]
        else:
            a = random.choice(board_medium_winning)                         # istnieje pole z możliwością wygranej weżeje
            board_status[a] = player_current[0]

                