import re

def isdate(string):

    if len(string) != 10:
        return False
    if (string[2] or string[5]) != '/':
        return False
    else:
        return True


test_string = input("please enter a date:\n")

print(isdate(test_string))