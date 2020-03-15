"""
    This is the main class for viewng, adding, editing and deleting schedules.
"""

import CalenderProcess
import CalenderOutput
sec_index = 2


def Main():
    """
        This function is the Main Function of the program
        args : Date, Title, Detail Arrays
    """
    date = ["2013-04-20", "2013-04-21", "2013-04-22"]
    title = ["MA for 2013-04", "Football", "Shopping"]
    detail = ["Time schedule is from 10:00 to 14:00",
              "Plays football at Shin-Yokohama park.",
              "Shopping with friends at Yokohama Station"]
    valid_inputs = ['1', '2', '3', 'q', 'Q']
    stay = True
    toggle = True
    print("Start Calender Application\n")
    while stay:
        print("=====================")
        print("1: Show Schedule")
        print("2: Edit Schedule")
        print("3: Schedule Export")
        print("q: quit")
        print("=====================")
        if toggle is True:
            user_input = input("Select menu: ")
        else:
            user_input = user_input
            toggle = True
        if user_input in valid_inputs:
            if user_input == valid_inputs[0]:
                # show schedule
                CalenderOutput.show_schedule(date, title, detail)
            elif user_input == valid_inputs[1]:
                # edit schedule
                CalenderProcess.execute(date, title, detail)
            elif user_input == valid_inputs[sec_index]:
                # Schedule report
                CalenderOutput.schedule_export(date, title, detail)
            elif user_input == 'q' or user_input == 'Q':
                # quit
                print("\n(Terminate Clander Application)\n")
                stay = False
            else:
                print("No Operation")
        else:
            toggle = False
            user_input = CalenderOutput.print_menu()
        while user_input not in valid_inputs:
            user_input = CalenderOutput.print_menu()


if __name__ == "__main__":
    Main()
