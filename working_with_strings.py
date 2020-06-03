def printtable(data):
    width = 0
    tjust = []
    row = 0
    for i in data:
        for j in i:
            if len(j) > width:
                width = len(j)
    for i in data:
        col = 0
        rowjust = []
        for j in i:
            jjj = j.rjust((width+3))
            # print(jjj)
            rowjust.append(jjj)
            col += 1
        tjust.append(rowjust)
        row += 1
    for i in tjust:
        print(i)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printtable(tableData)

