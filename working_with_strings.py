def printTable(data):
    count = 0
    for i in data:
        for j in i:
            if len(j) > count:
                count = len(j)
            print(j)
    print(count)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)