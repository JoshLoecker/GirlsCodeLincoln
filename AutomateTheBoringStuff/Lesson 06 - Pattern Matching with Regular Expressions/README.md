# Pattern Matching with Regular Expressions

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

Regular expressions, also known as regexes, are an extremely powerful tool for matching, searching, and manipulating
text. At their core, regular expressions allow you to describe patterns of text to search for, rather than having to
specify exact strings. This enables you to find and work with text in very flexible ways.

The `re` module in Python provides full regex support. To use regexes in your code, you first `import re`. You can then
call `re.compile()` and pass it a raw string representing the regex pattern you want to match. This returns a Regex
object. You can then call methods like `search()`, `findall()`, and `sub()` on the Regex object to perform matching and
substitution operations.

When writing the regex patterns, you use special metacharacters to match types of text. For example, `\d` matches
digits, `\w` matches word characters, and `\s` matches whitespace. You can use character classes like `[a-zA-Z0-9]` to
match specific sets of characters. The metacharacters `*` and `+` match repeated occurrences of patterns, while `?`
makes a pattern optional. Braces `{}` allow you to specify a specific number of matches.

The `re` module also provides options like `re.IGNORECASE` to make matching case-insensitive and `re.VERBOSE` to allow
writing regexes across multiple lines with comments. Groups and the `|` pipe character provide ways to match different
possible subpatterns.

Overall, mastering regular expressions in Python enables you to concisely describe text patterns you want to work with
and perform complex search, match, and replace operations with just a few lines of code. Regexes are invaluable for
cleaning and parsing text-based data.

## Learning Objectives
- **Introduction to Regular Expressions:** Define regular expressions and understand their role in text pattern
  searching. Differentiate between traditional text search methods (e.g., CTRL-F) and the advanced capabilities offered
  by regular expressions.
- **Recognizing Text Patterns:** Identify common text patterns in various contexts, such as phone numbers, email
  addresses, social security numbers, URLs, and hashtags. Understand how regular expressions can be used to describe and
  search for these patterns efficiently.
- **Mastering Basic Regular Expression Features:** Learn the basics of matching with regular expressions, including
  specifying character patterns. Explore the power of regular expressions in simplifying code for finding text patterns.
- **Advanced Regular Expression Techniques:** Understand advanced features of regular expressions, such as string
  substitution and creating custom character classes. Apply regular expressions to perform complex text processing tasks
  efficiently.

## Weekly Projects

### Weekly Project #1: Date Detection

Write a regular expression that can detect dates in the `DD/MM/YYYY` format. Assume that the days range from 01 to 31,
the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit,
it’ll have a leading zero (i.e., `01`, `02`, `03`, etc).

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent
dates like `31/02/2020` or `31/04/2021`. Then store these strings into variables named `month`, `day`, and `year`, and
write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February
has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year
evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note
how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

### Weekly Project #2: Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and
has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

### Weekly Project #3: Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the `strip()` string method. If no other arguments are
passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

