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
    for i in range(1,ceil(lim/2)):



psum = 0

for k in range(1, 10):
    if isprime(k):
        print(k, 'is prime')
        psum += k

print(psum)

