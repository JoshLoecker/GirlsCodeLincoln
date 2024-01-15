def printTable(tableData):
    colWidths = 0
    for i, table in enumerate(tableData):
        for word in table:
            if len(word) > colWidths:
                colWidths = len(word)
    
    for i, table in enumerate(tableData):
        for j, word in enumerate(table):
            print(word.rjust(colWidths), end=' ')
        print()


data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

printTable(data)
