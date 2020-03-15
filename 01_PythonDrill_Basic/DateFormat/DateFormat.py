"""
    This calss is for showing different types of dateformats after the user
    inputted the number of days he/she wants to know from today.
"""

import argparse
import time
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def Main():
    """
        this accept the int number and sort out the days, months and year
        according to the user input.
        The user can also input the negative numbers.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int,
                        help="display a square of a given number")
    userInputDate = (parser.parse_args()).n

    try:
        modifiedDate = (date.today() + timedelta(days=userInputDate))
        currentTime = datetime.now()
        if(userInputDate > 0):
            print(str(userInputDate) + " days later:")

        else:
            print(str(abs(userInputDate)) + " days before:")

        print(modifiedDate.strftime("%Y/%m/%d"))
        print(modifiedDate.strftime("%a, %b%d, '%y"))
        print(modifiedDate.strftime("%Y.%b.%d" + " AD " +
                                    currentTime.strftime("%I:%M:%S %p")))
    except:
        print("Data Overflow")


if __name__ == "__main__":
    Main()
