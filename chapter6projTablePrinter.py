def printTable(tableData):
    colWidths = [0] * len(tableData)
    
    for i in range(0, len(tableData)):
        for y in tableData[i]:
            if len(y) > colWidths[i]:
                colWidths[i] = len(y)
                
    colWidths.sort()
    widestWidth = colWidths[-1]
    
    for i in range(0, len(tableData[0])):
        for y in range(0, len(tableData)):
            print(tableData[y][i].rjust(widestWidth), end='')
            if y == len(tableData) - 1: print('')
            
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)