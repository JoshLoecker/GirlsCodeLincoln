# Functions

## Getting Started

### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install Poetry, run the following
command:

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Once Poetry is installed, you can install the project dependencies by running the following command:

```shell
poetry install
```

## Lesson Summary

This lesson will introduce the concept of functions in programming. Students will learn about built-in functions and how
to create their own custom functions. Students will also learn about the importance of functions in organizing code and
making it more resilient. Finally, students will learn about the importance of error handling in programming and how to
use try and except statements to make their programs more robust.

## Learning Objectives

- **Understanding Built-in Functions:** Students will be able to identify and use common built-in functions in Python,
  such as print(), input(), and len(),
  and comprehend their basic functionalities.
- **Creating Custom Functions:** Participants will gain the ability to write their own functions in Python, recognizing
  functions as a means of
  compartmentalizing code into logical groups, and understand the concept of local scopes within functions.
- **Organizing Code with Functions:** Learners will appreciate the role of functions in organizing code, viewing them as
  black boxes with inputs (
  parameters) and outputs (return values), and realizing how functions contribute to code modularity.
- **Enhancing Code Resilience with try and except Statements:** Students will be able to describe and implement try and
  except statements in Python, understanding their role in
  handling errors and making programs more robust by allowing code execution even in the presence of detected errors.

## Weekly Projects

### Weekly Project #1: The Collatz Sequence

Write a function named collatz() that has one parameter named `number`. If number is even, then collatz() should print
`number // 2` and return this value. If number is odd, then `collatz()` should print and return `3 * number + 1`.

Then write a program that lets the user type in an integer and that keeps calling `collatz()` on that number until the
function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using
this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the
Collatz sequence, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from `input()` to an integer with the `int()` function; otherwise, it will be a
string value.

Hint: An integer number is even if `number % 2 == 0`, and it’s odd if `number % 2 == 1`.

The output of this program could look something like this:

```
Enter number:
3
10
5
16
8
4
2
1
```

### Weekly Project #2: Input Validation

Use a `while` loop to force the user to enter a number. Calling `.isnumeric()` on the variable used to hold the user's
input can be used to determine if the input is a number or not Normally, the `int()` function will raise a ValueError
error if it is passed a noninteger string, as in `int('puppy')`. In the except clause, print a message to the user
saying they must enter an integer.

