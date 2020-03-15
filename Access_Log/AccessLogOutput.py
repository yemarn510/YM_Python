import re
import AccessLog


def show_errormsg():
    """
        This function is for printing the error message for files
        that does not exist
    """
    print("\nTarget file does not exist, please put correct path for the file")
    print()


def show_all_line(file_name, search_word):
    """
        This function is for printing every line in the files
        args : file_name : file_name
             : search_word : ''
    """
    files = open(file_name, 'r')
    for lines in files:
        print(lines)
    files.close()


def does_not_exist_file():
    """
        This function is for printing if the user doesn't
        input the first command line argument
    """
    print("\nPlease input the file name\n")


def output_array(array_to_print):
    """
        This function is for printing the array which includes
        the word that the user wants to search
        arg : arry_to_input : the array with lines that include
                              the search words
    """
    for lines in array_to_print:
        print(lines)
