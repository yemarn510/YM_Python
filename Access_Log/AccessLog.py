"""
    This is the main program for searching the words inside the file
"""
import AccessLogInput
import AccessLogOutput
import AccessLogProcess


def Main():
    """
        This is the main class for handling and executing
        all the functions.
    """
    file_name, search_word = AccessLogInput.Input()

    # print_error_message
    if file_name == '' and search_word == '':
        AccessLogOutput.show_errormsg()

    # for no argument inputs
    elif file_name == 'file_error':
        AccessLogOutput.does_not_exist_file()

    # print_everything_case
    elif file_name and search_word == '':
        AccessLogOutput.output_everything(file_name, search_word)

    # normal_case
    elif file_name and search_word:
        array_to_print = AccessLogProcess.search(file_name, search_word)
        AccessLogOutput.output_array(array_to_print)


if __name__ == "__main__":
    Main()
