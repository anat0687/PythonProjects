text = open("C:\\Users\\Andrew\\Documents\\large_sum.txt", "r")


def strconv(string):
    li = list(string.split(" "))
    for m in range(20):
        li[m] = int(li[m])
    return li


numlist = []
for i in range(100):
    numlist.append(int(text.readline().rstrip()))


print(sum(numlist))