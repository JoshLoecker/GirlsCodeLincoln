# The following is pseudocode and is not meant to be run as a program

Create a function called "join_list" that has an argument called "input_list"
    If the input_list is empty (use `if not input_list`):
        Return an empty string

    Create a variable called "output_string" and set it to an empty string
    If the length of the input_list is 1:
        Set output_string to the first item in the input_list
    Else if the length of the input_list is 2:
        Set output_string to the first item in the input_list + " and " + the second item in the input_list
    Else:
        Loop through the input_list
            If the current index is the last index in the input_list:
                Add "and " + the current item to the output_string
            Else:
                Add the current item + ", " to the output_string

    Return the output_string

# Use the following code to test your function:
print(join_list([]))
print(join_list(['apples']))
print(join_list(['apples', 'bananas']))
print(join_list(['apples', 'bananas', 'tofu']))
print(join_list(['apples', 'bananas', 'tofu', 'cats']))
