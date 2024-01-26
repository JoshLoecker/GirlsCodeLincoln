# The following is pseudocode and is not meant to be run as a program.

Create a function named collatz() that has one parameter named number.
    Create a variable to determine if the input number is odd or even.

    Test if the variable is even, then:
        Create a variable to hold the result of number // 2.
        Print the result.
        Return the result.

    Test if the variable is odd, then:
        Create a variable to hold the result of 3 * number + 1.
        Print the result.
        Return the result.

user_input = input("Enter a number: ")

While "userinput.isnumeric()" is False:
    Collect user input again as the initial input was not correct

Convert the input to an integer


While user_input is not 1, then:
    Call the collatz() function with the user input as the argument.
