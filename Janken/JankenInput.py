"""
    This is the class for getting command line arguments
"""
import sys
minimum_arg = 1
num_play_exist = 2
player_one_exist = 3
player_two_exist = 4


def check_inputs():
    """
        This function check the command line arguments
        return appropriate data to the main class
        arg :
        return : num_play : the number of games
               : first_strate : player1 Strategy
               : sec_strate : player2 Strategy
    """
    if len(sys.argv) == minimum_arg:
        print("\n Input the number of games \n")
        num_play = 'Nothing'
        first_strate = 0
        sec_strate = 0
        return num_play, first_strate, sec_strate

    elif len(sys.argv) == num_play_exist:
        num_play = int(sys.argv[1])
        first_strate = 1
        sec_strate = 1
        return num_play, first_strate, sec_strate

    elif len(sys.argv) == player_one_exist:
        num_play = int(sys.argv[1])
        first_strate = int(sys.argv[num_play_exist])
        sec_strate = 1
        return num_play, first_strate, sec_strate

    elif len(sys.argv) == player_two_exist:
        num_play = int(sys.argv[1])
        first_strate = int(sys.argv[num_play_exist])
        sec_strate = int(sys.argv[player_one_exist])
        return num_play, first_strate, sec_strate

    else:
        print("\nError\n")
        num_play = 'Nothing'
        first_strate = 0
        sec_strate = 0
        return num_play, first_strate, sec_strate

