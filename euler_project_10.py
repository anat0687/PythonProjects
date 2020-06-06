from math import ceil

def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
        if i == int(n/2):
            return True

def psieve(lim):
    numlist = list(range(1, lim+1))
    numlist[0] = 0
    for i in range(1, ceil(lim**0.5)):
        if isprime(i):
            for k in range(1, lim+1):
                if k > i and k % i == 0:
                    numlist[k-1] = 0
    return numlist


print(sum(psieve(2000000)))

