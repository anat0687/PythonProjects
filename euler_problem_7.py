

def isprime(n):
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
        if i == int(n/2):
            return True


count = 2
num = 4
while count < 6:
    if isprime(num):
        count += 1
        lastprime = num
        num += 1
    else:
        num += 1


print(lastprime)
