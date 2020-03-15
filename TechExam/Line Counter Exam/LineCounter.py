import LineCounterInput
import LineCounterProcess
import LineCounterOutput


def Main():
    """
        This is the main function for reading the python codes inside it
        and print according to the lines
    """
    file_name = LineCounterInput.read_file()
    if file_name != "Nothing":
        blank_lines, comment_lines, process_lines = LineCounterProcess.\
            read_lines(file_name)
        LineCounterOutput.output_message(
            blank_lines, comment_lines, process_lines)


if __name__ == "__main__":
    Main()
