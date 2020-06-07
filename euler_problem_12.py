

def triangle_num(num):
    tnum = sum(range(num+1))
    return tnum


def getdivs(n):
    divs = []
    for j in range(1, n+1):
        if n % j == 0:
            divs.append(j)

    return divs



# for i in range(1, 8):
# #    print(triangle_num (i))
#     print(getdivs(triangle_num(i)))

i = 1

while len(getdivs(triangle_num(i))) < 501:
    i += 1

print(triangle_num(i))
print(len(getdivs(triangle_num(i))))

