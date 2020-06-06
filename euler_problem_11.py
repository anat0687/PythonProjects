
text = open("C:\\Users\\Andrew\\Documents\\euler_number_grid.txt", "r")


def strconv(string):
    li = list(string.split(" "))
    for m in range(20):
        li[m] = int(li[m])
    return li


numgrid = []
for i in range(20):
    numgrid.append(strconv(text.readline().rstrip()))

for row in range(20):
    for col in range(20):
        try:
            up = numgrid[row][col] * numgrid[row-1][col] * numgrid[row-2][col] * numgrid[row-3][col]
        except IndexError:
            up = None
        try:
            right = numgrid[row][col] * numgrid[row][col+1] * numgrid[row][col+2] * numgrid[row][col+3]
        except IndexError:
            right = None
        try:
            dright = numgrid[row][col] * numgrid[row+1][col+1] * numgrid[row+2][col+2] * numgrid[row+3][col+3]
        except IndexError:
            dright = None
        try:
            dleft = numgrid[row][col] * numgrid[row+1][col-1] * numgrid[row+2][col-2] * numgrid[row+3][col-3]
        except IndexError:
            dleft = None


print(right)
print(up)
print(dleft)
print(dright)