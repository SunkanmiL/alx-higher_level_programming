#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        elif i == j:
            continue
        else:
            print("{}{}".format(i, j), end=", ")
