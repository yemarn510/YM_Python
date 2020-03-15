import argparse


def Main():
    """
        This is the Main fuction for calculator
        arg : userInput : User inputted expression.
        if the user enters blank, the program will be finished.
    """
    leave = True
    while leave:
        userInput = input("enter numerical expression : ")
        if userInput == '':
            leave = False
        if '*' in userInput:
            multi = int(userInput.index('*'))
            operatorIndex = multi+1
            first = userInput[:multi]
            second = userInput[multi+1:]
            try:
                if (userInput[operatorIndex] == "+"
                    or userInput[operatorIndex] == '-'
                    or userInput[operatorIndex] == '*'
                    or userInput[operatorIndex] == '/'
                        or userInput[operatorIndex] == ' '):
                    errorMessage()
                else:
                    answer = float(first) * float(second)
                    print('result is:', answer, '\n')
            except ValueError:
                errorMessage()

        elif '/' in userInput:
            multi = int(userInput.index('/'))
            operatorIndex = multi+1
            first = userInput[:multi]
            second = userInput[multi+1:]
            try:
                if (userInput[operatorIndex] == "+"
                    or userInput[operatorIndex] == '-'
                    or userInput[operatorIndex] == '*'
                    or userInput[operatorIndex] == '/'
                        or userInput[operatorIndex] == ' '):
                    errorMessage()
                else:
                    answer = float(first) / float(second)
                    print('result is:', answer, '\n')
            except ValueError:
                errorMessage()

        elif '+' in userInput:
            multi = int(userInput.index('+'))
            operatorIndex = multi+1
            first = userInput[:multi]
            second = userInput[multi+1:]
            try:
                if (userInput[operatorIndex] == "+"
                    or userInput[operatorIndex] == '-'
                    or userInput[operatorIndex] == '*'
                    or userInput[operatorIndex] == '/'
                        or userInput[operatorIndex] == ' '):
                    errorMessage()
                else:
                    answer = float(first) + float(second)
                    print('result is:', answer, '\n')
            except ValueError:
                errorMessage()

        elif '-' in userInput:
            multi = int(userInput.index('-'))
            operatorIndex = multi+1
            first = userInput[:multi]
            second = userInput[multi+1:]
            try:
                if (userInput[operatorIndex] == "+"
                    or userInput[operatorIndex] == '-'
                    or userInput[operatorIndex] == '*'
                    or userInput[operatorIndex] == '/'
                        or userInput[operatorIndex] == ' '):
                    errorMessage()
                else:
                    answer = float(first) - float(second)
                    print('result is:', answer, '\n')
            except ValueError:
                errorMessage()
        else:
            print("Calculation finished")


def errorMessage():
    print("Failed to calculate.")
    print("Input expression is invalid for expression.\n")


if __name__ == '__main__':
    Main()
