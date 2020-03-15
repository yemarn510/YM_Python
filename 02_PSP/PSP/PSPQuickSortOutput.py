"""
    This class is used for only printing out the array values
    one by one
"""
import PSPQuickSort


def printArray(sortedArray):
    """
        This fiunction is only for printing out the values
        arg : sortedArry : the sorted Array
    """
    if len(sortedArray) > 0:
        print("Sorted array is:")
        for secIndex in range(0, len(sortedArray), 1):
            print(sortedArray[secIndex])

    else:
        print("\n The file is empty \n")
