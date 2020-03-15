"""
    This Class is for playing a guessing game. Computer will generate one
    3-digit number and user has to guess what that would be. User have 10
    times to guess. Each time the user inputted the number, if the placing
    of the inputted numbers are correct, The program will show the number
    of "HIT". If the user inputted numbers are correct but the placing are
    wrong, the program will show the number of "BLOW".
"""

import random
computerArray = [0, 0, 0]  # Computer Generated Array
inputInt = [0, 0, 0]
storedArray = []
arrayforNthTime = ['First', 'Second', 'Third', 'Fourth',
                   'Fifth', 'Sixth', 'Seventh', 'Eight', 'Nineth', 'Tenth']
ramdomMaxNumber = 9
indexMaxNum = 2
arrayMaxNumber = 3
savedArray = 0
countNum = 10


def Main():
    """
     This is the main class which calls for generating the random numbers,
     checking hit and blow counts,checking the user inputs formats.
    """
    generateRandomNumber()
    print("Start Hit & Blow !")
    inputCount = 0
    print("The ", arrayforNthTime[inputCount], " challenge !")
    while(inputCount < countNum):
        checkUserInput()
        notWin = checkHitandBlow()
        if(notWin is True):
            print("The Correct Answer")
            inputCount = countNum
        elif(inputCount <= countNum):
            inputCount += 1
            print("")
            if(inputCount == countNum):
                print("Unfortunately Fail. The answer is {}{}{}"
                      .format(computerArray[0], computerArray[1],
                              computerArray[indexMaxNum]))
            else:
                print("The ", arrayforNthTime[inputCount], " challenge !")


def checkUserInput():
    """
        this function is for checing the user inputs,
        it can check
        - the overlapping input numbers
        - if the current inputted number is already existed or not
        - if the inputted number is 3 digit or not
        - if the input is string or the number
    """
    try:
        usrIN = input("Please input three columns of digit values : ")
        storedValue = usrIN
        maxLength = 3
        if len(storedArray) > 0:
            while storedValue in storedArray:
                usrIN = input("Try another number : ")
                storedValue = usrIN

        while (len(usrIN) != maxLength or usrIN[0] == usrIN[1] or
                usrIN[0] == usrIN[indexMaxNum] or usrIN[1] ==
                usrIN[indexMaxNum] or storedValue in storedArray):
            usrIN = input("Numbers are overlapping or Not Equal to 3"
                          " columns, Please Input again : ")
            storedValue = usrIN
    except:
        usrIN = input("You Inputted wrong Number or Format : ")
        if len(storedArray) > 0:
            while storedValue in storedArray:
                usrIN = input("Try another number : ")
                storedValue = usrIN

        while (len(usrIN) != maxLength or usrIN[0] == usrIN[1] or
                usrIN[0] == usrIN[indexMaxNum] or usrIN[1] ==
                usrIN[indexMaxNum] or storedValue in storedArray):
            usrIN = input("Numbers are overlapping or Not Equal to 3"
                          "columns, Please Input again : ")
            storedValue = usrIN
    storedArray.append(usrIN)
    for ArrayIndex in range(arrayMaxNumber):
        inputInt[ArrayIndex] = int(usrIN[ArrayIndex])


def generateRandomNumber():
    """
        This function is for generating the random numbers,
        The first digit will never be '0'
        The random values will not overlap
    """
    for RandomArrayIndex in range(0, arrayMaxNumber, 1):
        randomNumber = random.randint(0, ramdomMaxNumber)
        if RandomArrayIndex == 0:
            while(randomNumber == 0):
                randomNumber = random.randint(0, ramdomMaxNumber)
            computerArray[0] = randomNumber
        elif RandomArrayIndex == 1:
            computerArray[1] = randomNumber
            while computerArray[0] == computerArray[1]:
                randomNumber = random.randint(0, ramdomMaxNumber)
                computerArray[1] = randomNumber
        elif RandomArrayIndex == indexMaxNum:
            computerArray[1] = randomNumber
            while(computerArray[0] == computerArray[1] or
                    computerArray[0] == computerArray[indexMaxNum] or
                    computerArray[1] == computerArray[indexMaxNum]):
                randomNumber = random.randint(0, ramdomMaxNumber)
                computerArray[indexMaxNum] = randomNumber
    return computerArray


def checkHitandBlow():
    """
        This function is for checking the numbers of hit and blow
        counts.if the placing of the inputted number and the random
        number is corrrect, Hit count will be plus by one. if the
        inputted number is correct but the placing is wrong, the blow
        will be plus by ones. if the blow count is  3 and hit count also 3
        the user wins.
    """
    HITcount = 0
    Blowcount = 0
    win = False
    for BlowIndexOne in range(0, arrayMaxNumber, 1):
        for BlowIndexTwo in range(0, arrayMaxNumber, 1):
            if(computerArray[BlowIndexOne] == inputInt[BlowIndexTwo]):
                Blowcount += 1
    for hitIndexOne in range(0, arrayMaxNumber, 1):
        if(computerArray[hitIndexOne] == inputInt[hitIndexOne]):
            HITcount += 1
    if (Blowcount == arrayMaxNumber and HITcount == arrayMaxNumber):
        win = True
    else:
        print("HIT  : ", HITcount)
        print("BLOW : ", Blowcount)

    return win


if __name__ == '__main__':
    Main()
