"""
    This class does the sorting usins quicksort algorithm.
    The way the quicksort algorithm does is
    -Set pivot
    -Set the lower and upper index value
    -Sort while swapping the values
    -Set the pivot again
    -Set the lower and upper index value
    and so on
"""
import PSPQuickSort
sortedArray = []


def sort(randomArray):
    """
        This is the Main function for sorting the random

        arg : ramdomArray : unsorted random array
        return : sortedArray: sorted array
    """
    lenRDMArray = len(randomArray)
    quickSort(randomArray, 0, lenRDMArray-1)
    for index in range(lenRDMArray):
        sortedArray.append(randomArray[index])
    return sortedArray


def partition(randomArray, low, high):
    """
        This function is for sorting the array, pointing the samllest
        value as smallerValueIndex and looping throung. If the loop
        index value found the smaller value than the pivot, Swap the
        smallest and the loop index value
    """
    smallerValIndex = (low-1)
    pivot = randomArray[high]

    for loopIndex in range(low, high):

        if randomArray[loopIndex] < pivot:

            smallerValIndex = smallerValIndex+1
            randomArray[smallerValIndex], randomArray[loopIndex] = \
                randomArray[loopIndex], randomArray[smallerValIndex]

    randomArray[smallerValIndex+1], randomArray[high] = \
        randomArray[high], randomArray[smallerValIndex+1]
    return (smallerValIndex+1)


def quickSort(randomArray, low, high):
    """
        This function is for setting the upper and lower index values
        to be sorted, mainly left and right.
    """
    if low < high:

        partationValue = partition(randomArray, low, high)
        quickSort(randomArray, low, partationValue-1)
        quickSort(randomArray, partationValue+1, high)
