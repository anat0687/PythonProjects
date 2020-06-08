


def makeseq(num):
    count = 0
    n = num
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            count += 1
        else:
            n = int(3*n + 1)
            count += 1
    return count

maxlen = 0
maxi = 0

for i in range(2, 1000000):
    temp = makeseq(i)
    if temp > maxlen:
        maxlen = makeseq(i)
        maxi = i


print(maxi, maxlen)

