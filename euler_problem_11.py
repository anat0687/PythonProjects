
text = open("C:\\Users\\Andrew\\Documents\\euler_number_grid.txt", "r")

numgrid = []

def strconv(string):
    li = list(string.split(" "))
    for m in range(20):
        li[m] = int(li[m])
    return(li)


for i in range(20):
    numgrid.append(strconv(text.readline().rstrip()))

print(numgrid)
