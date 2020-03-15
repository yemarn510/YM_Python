"""
    This is the main class for playing Janken
"""
import JankenInput
import JankenOutput
import JankenProcess


def Main():
    """
        This is the main function for playing Janken
    """

    # Getting inputs
    num_play, first_strate, sec_strate = JankenInput.check_inputs()
    if num_play != 'Nothing':
        # Preparing Arrays
        player_one_arr, player_two_arr = JankenProcess.prepare_arrays(
            num_play, first_strate, sec_strate)

        # Judging arrays
        player_one_count, player_two_count = JankenProcess.judging_results(
            num_play, player_one_arr, player_two_arr)

        # Show the winner
        JankenOutput.show_winner(player_one_count, player_two_count)


if __name__ == "__main__":
    Main()
