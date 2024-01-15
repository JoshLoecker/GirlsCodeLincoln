# Manipulating Strings

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

This lesson will introduce the concept of strings in programming. Students will learn about the syntax for creating
strings and how to use common string methods, such as `upper()`, `lower()`, and `isupper()`. Students will also learn
about the differences between string and list data types and how to use slicing to extract substrings from strings.
Finally, students will learn about the importance of input validation in programming and how to use regular expressions
to ensure that user inputs are valid.

## Learning Objectives
- **Explore Advanced String Manipulation:** Learn techniques beyond simple string concatenation, including extracting
  partial strings, manipulating spacing, and converting cases. Understand how to utilize Python string methods to
  perform various text-processing tasks.
- **Implement Clipboard Automation:** Develop the ability to access the clipboard using Python code. Create a simple
  clipboard program that can store and manage multiple strings of text.
- **Automate Text Formatting:** Work through programming projects involving the automation of text formatting tasks.
  Apply string manipulation techniques to streamline the process of handling and formatting pieces of text efficiently.
- **Understand the Power of Text-Based Programs:** Recognize the effectiveness of text-based programs in manipulating
  large amounts of data quickly. Explore the advantages of working with text-based programs for tasks that may not
  involve graphical user interfaces or flashy visuals.

## Weekly Projects

### Weekly Project #1: Table Printer

Write a function named `printTable()` that takes a list of lists of strings and displays it in a well-organized table
with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example,
the value could look like this:

```python
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
```

Your `printTable()` function would print the following:

```
apples Alice dogs
oranges Bob cats
cherries Carol moose
banana David goose
```

Hint: your code will first have to find the longest string in each of the inner lists so that the whole column can be
wide enough to fit all the strings. You can store the maximum width of each column as a list of integers. The
`printTable()` function can begin with `colWidths = [0] * len(tableData)`, which will create a list containing the same
number of 0 values as the number of inner lists in `tableData`. That way, `colWidths[0]` can store the width of the
longest string in `tableData[0]`, `colWidths[1]` can store the width of the longest string in `tableData[1]`, and so on.
You can then find the largest value in the `colWidths` list to find out what integer width to pass to the `rjust()`
string method.


