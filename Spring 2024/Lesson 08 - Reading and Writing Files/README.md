# Reading and Writing Files

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

This lesson will introduce the concept of file handling in programming. Students will learn about the syntax for opening
and reading files and how to use common file methods, such as `read()` and `readlines()`. Students will also learn about
the differences between plaintext and binary files and how to use the `write()` and `append()` methods to write to
files. Finally, students will learn about the importance of file organization in programming and how to use the `os`
module to automate file copying, renaming, moving, and compressing.

### Learning Objectives
- **Understanding File Organization:** Recognize the organizational structure of files into folders or directories.
  Understand the concept of file paths as descriptors of a file's location.
- **Exploring the Concept of Current Working Directory:** Understand the significance of the current working directory
  in file operations. Learn how specifying file paths relative to the current working directory can simplify file
  manipulation.
- **Direct Interaction with Text Files:** Learn how to use the open() function to directly interact with the contents of
  text files. Understand the read() and readlines() methods for reading the entire content or lines from a text file.
- **Writing and Appending to Text Files:** Explore the capabilities of the open() function in write and append modes for
  creating new text files or adding to existing ones. Understand how to write and append data to text files
  programmatically.
