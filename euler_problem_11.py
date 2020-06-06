
text = open("C:\\Users\\Andrew\\Documents\\euler_number_grid.txt", "r")


def strconv(string):
    li = list(string.split(" "))
    for m in range(20):
        li[m] = int(li[m])
    return li


upmax = 0
rightmax = 0
drightmax = 0
dleftmax = 0

up = 0
right = 0
dright = 0
dleft = 0

numgrid = []
for i in range(20):
    numgrid.append(strconv(text.readline().rstrip()))

for row in range(20):
    for col in range(20):
        try:
            up = numgrid[row][col] * numgrid[row-1][col] * numgrid[row-2][col] * numgrid[row-3][col]
        except IndexError:
            up = 0
        try:
            right = numgrid[row][col] * numgrid[row][col+1] * numgrid[row][col+2] * numgrid[row][col+3]
        except IndexError:
            right = 0
        try:
            dright = numgrid[row][col] * numgrid[row+1][col+1] * numgrid[row+2][col+2] * numgrid[row+3][col+3]
        except IndexError:
            dright = 0
        try:
            dleft = numgrid[row][col] * numgrid[row+1][col-1] * numgrid[row+2][col-2] * numgrid[row+3][col-3]
        except IndexError:
            dleft = 0

        if up > upmax:
            upmax = up
        if right > rightmax:
            rightmax = right
        if dright > drightmax:
            drightmax = dright
        if dleft > dleftmax:
            dleftmax = dleft


print(max(upmax, rightmax, dleftmax, drightmax))

