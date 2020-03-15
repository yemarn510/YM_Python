"""
    This class is for preparing arrays, judging the results and
    checking which player do which action.
"""
from random import randrange


def prepare_arrays(num_play, first_strate, sec_strate):
    """
        This is the function for creating arrays according to
        the user inputs
        arg : num_play : the number of games
            : first_strate : player1 Strategy
            : sec_strate : player2 Strategy
        return : p_one : player1 array
               : p_two : player2 array
    """
    player_one_strate_one = 1
    player_one_strate_two = 2
    player_one_strate_three = 3

    player_two_strate_one = 1
    player_two_strate_two = 2
    player_two_strate_three = 3

    if first_strate == player_one_strate_one:
        player_one = random(num_play)
    elif first_strate == player_one_strate_two:
        player_one = create_only_rock(num_play)
    elif first_strate == player_one_strate_three:
        player_one = create_cycle(num_play)

    if sec_strate == player_two_strate_one:
        player_two = random(num_play)
    elif sec_strate == player_two_strate_two:
        player_two = create_only_rock(num_play)
    elif sec_strate == player_two_strate_three:
        player_two = create_cycle(num_play)

    return player_one, player_two


def judging_results(num_play, player_one, player_two):
    """
        This is the function for checking the arrays and decides
        who wins each game
        arg : num_play : the numbers of game
            : player_one : player1 array
            : player_two : player2 array
        return : player_one_count : the number of games that player 1 won
               : player_two_count : the number of games that player 2 won
    """
    player_one_count = 0
    player_two_count = 0
    rand_max = 4
    rand_min = 1
    JanKen_array = ['', "Paper", "Rock", "Scissors"]
    number_to_print_array = ["First", "Second", "Third",
                             "Fourth", "Fifth", "Sixth", "Seventh", "Eight"]
    for numbers in range(0, len(player_one), 1):
        print('[{}'.format(str(number_to_print_array[numbers])), "Play]")

        if player_one[numbers] == player_two[numbers]:
            print(JanKen_array[player_one[numbers]],
                  "vs", JanKen_array[player_two[numbers]])
            print("Even.")
            print()
            even = True
            while even:
                extra_one = randrange(rand_min, rand_max)
                extra_two = randrange(rand_min, rand_max)
                if extra_one == extra_two:
                    even = True
                else:
                    even_player_one = extra_one
                    even_player_two = extra_two
                    player_one_count, player_two_count = play_jenken(
                        even_player_one, even_player_two, player_one_count,
                        player_two_count)
                    even = False
        else:
            even_player_one = player_one[numbers]
            even_player_two = player_two[numbers]
            player_one_count, player_two_count = play_jenken(
                even_player_one, even_player_two, player_one_count,
                player_two_count)
        print()

    return player_one_count, player_two_count


def play_jenken(even_player_one, even_player_two, player_one_count,
                player_two_count):
    """
        This is the main function for making decisions which player wins
        arg : even_player_one : player 1 argument for passing functions
            : even_player_two : player 2 argument for passing functions
            : player_one_count : the number of games player 1 won
            : player_two_count : the number of games player 2 won
        return : player_one_count : the number of games player 1 won
               : player_two_count : the number of games player 2 won
    """
    JanKen_array = ['', "Paper", "Rock", "Scissors"]
    forward_skip_seq = 2
    backward_skip_seq = -2

    if even_player_one-even_player_two == 1:
        print(JanKen_array[even_player_one],
              "vs", JanKen_array[even_player_two])
        print("Player 2 wins")
        player_two_count = player_two_count + 1
    elif even_player_one-even_player_two == forward_skip_seq:
        print(JanKen_array[even_player_one],
              "vs", JanKen_array[even_player_two])
        print("Player 1 wins")
        player_one_count = player_one_count + 1
    elif even_player_one-even_player_two == -1:
        print(JanKen_array[even_player_one],
              "vs", JanKen_array[even_player_two])
        print("Player 1 wins")
        player_one_count = player_one_count + 1
    elif even_player_one-even_player_two == backward_skip_seq:
        print(JanKen_array[even_player_one],
              "vs", JanKen_array[even_player_two])
        print("Player 2 wins")
        player_two_count = player_two_count + 1
    else:
        pass
    return player_one_count, player_two_count


def random(num_play):
    """
        This is the function for generating random arrays
        arg : num_play : the number of games
        return : random_array : the array with random numbers
    """
    # generate the random array
    rand_max = 4
    rand_min = 1

    random_array = []
    for index in range(0, num_play, 1):
        random_array.append(randrange(rand_min, rand_max))
    return random_array


def create_only_rock(num_play):
    """
        This is the function for generating an array which contains
        only 2
        args : num_play : the number of games
        return : only_rock_array : the array with only value 2
    """
    # generate only rock array
    only_rock = 2

    only_rock_array = []
    for index in range(0, num_play, 1):
        only_rock_array.append(only_rock)
    return only_rock_array


def create_cycle(num_play):
    """
        This is the function for gererating the values that contains 1,2,3
        consequencly
        args : num_play : the number of games
        return : cycle_array : the array that contains in order 1,2,3
    """
    cycle_array = []
    cycel_count = 1
    max_cyc_cnt = 4

    for index in range(0, num_play, 1):
        if cycel_count == max_cyc_cnt:
            cycel_count = 1
        cycle_array.append(cycel_count)
        cycel_count = cycel_count + 1
    return cycle_array
