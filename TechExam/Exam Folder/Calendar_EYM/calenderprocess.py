"""
    This Class is for Processing the editing data, Adding new Schedule,
    and Deleting the existed data.
"""

import Calender


def execute(date, title, detail):
    """
        This function is for adding, deleting and editing to and from the
        current schedule
        args : Date : Array
             : Title : Array
             : Detail : Array
    """
    print()
    print("Edit Schedule.")
    edit_date = input("Input date for registration: ")
    edit_title = input("Input title: ")

    # delete
    if edit_date in date and edit_title == r'\delete':
        date, title, detail = delete(
            date, title, detail, edit_date, edit_title)

    # add
    elif edit_date not in date:
        if edit_title == r'\delete':
            date, title, detail = delete(
                date, title, detail, edit_date, edit_title)
        else:
            edit_detail = input("Input detail: ")
            date, title, detail = add(
                date, title, detail, edit_date, edit_title, edit_detail)

    # edit
    else:
        edit_detail = input("Input detail: ")
        date, title, detail = edit(
            date, title, detail, edit_date, edit_title, edit_detail)


def edit(date, title, detail, edit_date, edit_title, edit_detail):
    """
        This function is for editing the current existed schedule
        args : date : Array
             : title : Array
             : detail : Array
             : edit_date : user inputted date
             : edit_title : user inputted title
             : edit_detail : usere inputted detail
        return : date : Array
               : title : Array
               : detail : Array
    """
    if edit_date in date:
        date_index = date.index(edit_date)
        date[date_index] = edit_date
        title[date_index] = edit_title
        detail[date_index] = edit_detail
        print("  -----------------------------")
        print("  [Date]", edit_date)
        print("  [Title]", title[date_index])
        print("  [Detail]", detail[date_index])
        print("  -----------------------------")
    return date, title, detail


def delete(date, title, detail, edit_date, edit_title):
    """
        This function is for deleting the current existed schedule
        args : date : Array
             : title : Array
             : detail : Array
             : edit_date : user inputted date
             : edit_title : user inputted title
             : edit_detail : usere inputted detail
        return : date : Array
               : title : Array
               : detail : Array
    """
    if edit_date in date:
        date_index = date.index(edit_date)
        if edit_title == r'\delete':
            if title[date_index] == '':
                print("\n There is no schedule to be deleted ")
            else:
                title[date_index] = ''
                detail[date_index] = ''
                print("\n Selected Schedule is deleted successfully.")
    else:
        if edit_title == r'\delete':
            print("\n There is no schedule to be deleted \n")
    return date, title, detail


def add(date, title, detail, edit_date, edit_title, edit_detail):
    """
        This function is for adding the schedule to the existed schedule
        args : date : Array
             : title : Array
             : detail : Array
             : edit_date : user inputted date
             : edit_title : user inputted title
             : edit_detail : usere inputted detail
        return : date : Array
               : title : Array
               : detail : Array
    """
    date.append(edit_date)
    title.append(edit_title)
    detail.append(edit_detail)
    print("========================")
    return date, title, detail


if __name__ == "__main__":
    execute(date, title, detail)
