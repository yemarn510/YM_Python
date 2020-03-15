import unittest
import Calender
import CalenderProcess
import CalenderOutput


class TestStringMethods(unittest.TestCase):

    def test_adding_schedule_success(self):
        """
            This is testing for adding schedule to the current
            schedule
        """

        # prepare
        date = ["2013-04-20", "2013-04-21", "2013-04-22"]
        title = ["MA for 2013-04", "Football", "Shopping"]
        detail = ["Time schedule is from 10:00 to 14:00",
                  "Plays football at Shin-Yokohama park.",
                  "Shopping with friends at Yokohama Station"]

        expected_date = ["2013-04-20", "2013-04-21",
                         "2013-04-22", "2019-10-31"]
        expected_title = ["MA for 2013-04", "Football",
                          "Shopping", "adding_title_for_2019_10_31"]
        expected_detail = ["Time schedule is from 10:00 to 14:00",
                           "Plays football at Shin-Yokohama park.",
                           "Shopping with friends at Yokohama Station",
                           "adding_detail_for_2019_10_31"]

        edit_date = "2019-10-31"
        edit_title = "adding_title_for_2019_10_31"
        edit_detail = "adding_detail_for_2019_10_31"

        # execute
        actual_date, actual_title, actual_detail = CalenderProcess.add(
            date, title, detail, edit_date, edit_title, edit_detail)

        # assert
        self.assertTrue(expected_date, actual_date)
        self.assertTrue(expected_title, actual_title)
        self.assertTrue(expected_detail, actual_detail)

    def testing_delete_function(self):
        """
            This is testing for deleting schedule from the current
            schedule
        """

        # prepare
        date = ["2013-04-20", "2013-04-21", "2013-04-22"]
        title = ["MA for 2013-04", "Football", "Shopping"]
        detail = ["Time schedule is from 10:00 to 14:00",
                  "Plays football at Shin-Yokohama park.",
                  "Shopping with friends at Yokohama Station"]

        expected_date = ["2013-04-20", "2013-04-21", '']
        expected_title = ["MA for 2013-04", "Football",
                          '']
        expected_detail = ["Time schedule is from 10:00 to 14:00",
                           "Plays football at Shin-Yokohama park.",
                           '']

        edit_date = "2013-04-22"
        edit_title = r"\delete"

        # execute
        actual_date, actual_title, actual_detail = CalenderProcess.delete(
            date, title, detail, edit_date, edit_title)

        # assert
        self.assertTrue(expected_date, actual_date)
        self.assertTrue(expected_title, actual_title)
        self.assertTrue(expected_detail, actual_detail)

    def testing_edit_success_with_editing_detail_and_title(self):
        """
            This is testing for editing schedule to the current
            existed schedule
        """

        # prepare
        date = ["2013-04-20", "2013-04-21", "2013-04-22"]
        title = ["MA for 2013-04", "Football", "Shopping"]
        detail = ["Time schedule is from 10:00 to 14:00",
                  "Plays football at Shin-Yokohama park.",
                  "Shopping with friends at Yokohama Station"]

        expected_date = ["2013-04-20", "2013-04-21",
                         "2013-04-22"]
        expected_title = ["MA for 2013-04", "Football",
                          "editing_title_2013_04_22"]
        expected_detail = ["Time schedule is from 10:00 to 14:00",
                           "Plays football at Shin-Yokohama park.",
                           "editing_detail_for_2013_04_22"]

        edit_date = "2013-04-22"
        edit_title = "editing_title_2013_04_22"
        edit_detail = "editing_detail_for_2013_04_22"

        # execute
        actual_date, actual_title, actual_detail = CalenderProcess.edit(
            date, title, detail, edit_date, edit_title, edit_detail)

        # assert
        self.assertTrue(expected_date, actual_date)
        self.assertTrue(expected_title, actual_title)
        self.assertTrue(expected_detail, actual_detail)

    def testing_new_user_inputtedd_date_with_delete_success(self):
        """
            This is testing for editing schedule to the current
            existed schedule
        """

        # prepare
        date = ["2013-04-20", "2013-04-21", "2013-04-22"]
        title = ["MA for 2013-04", "Football", "Shopping"]
        detail = ["Time schedule is from 10:00 to 14:00",
                  "Plays football at Shin-Yokohama park.",
                  "Shopping with friends at Yokohama Station"]

        expected_date = ["2013-04-20", "2013-04-21",
                         "2013-04-22"]
        expected_title = ["MA for 2013-04", "Football",
                          "editing_title_2013_04_22", '']
        expected_detail = ["Time schedule is from 10:00 to 14:00",
                           "Plays football at Shin-Yokohama park.",
                           '']

        edit_date = "2019-14-10"
        edit_title = r"\delete"

        # execute
        actual_date, actual_title, actual_detail = CalenderProcess.delete(
            date, title, detail, edit_date, edit_title)

        # assert
        self.assertTrue(expected_date, actual_date)
        self.assertTrue(expected_title, actual_title)
        self.assertTrue(expected_detail, actual_detail)


if __name__ == '__main__':
    unittest.main()
