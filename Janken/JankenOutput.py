"""
    This class is for printing message and showing who is
"""
from random import randrange


def show_winner(player_one_count, player_two_count):
    """
        This is the function for outputting who is the winner
        args : player_one_count : the number of games player 1 won
             : player_two_count : the number of games player 2 won
    """
    print("The Score is {}-{}. ".format(str(player_one_count),
                                        str(player_two_count)),
          end='')
    if player_one_count > player_two_count:
        print("Player 1 wins.")
    elif player_one_count < player_two_count:
        print("player 2 wins.")
    else:
        print("The Game is Draw")
