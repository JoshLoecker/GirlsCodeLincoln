# Debugging

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

### Lesson Summary

This lesson will introduce the concept of debugging in programming. Students will learn about the importance of
debugging in preventing bugs and how to use the `logging` module to log error messages to a file. Students will also
learn about the importance of assertions in preventing bugs and how to use the `assert` statement to check for
conditions. Finally, students will learn about the importance of exceptions in preventing bugs and how to use the
`try` and `except` statements to handle exceptions.

### Learning Objectives
- **Understanding the Prevalence of Bugs in Programming:** Recognize that writing code and debugging are integral parts
  of programming. Understand that bugs are common even among professional programmers and are a natural aspect of
  coding.
- **Introduction to Debugging Tools and Techniques:** Learn about various tools and techniques for debugging programs
  effectively. Understand the importance of early bug detection in the debugging process.
- **Exploring Logging and Assertions:** Explore the use of logging and assertions as tools to identify and catch bugs
  early in the program. Understand the concept of assertions as "sanity checks" for necessary conditions and their role
  in failing fast.
- **Comparing Assertions, Exceptions, and Logging:** Understand the differences between assertions, exceptions, and
  logging in the context of bug detection and prevention. Learn when to use each tool based on the nature of the error
  and the program's recovery possibilities.
