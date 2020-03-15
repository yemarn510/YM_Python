first = int(input("P1 : "))
sec = int(input("P2 : "))

if first-sec == 1:
    print("P2 is a winner")
elif first-sec == 2:
    print("P1 is a winner")
elif first-sec == -1:
    print("P1 is a winner")
elif first-sec == -2:
    print("P2 is a winner")
else:
    print("Even")
