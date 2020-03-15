import sys
import os


def read_file():
    """
        This is the function for checking if the file exists
        or not
        return : file_name : the name of the file
    """
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if os.path.exists(file_name):
            print("============")
            print(file_name)
            try:
                read_file = open(file_name, "r")
            except():
                file_name.close()
                print("Fail to read {}{}{}\n".format(r'"', file_name, r'"'))
            # finally:
            #     print("An error occoured")
            return file_name
        else:
            print("File {}{}{} is not found\n".format(r'"', file_name, r'"'))
            return "Nothing"

    else:
        print("No file name is input\n")
        return "Nothing"
