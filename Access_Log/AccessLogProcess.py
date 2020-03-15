import re
import AccessLogInput
array_to_print = []


def search(file_name, search_word):
    """
        This function is for searching the search word(s)
        inside the file
        args : file_name : file name in the same directory
        return : array_to_print : the array with lines
                                  that contains the search
                                  word
    """
    files = open(file_name, 'r')
    for lines in files:
        if re.search(search_word, lines):
            array_to_print.append(lines)
    files.close()
    return array_to_print
