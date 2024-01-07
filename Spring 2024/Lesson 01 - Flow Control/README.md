# Control Flow

[Google Slides Link](https://docs.google.com/presentation/d/107A5EaseG4CJ8u-WYYzv9BwloNFcO5I8ZIZdcKmb5ts/edit?usp=sharing)

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

This lesson will introduce the concept of control flow in programming. Students will learn about Boolean values and
expressions, comparison operators, Boolean operators, and flow control statements. Students will also learn about the
importance of flow control in programming and how it can be used to create more complex programs. Finally, students will
learn about the importance of flow control in game development and how to use it to create a rock/paper/scissors game.

### Learning Objectives

- **Understand Fundamental Flow Control Concepts:** Understand basic concepts of flow control, including Boolean values,
  comparison operators, and Boolean operators.
  Be able to write expressions using these concepts and evaluate their truth value.
- **Exploring Control Flow Statements:** Explain the structure and function
  of `if`, `else`, `elif`, `while`, `for`, `break`, and `continue` statements for
  controlling program flow. Use these statements appropriately in code examples.
- **Implementing Control Flow in Game Development:** Apply control flow concepts to create a rock/paper/scissors game.

### Weekly Projects

#### Weekly Project #1: Explore Boolean Expressions

[Source Code](./explore_boolean_expressions.py)

What do the following expressions evaluate to? After you answer, type (or copy and paste) the expressions into a Python
interactive shell to check your answers.

```python
(5 > 4) and (3 == 5)

not (5 > 4)

(5 > 4) or (3 == 5)

not ((5 > 4) or (3 == 5))

(True and True) and (True == False)

(not False) or (not True)
```

#### Weekly Project #2: Rock/Paper/Scissors

[Source Code](./rock_paper_scissors.py)

- The user will input their choice (rock/paper/scissors).
- The computer will make a random choice (rock/paper/scissors).
- The programmer will test for each possible outcome.

