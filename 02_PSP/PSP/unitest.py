import unittest
import PSPQuickSortInput
import PSPQuickSortProcess


class TestStringMethods(unittest.TestCase):

    def test_getArray_success_with_valid_values(self):
        """
            This is testing for normal files
        """

        # prepare
        fileName = "10Lines"
        expectedResult = [12.0, 13.5, 1.0, 5.5,
                          9.0, 19.5, 12.0, 23.5, 5.0, 51.0]

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertTrue(expectedResult, actuatlResponse)

    def test_getArray_error_with_not_existing_file(self):
        """
            This is test for Non Existing file
        """

        # prepare
        fileName = "10Lines1"

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertTrue(actuatlResponse)

    def test_getArray_error_with_empty_value(self):
        """
            This is for testing empty files
        """

        # prepare
        fileName = "empty"
        expectedResult = "\n The file is empty \n"

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertTrue(actuatlResponse)

    def test_getArray_error_inlude_strings(self):
        """
            This is for testing array including strings
        """

        # prepare
        fileName = "10ContStrings"
        expectedResult = "\n The Lines contain Strings \n"

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertTrue(actuatlResponse)

    def test_getArray_success_contain_blanks(self):
        """
            This is for testing blank lines
        """
        # prepare
        fileName = "10ContBlanks"
        expectedResult = [2.0, 3.4, 5.9, 6.5, 12.0, 13.0]

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertTrue(expectedResult, actuatlResponse)

    def test_sort_success_return_sortedArray(self):
        """
            This is the test for getting sortedArray
        """

        # prepare
        unsortedArray = [12.0, 13.5, 1.0, 5.5,
                         9.0, 19.5, 12.0, 23.5, 5.0, 51.0]
        expectedResult = [1.0, 5.0, 5.5, 9.0,
                          12.0, 12.0, 13.5, 19.5, 23.5, 51.0]

        # execute
        actuatlResponse = PSPQuickSortProcess.sort(unsortedArray)

        # assert
        self.assertEqual(expectedResult, actuatlResponse)


if __name__ == '__main__':
    unittest.main()
