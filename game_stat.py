"""
We try to learn and last lesson was related to file managment. Even the game instuction does not requiers we add this
to practice as much as Possible and utilise CodeCool to extreme.

The file name is game_statistic.txt

6 data is coleected while game runs in 6 rows of the file:

1- line  - numbers of application useed
2- line  - number of x wins
3- line  - number of o wins
4- line  - number of Human wins
5- line  - number of Computer wins
6- line  - number of Draw

"""

game_statistic_table_1 = [0,0,0,0,0,0]

def game_statis(game_writ_stat):
    with open("game_statistic.txt", "w", encoding='utf8') as gs_file:
        gs_file.write('\n'.join(game_writ_stat))

def get_game_statistic_stat():
    global game_statistic_table_1
    with open("game_statistic.txt", "r", encoding='utf8') as gs_file:
        lines = gs_file.readlines()
        gs_file.seek(0)
        for number, line in enumerate(lines):
            game_statistic_table_1[number] = int(line.strip('\n'))
        game_writ_stat = [str(game_statistic_table_1[0]),str(game_statistic_table_1[1]), str(game_statistic_table_1[2]), str(game_statistic_table_1[3]), str(game_statistic_table_1[4]), str(game_statistic_table_1[5])]
        game_statis(game_writ_stat)
        print(f"The application was used {game_statistic_table_1[0]} times already\n\t{game_statistic_table_1[1]} times win 'X'\n\t{game_statistic_table_1[2]} times win 'O'\n\t{game_statistic_table_1[3]} times win Human\n\t{game_statistic_table_1[4]} times win Computer\n\t{game_statistic_table_1[5]} was Draw")
        print("-" * 126)
