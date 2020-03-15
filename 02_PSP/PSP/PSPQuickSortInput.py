"""
    This class checks
    -if the inputted file name is a text file or word file
    -if the text files contains strings between the float
     values
    -if the
"""
import os.path
array = []
tempArray = []


def getArray(fileName):
    """
        This function removes the '\n' and '\t' and check if the text file
        exists in the directory.
        This function also detects the strings and show message

        args : fileName : user inputted file name or file name
        return : fileError: file error
               : tempArray : array for processing and removing '\t' and '\n'
               : array: unsorted array
    """
    fileError = False
    fileNameforInput = "Textfiles\\" + fileName + '.txt'
    if os.path.exists(fileNameforInput):
        fileReader = open(fileNameforInput, "r")
        for lines in fileReader:
            lines = lines.replace('\n', '')
            lines = lines.replace('\t', '')
            lines = lines.replace(' ', '')
            tempArray.append(lines)
        while '' in tempArray:
            tempArray.remove('')
        for valuesInArr in tempArray:
            try:
                okLines = float(valuesInArr)
                array.append(okLines)
            except ValueError:
                fileError = True
                print("\n The Lines contain Strings \n")
                return fileError
                fileReader.close()
        return array
        fileReader.close()
    else:
        print("\n The File Name does not exist \n")
        fileError = True
        return fileError
        fileReader.close()
