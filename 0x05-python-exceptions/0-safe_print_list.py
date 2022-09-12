#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements of a list
    Returns the amount of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except:
            continue
    print("")
    return count
