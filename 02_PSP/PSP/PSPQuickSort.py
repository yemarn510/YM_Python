"""
    This is the main class for sorting values from the text file.
    This class can skip blank lines.
    This class will be closed if there is the string values in the text filse.
    This class will print out the sorted array if there is no string values
    in the file.
"""
import argparse
import PSPQuickSortInput
import PSPQuickSortProcess
import PSPQuickSortOutput


def Main():
    """
        This function accepts the command line argument for
        input text file names.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName", type=str,
                        help="Input text file Name")
    fileName = (parser.parse_args()).fileName
    randomArray = PSPQuickSortInput.getArray(fileName)
    if randomArray is True:
        pass
    else:
        sortedArray = PSPQuickSortProcess.sort(randomArray)
        PSPQuickSortOutput.printArray(sortedArray)


if __name__ == '__main__':
    Main()
