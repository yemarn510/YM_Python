asd = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]

for x in asd:
    print(asd)
    if x == 7 in asd:
        asd.pop(x-1)

    print(asd)
