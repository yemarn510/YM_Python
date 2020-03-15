"""
    This class is for showing the schedule, exporting the schedule
    and print menu.
"""

import csv
import Calender
output_file_name = 'export.csv'


def schedule_export(date, title, detail):
    """
        This function is for exporting to the excel file with
        args : Date : Array
             : Title : Array
             : Detail : Array
    """
    with open(output_file_name, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Title', 'Detail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for index_two in range(0, len(date), 1):
            if title[index_two] == '' or detail[index_two] == '':
                pass
            else:
                writer.writerow({'Date': date[index_two],
                                 'Title': title[index_two],
                                 'Detail': detail[index_two]})
        print("\nExport all schedules successfully.\n")


def show_schedule(date, title, detail):
    """
        This function is for showing schedules
        args : Date : Array
             : Title : Array
             : Detail : Array
    """
    for index in range(0, len(date), 1):
        if date[index] == '' or title[index] == '' or detail[index] == '':
            pass
        else:
            print("  --------------------------")
            print("  [Date]", date[index])
            print("  [Title]", title[index])
            print("  [Detail]", detail[index])
    print("  --------------------------")


def print_menu():
    """
        This function is for reducing redundant print lines
        return : user_input : string
    """
    print("\nPlease input exist number or “q” or “Q” \n")
    print("=============================\n")
    print("Start Calender Application")
    print("1: Show Schedule")
    print("2: Edit Schedule")
    print("3: Schedule Export")
    print("q: quit\n")
    user_input = input("Select menu: ")
    print()
    return user_input
