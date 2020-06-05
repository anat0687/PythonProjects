

test_num = 600851475143
mods = test_num
factors = []
i = 2


while i <= mods:
    if test_num % i == 0:
        test_num = test_num / i
        mods = test_num
        factors.append(i)
        i = 1
    i += 1


print(max(factors))

