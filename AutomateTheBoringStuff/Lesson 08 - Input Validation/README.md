# Input Validation

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

This lesson will introduce the concept of input validation in programming. Students will learn about the importance of
input validation in preventing nonsensical or incorrect user inputs. Students will also learn how to implement basic
input validation code using a while loop. Finally, students will learn about the challenges of manual input validation
and how to use try and except statements to make their programs more robust.

## Learning Objectives
- **Understanding the Importance of Input Validation:** Recognize the significance of input validation in preventing
  nonsensical or incorrect user inputs. Understand how input validation contributes to code robustness, bug prevention,
  and security.
- **Implementing Basic Input Validation Code:** Learn the fundamentals of input validation through a basic example using
  a while loop. Understand the key components of input validation code, such as type conversion, exception handling, and
  conditional statements.
- **Exploring Challenges with Manual Input Validation:** Identify potential challenges and drawbacks of manually
  implementing input validation for every input() call in a program. Understand the limitations and the risk of
  overlooking certain cases in manual input validation.

## Weekly Projects

### Weekly Project #1: Sandwich Maker

Write a program that asks users for their sandwich preferences. The program should use `PyInputPlus` to ensure that they
enter valid input, such as:

Using `inputMenu()` for a bread type: wheat, white, or sourdough.
Using `inputMenu()` for a protein type: chicken, turkey, ham, or tofu.
Using `inputYesNo()` to ask if they want cheese.
If so, using `inputMenu()` to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using `inputYesNo()` to ask if they want mayo, mustard, lettuce, or tomato.
Using `inputInt()` to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their
selection.

### Weekly Project #2: Multiplication Quiz

PyInputPlus’s features can be useful for creating a timed multiplication quiz. By setting the `allowRegexes`,
`blockRegexes`, `timeout`, and `limit` keyword argument to `pyip.inputStr()`, you can leave most of the implementation
to PyInputPlus. The less code you need to write, the faster you can write your programs. Let’s create a program that
poses 10 multiplication problems to the user, where the valid input is the problem’s correct answer. Open a new file
editor tab and save the file as `multiplicationQuiz.py`.

First, we’ll import `pyinputplus`, `random`, and `time`. We’ll keep track of how many questions the program asks and how
many correct answers the user gives with the variables numberOfQuestions and correctAnswers. A `for` loop will
repeatedly pose a random multiplication problem 10 times:

```python

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
```

> Inside the for loop, the program will pick two single-digit numbers to multiply. We’ll use these numbers to create
> a `#Q: N × N =` prompt for the user, where `Q` is the question number (1 to 10) and `N` are the two numbers to
> multiply.

```python
    # Pick two random numbers:
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
```

The `pyip.inputStr()` function will handle most of the features of this quiz program. The argument we pass for
`allowRegexes` is a list with the regex string `'^%s$'`, where `%s` is replaced with the correct answer. The `^` and `%`
characters ensure that the answer begins and ends with the correct number, though PyInputPlus trims any whitespace from
the start and end of the user’s response first just in case they inadvertently pressed the spacebar before or after
their answer. The argument we pass for `blocklistRegexes` is a list with `('.*', 'Incorrect!')`. The first string in the
tuple is a regex that matches every possible string. Therefore, if the user response doesn’t match the correct answer,
the program will reject any other answer they provide. In that case, the `'Incorrect!'` string is displayed and the user
is prompted to answer again. Additionally, passing `8` for `timeout` and `3` for `limit` will ensure that the user only
has 8 seconds and 3 tries to provide a correct answer:

> If the user answers after the 8-second timeout has expired, even if they answer correctly, `pyip.inputStr()` raises a
`TimeoutException` exception. If the user answers incorrectly more than 3 times, it raises a `RetryLimitException`
> exception. Both of these exception types are in the `PyInputPlus` module, so `pyip.` needs to prepend them:

> Remember that, just like how else blocks can follow an if or elif block, they can optionally follow the last except
> block. The code inside the following else block will run if no exception was raised in the try block. In our case,
> that means the code runs if the user entered the correct answer:

```python
try:
    # Right answers are handled by allowRegexes.
    # Wrong answers are handled by blockRegexes, with a custom message.
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                  blockRegexes=[('.*', 'Incorrect!')],
                  timeout=8, limit=3)
except pyip.TimeoutException:
    print('Out of time!')
except pyip.RetryLimitException:
    print('Out of tries!')
else:
    # This block runs if no exceptions were raised in the try block.
    print('Correct!')
    correctAnswers += 1
```

> No matter which of the three messages, “Out of time!”, “Out of tries!”, or “Correct!”, displays, let’s place a
> 1-second pause at the end of the for loop to give the user time to read it. After the program has asked 10 questions
> and the for loop continues, let’s show the user how many correct answers they made:

```python
    time.sleep(1.5)  # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
```

PyInputPlus is flexible enough that you can use it in a wide variety of programs that take keyboard input from the user,
as demonstrated by the programs in this chapter.

### Weekly Project #3: Multiplication Quiz

To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without
importing it. This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll
need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the
correct answer after the 8-second limit.

