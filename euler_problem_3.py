
from math import floor


test_num = 51475143
mods = test_num

factors = []

i = 2

while i < floor(mods):
    if test_num % i == 0:
        mods = test_num
        test_num = test_num / i
        factors.append(i)
        i = 1
    i += 1


print(factors)

