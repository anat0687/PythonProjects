
prev = 1
now = 1
next = 0

fibsum = 0

while next < 4000000:
    next = now + prev
    if next % 2 == 0:
        fibsum += next
    prev = now
    now = next


print(fibsum)
