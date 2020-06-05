from math import ceil


test_num = 12


def get_divs(num):
    for i in range(1, ceil(num/2)+1):
        if num % i == 0:
            yield i


def sum_divs(num):
    divsum = 0
    for value in get_divs(num):
        divsum = divsum + value
    return divsum


facsums = []
for j in range(test_num):
    jsum = sum_divs(j)
    facsums.append(jsum)


kdex = 0
amipairs = []
for k in facsums:
    kdex += 1
    indices = [i for i, x in enumerate(facsums) if x == kdex]
    if kdex in indices:
        amipairs.append([kdex, indices.index(kdex)])

print(amipairs)

amisum = 0
for n in range(len(amipairs)):
    amisum += sum(amipairs[n])

print(amisum)


