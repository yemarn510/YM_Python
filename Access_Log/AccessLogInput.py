import sys
import re
import os
import AccessLogOutput


def Input():
    """
        This function is for getting the file name and
        search word.
        This function can check
        -if the file exists or not
        -if the user input the file name or not
        -if the the user input the file that does not exist

        return : file_name : file name
               : search_word : the word that the user want to search
    """

    if len(sys.argv) == 1:
        file_name = 'file_error'
        search_word = ''
        return file_name, search_word

    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
        if os.path.exists(file_name):
            search_word = ''
            return file_name, search_word
        else:
            file_name = ''
            search_word = ''
            return file_name, search_word

    elif len(sys.argv) == 3:
        file_name = sys.argv[1]
        search_word = sys.argv[2]
        if os.path.exists(file_name):
            return file_name, search_word
        else:
            file_name = ''
            search_word = ''
            return file_name, search_word

    else:
        file_name = ''
        search_word = ''
        return file_name, search_word
