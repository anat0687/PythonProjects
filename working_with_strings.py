def printtable(data):
    width = 0
    tjust = []
    row = 0
    for i in data:
        i.sort()
        for j in i:
            if len(j) > width:
                width = len(j)
    for i in data:
        rowjust = []
        for j in i:
            jjj = j.rjust((width+2))
            rowjust.append(jjj)
        tjust.append(rowjust)
        row += 1

    rez = [[tjust[j][i] for j in range (len (tjust))] for i in range (len (tjust[0]))]
    print("\n")
    for row in rez:
        print("".join(row))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printtable(tableData)

