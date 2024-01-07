# Keeping Time, Scheduling Tasks, and Launching Programs

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

This lesson will introduce the concept of time in programming. Students will learn about the importance of time in
scheduling tasks and how to use the `time` and `datetime` modules to keep track of time. Students will also learn about
the importance of time in scheduling tasks and how to use the `time` and `datetime` modules to schedule tasks. Finally,
students will learn about the importance of time in scheduling tasks and how to use the `time` and `datetime` modules to
launch programs.

### Learning Objectives
- **Scheduling and Automation with Time Modules:** Understand the role of Python's time and datetime modules in
  scheduling programs to run at specific times or intervals. Learn to utilize time.time() for obtaining epoch timestamps
  and datetime for performing date arithmetic, formatting, and parsing with date information.
- **Automating Program Execution:** Explore the time.sleep() function and its role in adding pauses to a program,
  especially when scheduling tasks. Discover methods to schedule programs for automatic execution, leveraging the
  scheduler provided by the operating system.
- **Multithreading and Concurrent Execution:** Learn about the threading module and its use in creating multiple threads
  for concurrent execution of tasks, such as downloading multiple files simultaneously. Understand the importance of
  ensuring threads read and write only local variables to avoid potential concurrency issues.
