#!/usr/bin/python3
if __name__ == "__main__":
    """
    Program prints the results of the addition of all arguments
    """
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0")
    elif count == 1:
        print("{}".format(sys.argv[1]))
    else:
        print("{}".format(sum([int(i) for i in sys.argv[1:]])))
