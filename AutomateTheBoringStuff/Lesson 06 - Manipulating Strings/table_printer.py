# The following is pseudocode and is not meant to be run

Create a function called printTable
    Create a variable called colWidths and set it to 0
    Use a for loop to iterate through each table in tableData
        Use a for loop to iterate through each word in table
            If the length of the word is greater than colWidths
                Set colWidths to the length of the word

    Use a for loop to iterate through each table in tableData
        Use a for loop to iterate through each word in table
            Print the word right justified by colWidths
        Print a newline


# Use the following table for testing
data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


Call the printTable function and pass it the data variable
