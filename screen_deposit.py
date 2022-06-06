import os

HELP_SCREEN_STARTT = '\033[3;32;40m'
HELP_SCREEN_END = '\033[0;37;40m'

game_help =(HELP_SCREEN_STARTT+
    '''
    TIC-TAK-TOE by Paulina & Arek
    ___________________________________________________________________________________________________________________
    Following WIKIPEDIA - https://en.wikipedia.org/wiki/Tic-tac-toe?msclkid=464a4905d05d11ec88638b810a995cf3

    Tic-tac-toe (American English), noughts and crosses (Commonwealth English), or Xs and Os (Irish English) 
    is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. 
    The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 
    It is a solved game, with a forced draw assuming best play from both players.

    Games played on three-in-a-row boards can be traced back to ancient Egypt, 
    where such game boards have been found on roofing tiles dating from around 1300 BC
    ___________________________________________________________________________________________________________________
    You can start the game using terminal simply type:
    1- python tic_tac_toe.py
    2- python tic_tac_toe.py play
    cls
    You can read game help directly from terminal by typing -> python tic_tac_toe.py help
    You can read game statistics from terminal by typing    -> python tic_tac_toe.py stat

    At the beginning you must determine who plays the game for which You have 4 available options:

        1- Human    against   Computer
        2- Computer against   Human
        3- Human    against   Human
        4- Computer against   Computer
    
    Depending your choice, except option 3 (Human vs Human) , user must choose difficulty level for the computer among 2 options.
        1- EASY - the computer chooses randomly from available free fields
        2- HARD - the computer tries to pick the square that gives it a win
    
    You always have the option to stop application by entering the word quit.
    ___________________________________________________________________________________________________________________
    '''
    +HELP_SCREEN_END)

game_titele = (
    """                                                                                   
       ######### ### #########    ######### ######### #########    #########  #######  #########      1   |  2   |  3
      ######### ### #########    ######### ######### #########    ######### ######### #########     ------+------+-----
        ###    ### ###             ###    ###   ### ###             ###    ###   ### ###         A    X   |  .   |  .    
       ###    ### ###       ###   ###    ###   ### ###      ###    ###    ###   ### ######          ------+------+-----
      ###    ### ###             ###    ######### ###             ###    ###   ### ###           B    .   |  O   |  .      
     ###    ### #########       ###    ###   ### #########       ###    ######### #########         ------+------+-----
    ###    ### #########       ###    ###   ### #########       ###     #######  #########       C    .   |  .   |  X   

    created by Paulina & Arek
    """
)

game_signes = (
    """
           ###   ###
            ### ###
              ###
            ### ###
           ###   ###  
    """,
    """
            #######
           ###   ###
           ###   ###
           ###   ###
            #######
    """  )
    
def screen_title():
    os.system("cls")
    print(game_titele)
    print("-" * 126)

if __name__ == "__main__":
    screen_title()
    print(game_help)