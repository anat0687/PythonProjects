import re


def dateword(datestr):
    months = ["january", "feb", "mar", "apr", "may", "june",
              "july", "aug", "sep", "oct", "nov", "dec"]
    phoneNumRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    mo = phoneNumRegex.search(test_string)
    #print(mo.groups())
    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))
    if day > 31:
        print("not a valid date")
        return
    if month > 12:
        print("not a valid date")
        return
    monthword = months[month-1]
    print(monthword + mo.group(1) + mo.group(2))


test_string = input("please enter a date:\n")

dateword(test_string)