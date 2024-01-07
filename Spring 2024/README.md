# Python Programming for Automation

Written for the Spring 2024 semester by Josh Loecker

# Table of Contents

[Lesson 1: Control Flow](#lesson-1-control-flow)<br>
[Lesson 2: Functions](#lesson-2-functions)<br>
[Lesson 3: Lists](#lesson-3-lists)<br>
[Lesson 4: Dictionaries and Structuring Data](#lesson-4-dictionaries-and-structuring-data)<br>
[Lesson 5: Manipulating Strings](#lesson-5-manipulating-strings)<br>
[Lesson 6 - Pattern Matching with Regular Expressions](#lesson-6-pattern-matching-with-regular-expressions)<br>
[Lesson 7 - Input Validation](#lesson-7-input-validation)<br>
[Lesson 8 - Reading and Writing Files](#lesson-8-reading-and-writing-files)<br>
[Lesson 9 - Organizing Files](#lesson-9-organizing-files)<br>
[Lesson 10 - Debugging](#lesson-10-debugging)<br>
[Lesson 11 - Web  Scraping](#lesson-11-web--scraping)<br>
[Lesson 12 - Working with Excel Spreadsheets](#lesson-12-working-with-excel-spreadsheets)<br>
[Lesson 13 - Working with Google Spreadsheets](#lesson-13-working-with-google-spreadsheets)<br>
[Lesson 14 - Working with PDF and Word Documents](#lesson-14-working-with-pdf-and-word-documents)<br>
[Lesson 15 - Working with CSV Files and JSON Data](#lesson-15-working-with-csv-files-and-json-data)<br>
[Lesson 16 - Keeping Time, Scheduling Tasks, and Launching Programs](#lesson-16-keeping-time-scheduling-tasks-and-launching-programs)<br>
[Lesson 17 - Sending Email and Text Messages](#lesson-17-sending-email-and-text-messages)<br>
[Lesson 18 - Manipulating Images](#lesson-18-manipulating-images)<br>
[Lesson 19 - Controlling the Keyboard and Mouse with GUI Automation](#lesson-19-controlling-the-keyboard-and-mouse-with-gui-automation)<br>

# Objective

[Semester's Google Drive Folder](https://drive.google.com/drive/folders/1cDAKYNv1yJ8sKbn1HnCjVv3fdUEZa4JP?usp=sharing)

This semester will (more or less) follow the amazing
book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart

Each chapter will be covered in 1-2 weeks, in a work-at-your-own-pace style. The goal is to use the book as a guide for
learning the programming concepts required for that week's project

This file is a table of contents for the semester. Each week will have a link to the Google Slides presentation, a link
to the GitHub repo for that week's project, and a list of the learning objectives for that week.

---

## Lesson 1: Control Flow

[Google Slides Link](https://docs.google.com/presentation/d/107A5EaseG4CJ8u-WYYzv9BwloNFcO5I8ZIZdcKmb5ts/edit?usp=sharing)<br>

[GitHub Repo Link](https://github.com/JoshLoecker/GirlsCodeLincoln/tree/master/Spring%202024/Lesson%2001%20-%20Control%20Flow)

### Learning Objectives

- **Understand Fundamental Flow Control Concepts:** Understand basic concepts of flow control, including Boolean values,
  comparison operators, and Boolean operators.
  Be able to write expressions using these concepts and evaluate their truth value.
- **Exploring Control Flow Statements:** Explain the structure and function
  of `if`, `else`, `elif`, `while`, `for`, `break`, and `continue` statements for
  controlling program flow. Use these statements appropriately in code examples.
- **Implementing Control Flow in Game Development:** Apply control flow concepts to create a rock/paper/scissors game.

### Weekly Projects
- [Explore Boolean Expressions](./Lesson%2001%20-%20Flow%20Control/explore_boolean_expressions.py)
- [Rock/Paper/Scissors](./Lesson%2001%20-%20Flow%20Control/rock_paper_scissors.py)

---

## Lesson 2: Functions

### Learning Objectives

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

### Weekly Projects
- [The Collatz Sequence](./Lesson%2002%20-%20Functions/the_collatz_sequence.py)
- [Input Validation](./Lesson%2002%20-%20Functions/input_validation.py)

---

## Lesson 3: Lists

### Learning Objectives
- **Understand the Basics of Lists:** Define lists in programming as ordered sequences. Recognize the syntax for
  creating a list and distinguish the "list value" from its internal values.
- **Explore List Methods:** Define methods in programming and their connection to specific data types. Explore and use
  common list methods, such as append() and remove().
- **Compare Sequence Data Types:** Differentiate mutable and immutable sequence data types. Compare lists, tuples, and
  strings, highlighting their unique characteristics and use cases.
- **Grasp the Importance of List References:** Explain that variables store references, not list values directly.
  Introduce the use of copy() and deepcopy() for managing list changes without affecting other variables.

### Weekly Projects
- [Comma Code](./Lesson%2003%20-%20Lists/comma_code.py)
- [Coin Flip Streaks](./Lesson%2003%20-%20Lists/coin_flip_streaks.py)
- [Character Picture Grid](./Lesson%2003%20-%20Lists/character_picture_grid.py)

---

## Lesson 4: Dictionaries and Structuring Data

### Learning Objectives

### Weekly Projects
- [Chess Dictionary Validator](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/chess_dictionary_validator.py)
- [Fantasy Game Inventory](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/fantasy_game_inventory.py)
- [List to Dictionary Function for Fantasy Game Inventory](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/list_to_dictionary_function_for_fantasy_game_inventory.py)

## Lesson 5: Manipulating Strings

### Learning Objectives

### Weekly Projects
- [Table Printer](./Lesson%2005%20-%20Manipulating%20Strings/table_printer.py)
- [Zombie Dice Bots](./Lesson%2005%20-%20Manipulating%20Strings/zombie_dice_bots.py)

---

## Lesson 6 - Pattern Matching with Regular Expressions

### Learning Objectives

### Weekly Projects
- [Date Detection](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/date_detection.py)
- [Strong Password Detection](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/strong_password_detection.py)
- [Regex Version of the `strip()` Method](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/regex_version_of_the_strip_method.py)

---

## Lesson 7 - Input Validation

### Learning Objectives

### Weekly Projects
- [Sandwich Maker](./Lesson%2007%20-%20Input%20Validation/sandwich_maker.py)
- [Write Your Own Multiplication Quiz](./Lesson%2007%20-%20Input%20Validation/write_your_own_multiplication_quiz.py)

---

## Lesson 8 - Reading and Writing Files

### Learning Objectives

### Weekly Projects
- [Extending the Multi-Clipboard](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/extending_the_multi_clipboard.py)
- [Mad Libs](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/mad_libs.py)
- [Regex Search](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/regex_search.py)

---

## Lesson 9 - Organizing Files

### Learning Objectives

### Weekly Projects
- [Selective Copy](./Lesson%2009%20-%20Organizing%20Files/selective_copy.py)
- [Deleting Unneeded Files](./Lesson%2009%20-%20Organizing%20Files/deleting_unneeded_files.py)
- [Filling in the Gaps](./Lesson%2009%20-%20Organizing%20Files/filling_in_the_gaps.py)

---

## Lesson 10 - Debugging

### Learning Objectives

### Weekly Projects
- [Debugging Coin Toss](./Lesson%2010%20-%20Debugging/debugging_coin_toss.py)

---

## Lesson 11 - Web  Scraping

### Learning Objectives

### Weekly Projects
- [Command Line Emailer](./Lesson%2011%20-%20Web%20Scraping/command_line_emailer.py)
- [Image Site Downloader](./Lesson%2011%20-%20Web%20Scraping/image_site_downloader.py)
- [2048](./Lesson%2011%20-%20Web%20Scraping/2048.py)
- [Link Verification](./Lesson%2011%20-%20Web%20Scraping/link_verification.py)

---

## Lesson 12 - Working with Excel Spreadsheets

### Learning Objectives

### Weekly Projects
- [Multiplication Table Maker](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/multiplication_table_maker.py)
- [Blank Row Inserter](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/blank_row_inserter.py)
- [Spreadsheet Cell Inverter](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/spreadsheet_cell_inverter.py)
- [Text Files to Spreadsheet](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/text_files_to_spreadsheet.py)
- [Spreadsheet to Text Files](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/spreadsheet_to_text_files.py)

---

## Lesson 13 - Working with Google Spreadsheets

### Learning Objectives

### Weekly Projects
- [Downloading Google Forms Data](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/downloading_google_forms_data.py)
- [Converting Spreadsheets to Other Formats](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/converting_spreadsheets_to_other_formats.py)
- [Finding Mistakes in a Spreadsheet](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/finding_mistakes_in_a_spreadsheet.py)

---

## Lesson 14 - Working with PDF and Word Documents

### Learning Objectives

### Weekly Projects
- [PDF Paranoia](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/pdf_paranoia.py)
- [Custom Invitations as Word Documents](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/custom_invitations_as_word_documents.py)
- [Brute-Force PDF Password Breaker](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/brute_force_pdf_password_breaker.py)

---

## Lesson 15 - Working with CSV Files and JSON Data

### Learning Objectives

### Weekly Projects
- [Excel-to-CSV Converter](./Lesson%2015%20-%20Working%20with%20CSV%20Files%20and%20JSON%20Data/excel_to_csv_converter.py)

---

## Lesson 16 - Keeping Time, Scheduling Tasks, and Launching Programs

### Learning Objectives

### Weekly Projects
- [Prettified Stopwatch](./Lesson%2016%20-%20Keeping%20Time%2C%20Scheduling%20Tasks%2C%20and%20Launching%20Programs/prettified_stopwatch.py)
- [Scheduled Web Comic Downloader](./Lesson%2016%20-%20Keeping%20Time%2C%20Scheduling%20Tasks%2C%20and%20Launching%20Programs/scheduled_web_comic_downloader.py)

---

## Lesson 17 - Sending Email and Text Messages

### Learning Objectives

### Weekly Projects
- [Random Chore Assignment Emailer](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/random_chore_assignment_emailer.py)
- [Umbrella Reminder](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/umbrella_reminder.py)
- [Auto Unsubscriber](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/auto_unsubscriber.py)
- [Controlling Your Computer Through Email](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/controlling_your_computer_through_email.py)

---

## Lesson 18 - Manipulating Images

### Learning Objectives

### Weekly Projects
- [Extending and Fixing the Chapter Project Programs](./Lesson%2018%20-%20Manipulating%20Images/extending_and_fixing_the_chapter_project_programs.py)
- [Identifying Photo Folders on the Hard Drive](./Lesson%2018%20-%20Manipulating%20Images/identifying_photo_folders_on_the_hard_drive.py)
- [Custom Seating Cards](./Lesson%2018%20-%20Manipulating%20Images/custom_seating_cards.py)

---

## Lesson 19 - Controlling the Keyboard and Mouse with GUI Automation

### Learning Objectives

### Weekly Projects
- [Looking Busy](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/looking_busy.py)
- [Using the Clipboard to Read a Text Field](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/using_the_clipboard_to_read_a_text_field.py)
- [Instant Messenger Bot](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/instant_messenger_bot.py)
- [Game-Playing Bot Tutorial](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/game_playing_bot_tutorial.py)
