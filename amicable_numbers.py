from math import ceil


test_num = 9999


def get_divs(num):
    for i in range(0, ceil(num/2)+1):
        if i == 0:
            yield i
        elif num % i == 0:
            yield i


def sum_divs(num):
    divsum = 0
    if num == 1:
        return divsum
    else:
        for value in get_divs(num):
            divsum = divsum + value
        return divsum


facsums = []
for j in range(test_num):
    jsum = sum_divs(j)
    facsums.append(jsum)

print(facsums)

amisum = 0
for k in range(test_num):
    for n in range(k+1, test_num):
        if facsums[k] == n and facsums[n] == k:
            print(n, k)
            amisum += n + k


print(amisum)


