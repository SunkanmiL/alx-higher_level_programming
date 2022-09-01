#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    converts a Roman numeral to an integer
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    hashMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arr = [hashMap[key] for key in roman_string]
    num = arr[-1]
    for idx in range(len(arr)-1, 0, -1):
        if arr[idx] > arr[idx-1]:
            num -= arr[idx-1]
        else:
            num += arr[idx-1]
    return num
