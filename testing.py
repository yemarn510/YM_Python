array = []


def main():
    f = open("testing.txt", "r")
    fl = f.readlines()
    for x in fl:
        array.append(x)
    print(array)
    if '\n' in array:
        array.remove('\n')
    if '\t\n' in array:
        array.remove('\t\n')
    print(array)
    f.close()


if __name__ == "__main__":
    main()
