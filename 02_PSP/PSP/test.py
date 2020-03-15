import unittest
import PSPQuickSortInput
import PSPQuickSortProcess


class TestStringMethods(unittest.TestCase):

    def test_getArray(self):
        """This is test smaple
        """

        # prepare
        fileName = "10Lines"
        expectedResult = [12.0, 13.5, 1.0, 5.5,
                          9.0, 19.5, 12.0, 23.5, 5.0, 51.0]

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertEqual(expectedResult, actuatlResponse)

    def test_getArray_error_with_not_existing_file(self):
        """This is test smaple
        """

        # prepare
        fileName = "10Lines1"

        # execute
        actuatlResponse = PSPQuickSortInput.getArray(fileName)

        # assert
        self.assertFalse(actuatlResponse)

    def test_return_sortedarray(self):
        '''
            This is for checking if the array sorted properly
        '''

        # prepare


if __name__ == '__main__':
    unittest.main()
