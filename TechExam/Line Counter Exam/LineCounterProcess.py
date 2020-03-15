import LineCounter
array_lines = []


def read_lines(file_name):
    """
        This is the main function for
        -reading lines
        -checking comments in the lines
        -blank lines and
        -the process lines
        arg : file_name : the name of the file to read
        return : blank_lines : the line with spaces
                comment_lines: the commented lines
                process_lines: the lines for process the coding
    """
    blank_line_count = 0
    comment_lines_count = 0
    process_lines_count = 0
    line_count = 0
    read_file = open(file_name, "r")
    for lines in read_file:
        lines = lines.replace('\n', '')
        lines = lines.replace(' ', '')
        lines = lines.replace('\t', '')
        line_count += 1
        array_lines.append(lines)
    index = 0
    while(index < len(array_lines)):
        if r'#' in array_lines[index]:
            cmt_line = array_lines[index]
            cmt_index = cmt_line.find(r'#')
            if cmt_index == 0:
                comment_lines_count += 1
            else:
                cmt_or_not = cmt_line[:cmt_index]
                if cmt_or_not.isspace():
                    comment_lines_count += 1
            index += 1

        elif array_lines[index] == '':
            blank_line_count += 1
            index += 1

        elif array_lines[index] == r'"""':
            sec_index = index + 1
            stay = True
            count = 0
            while(stay):
                if array_lines[sec_index] == r'"""':
                    comment_lines_count = comment_lines_count + count + 2
                    index = index + count + 2
                    stay = False
                else:
                    count += 1
                    sec_index += 1

        elif r'"""' in array_lines[index]:
            comment_lines_count += 1
            index += 1
        else:
            index += 1
    read_file.close()
    blank_lines = blank_line_count
    comment_lines = comment_lines_count
    process_lines = line_count - (blank_line_count + comment_lines_count)
    return blank_lines, comment_lines, process_lines
