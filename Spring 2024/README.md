# Python Programming for Automation

Written for the Spring 2024 semester by Josh Loecker

# Table of Contents

[Lesson 1 - Control Flow](#lesson-1---control-flow)<br>
[Lesson 2 - Functions](#lesson-2---functions)<br>
[Lesson 3 - Lists](#lesson-3---lists)<br>
[Lesson 4 - Dictionaries and Structuring Data](#lesson-4---dictionaries-and-structuring-data)<br>
[Lesson 5 - Manipulating Strings](#lesson-5---manipulating-strings)<br>
[Lesson 6 - Pattern Matching with Regular Expressions](#lesson-6---pattern-matching-with-regular-expressions)<br>
[Lesson 7 - Input Validation](#lesson-7---input-validation)<br>
[Lesson 8 - Reading and Writing Files](#lesson-8---reading-and-writing-files)<br>
[Lesson 9 - Organizing Files](#lesson-9---organizing-files)<br>
[Lesson 10 - Debugging](#lesson-10---debugging)<br>
[Lesson 11 - Web  Scraping](#lesson-11---web--scraping)<br>
[Lesson 12 - Working with Excel Spreadsheets](#lesson-12---working-with-excel-spreadsheets)<br>
[Lesson 13 - Working with Google Spreadsheets](#lesson-13---working-with-google-spreadsheets)<br>
[Lesson 14 - Working with PDF and Word Documents](#lesson-14---working-with-pdf-and-word-documents)<br>
[Lesson 15 - Working with CSV Files and JSON Data](#lesson-15---working-with-csv-files-and-json-data)<br>
[Lesson 16 - Keeping Time, Scheduling Tasks, and Launching Programs](#lesson-16---keeping-time-scheduling-tasks-and-launching-programs)<br>
[Lesson 17 - Sending Email and Text Messages](#lesson-17---sending-email-and-text-messages)<br>
[Lesson 18 - Manipulating Images](#lesson-18---manipulating-images)<br>
[Lesson 19 - Controlling the Keyboard and Mouse with GUI Automation](#lesson-19---controlling-the-keyboard-and-mouse-with-gui-automation)<br>

# Objective

[Semester's Google Drive Folder](https://drive.google.com/drive/folders/1cDAKYNv1yJ8sKbn1HnCjVv3fdUEZa4JP?usp=sharing)

This semester will (more or less) follow the amazing
book ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) by Al Sweigart

Each chapter will be covered in 1-2 weeks, in a work-at-your-own-pace style. The goal is to use the book as a guide for
learning the programming concepts required for that week's project

This file is a table of contents for the semester. Each week will have a link to the Google Slides presentation, a link
to the GitHub repo for that week's project, and a list of the learning objectives for that week.

---

## Lesson 1 - Control Flow

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

## Lesson 2 - Functions

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

## Lesson 3 - Lists

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

## Lesson 4 - Dictionaries and Structuring Data

### Learning Objectives
- **Master the Dictionary Data Type:** Define the dictionary data type and its role in organizing and accessing data.
  Understand the concept of key-value pairs in dictionaries. Identify the various data types that can serve as keys in
  dictionaries.
- **Compare Lists and Dictionaries:** Contrast the differences between lists and dictionaries in terms of structure and
  functionality. Recognize the advantages of using dictionaries, particularly in mapping one item to another, compared
  to the sequential nature of lists.
- **Apply Dictionaries in Data Modeling:** Explore how dictionaries can be effectively combined with lists to create
  complex data structures. Develop the ability to model real-world objects using dictionaries, enhancing program
  representation.
- **Hands-On: Create a Tic-Tac-Toe Data Structure:** Apply knowledge of dictionaries and lists to create a data
  structure for modeling a tic-tac-toe board. Understand the advantages of using a combination of dictionaries and lists
  for organizing complex game-related data.

### Weekly Projects
- [Chess Dictionary Validator](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/chess_dictionary_validator.py)
- [Fantasy Game Inventory](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/fantasy_game_inventory.py)
- [List to Dictionary Function for Fantasy Game Inventory](./Lesson%2004%20-%20Dictionaries%20and%20Structuring%20Data/list_to_dictionary_function_for_fantasy_game_inventory.py)

## Lesson 5 - Manipulating Strings

### Learning Objectives
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

### Weekly Projects
- [Table Printer](./Lesson%2005%20-%20Manipulating%20Strings/table_printer.py)
- [Zombie Dice Bots](./Lesson%2005%20-%20Manipulating%20Strings/zombie_dice_bots.py)

---

## Lesson 6 - Pattern Matching with Regular Expressions

### Learning Objectives
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

### Weekly Projects
- [Date Detection](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/date_detection.py)
- [Strong Password Detection](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/strong_password_detection.py)
- [Regex Version of the `strip()` Method](./Lesson%2006%20-%20Pattern%20Matching%20with%20Regular%20Expressions/regex_version_of_the_strip_method.py)

---

## Lesson 7 - Input Validation

### Learning Objectives
- **Understanding the Importance of Input Validation:** Recognize the significance of input validation in preventing
  nonsensical or incorrect user inputs. Understand how input validation contributes to code robustness, bug prevention,
  and security.
- **Implementing Basic Input Validation Code:** Learn the fundamentals of input validation through a basic example using
  a while loop. Understand the key components of input validation code, such as type conversion, exception handling, and
  conditional statements.
- **Exploring Challenges with Manual Input Validation:** Identify potential challenges and drawbacks of manually
  implementing input validation for every input() call in a program. Understand the limitations and the risk of
  overlooking certain cases in manual input validation.

### Weekly Projects
- [Sandwich Maker](./Lesson%2007%20-%20Input%20Validation/sandwich_maker.py)
- [Write Your Own Multiplication Quiz](./Lesson%2007%20-%20Input%20Validation/write_your_own_multiplication_quiz.py)

---

## Lesson 8 - Reading and Writing Files

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

### Weekly Projects
- [Extending the Multi-Clipboard](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/extending_the_multi_clipboard.py)
- [Mad Libs](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/mad_libs.py)
- [Regex Search](./Lesson%2008%20-%20Reading%20and%20Writing%20Files/regex_search.py)

---

## Lesson 9 - Organizing Files

### Learning Objectives
- **Automating File Organization:** Understand the benefits of automating file organization tasks in Python. Recognize
  scenarios where automating file copying, renaming, moving, and compressing can significantly improve efficiency.
- **Exploring Common File Organization Tasks:** Identify common file organization tasks, such as copying specific file
  types, renaming files in bulk, and compressing multiple folders into a ZIP file. Understand the potential time savings
  and accuracy improvements achieved through automation.
- **Introduction to File Extensions:** Understand the concept of file extensions and their role in identifying file
  types. Learn how to view file extensions on different operating systems and file browsers.
- **Best Practices in File Handling Code:** Learn best practices for writing file handling code, including commenting
  out potentially risky operations and using print() calls for verification. Understand the importance of testing and
  verifying file handling code before executing potentially irreversible operations.
- **Preparing for Code Analysis and Debugging:** Acknowledge that writing perfect programs is a rare occurrence and that
  debugging is a crucial part of the programming process. Anticipate the next chapter's focus on Python modules that aid
  in code analysis and debugging for improving program correctness.

### Weekly Projects
- [Selective Copy](./Lesson%2009%20-%20Organizing%20Files/selective_copy.py)
- [Deleting Unneeded Files](./Lesson%2009%20-%20Organizing%20Files/deleting_unneeded_files.py)
- [Filling in the Gaps](./Lesson%2009%20-%20Organizing%20Files/filling_in_the_gaps.py)

---

## Lesson 10 - Debugging

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

### Weekly Projects
- [Debugging Coin Toss](./Lesson%2010%20-%20Debugging/debugging_coin_toss.py)

---

## Lesson 11 - Web  Scraping

### Learning Objectives
- **Recognizing the Significance of Web Scraping:** Understand the importance of web scraping in programming, especially
  when much of computer work involves internet-related tasks. Recognize the value of extending programs to access and
  process content from the web.
- **Exploring Essential Modules for Web Scraping:** Learn about key Python modules for web scraping, including
  webbrowser, requests, bs4 (Beautiful Soup), and selenium. Understand the functionalities provided by each module, such
  as opening a browser, downloading files and web pages, parsing HTML, and controlling web browsers.
- **Hands-On Application of Web Scraping Techniques:** Gain practical experience in using web scraping modules for
  common tasks, such as downloading web pages, parsing HTML content, and controlling web browsers. Explore the requests
  module for straightforward downloads and the BeautifulSoup module for parsing downloaded pages with basic HTML
  concepts and selectors. Understand the role of the selenium module in fully automating web-based tasks, including
  logging in to websites and filling out forms automatically.

### Weekly Projects
- [Command Line Emailer](./Lesson%2011%20-%20Web%20Scraping/command_line_emailer.py)
- [Image Site Downloader](./Lesson%2011%20-%20Web%20Scraping/image_site_downloader.py)
- [2048](./Lesson%2011%20-%20Web%20Scraping/2048.py)
- [Link Verification](./Lesson%2011%20-%20Web%20Scraping/link_verification.py)

---

## Lesson 12 - Working with Excel Spreadsheets

### Learning Objectives
- **Understanding the Challenges in Data Processing:** Recognize that the difficulty in processing information often
  lies in formatting data appropriately for programmatic manipulation. Understand the importance of efficient data
  processing for enhancing program functionality.
- **Exploring Python's Role in Spreadsheet Handling:** Learn about the openpyxl module and its significance in loading
  and manipulating spreadsheets within Python. Understand the advantages of using Python for extracting and manipulating
  data from spreadsheets.
- **Leveraging Python for Spreadsheet Automation:** Gain practical skills in automating spreadsheet tasks using Python,
  such as copying and pasting data, making edits based on criteria, and searching for specific information in multiple
  spreadsheets. Recognize the efficiency gains achieved by using Python to perform repetitive and mindless spreadsheet
  tasks.

### Weekly Projects
- [Multiplication Table Maker](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/multiplication_table_maker.py)
- [Blank Row Inserter](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/blank_row_inserter.py)
- [Spreadsheet Cell Inverter](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/spreadsheet_cell_inverter.py)
- [Text Files to Spreadsheet](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/text_files_to_spreadsheet.py)
- [Spreadsheet to Text Files](./Lesson%2012%20-%20Working%20with%20Excel%20Spreadsheets/spreadsheet_to_text_files.py)

---

## Lesson 13 - Working with Google Spreadsheets

### Learning Objectives
- **Recognizing the Role of Spreadsheets in Data Organization:** Understand that spreadsheets serve as essential tools
  for organizing information into two-dimensional data structures and performing calculations with formulas. Recognize
  the common use of spreadsheets for producing charts and visualizing data.
- **Integrating Python with Microsoft Excel:** Learn about the openpyxl module and its role in enabling Python programs
  to read and modify Excel spreadsheet files. Explore practical applications of Python in automating repetitive tasks
  within Excel, such as copying data, making edits based on criteria, and analyzing large datasets.
- **Understanding the Power of Python in Spreadsheet Automation:** Recognize the potential of Python in automating
  mindless and repetitive spreadsheet tasks, leading to increased efficiency. Understand how Python, equipped with the
  openpyxl module, can handle even the most extensive spreadsheets with ease.

### Weekly Projects
- [Downloading Google Forms Data](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/downloading_google_forms_data.py)
- [Converting Spreadsheets to Other Formats](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/converting_spreadsheets_to_other_formats.py)
- [Finding Mistakes in a Spreadsheet](./Lesson%2013%20-%20Working%20with%20Google%20Spreadsheets/finding_mistakes_in_a_spreadsheet.py)

---

## Lesson 14 - Working with PDF and Word Documents

### Learning Objectives
- **Exploring Python Modules for PDF and Word Interaction:** Learn about Python modules, PyPDF2, and python-docx,
  designed to facilitate interaction with PDFs and Word documents, respectively. Understand the importance of using
  these modules for more than basic file operations, considering the complexity of the file formats.
- **Utilizing PyPDF2 for PDF Document Manipulation:** Explore the functionality provided by the PyPDF2 module for
  reading and writing PDF documents in Python. Acknowledge the potential challenges in reading text from PDFs due to the
  intricate PDF file format and the limitations of PyPDF2.
- **Understanding the Complexity of PDF and Word Documents:** Recognize that PDF and Word documents are binary files
  with additional complexity compared to plaintext files. Understand that these files store not only text but also font,
  color, and layout information, requiring specialized handling in Python.

### Weekly Projects
- [PDF Paranoia](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/pdf_paranoia.py)
- [Custom Invitations as Word Documents](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/custom_invitations_as_word_documents.py)
- [Brute-Force PDF Password Breaker](./Lesson%2014%20-%20Working%20with%20PDF%20and%20Word%20Documents/brute_force_pdf_password_breaker.py)

---

## Lesson 15 - Working with CSV Files and JSON Data

### Learning Objectives
- **Understanding CSV and JSON as Plaintext File Formats:** Recognize CSV as an acronym for "comma-separated values" and
  understand that CSV files store simplified spreadsheets as plaintext. Grasp the concept that JSON (JavaScript Object
  Notation) stores information in JavaScript source code in plaintext files, making it a common format in web
  applications.
- **Exploring Python's csv and json Modules:** Learn about Python's csv module, designed for parsing and handling CSV
  files, and understand its functions. Explore the json module in Python, which simplifies the process of reading and
  writing to JSON files, and comprehend its usage.
- **Parsing Data from Common Plaintext Formats:** Understand the significance of CSV and JSON as common plaintext
  formats for storing data, facilitating easy parsing by programs while remaining human-readable. Acknowledge the role
  of the csv and json modules in Python in simplifying the handling of data stored in CSV and JSON file formats.

### Weekly Projects
- [Excel-to-CSV Converter](./Lesson%2015%20-%20Working%20with%20CSV%20Files%20and%20JSON%20Data/excel_to_csv_converter.py)

---

## Lesson 16 - Keeping Time, Scheduling Tasks, and Launching Programs

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

### Weekly Projects
- [Prettified Stopwatch](./Lesson%2016%20-%20Keeping%20Time%2C%20Scheduling%20Tasks%2C%20and%20Launching%20Programs/prettified_stopwatch.py)
- [Scheduled Web Comic Downloader](./Lesson%2016%20-%20Keeping%20Time%2C%20Scheduling%20Tasks%2C%20and%20Launching%20Programs/scheduled_web_comic_downloader.py)

---

## Lesson 17 - Sending Email and Text Messages

### Learning Objectives
- **Email Automation Proficiency:** Gain a comprehensive understanding of the EZGmail module for sending and reading
  emails from Gmail accounts using Python. Learn to utilize Python's smtplib, imapclient, and pyzmail modules for
  interacting with standard SMTP and IMAP email protocols. Develop the skills to automate email-related tasks, such as
  sending personalized emails based on data from spreadsheets. Explore techniques for handling security and spam
  precautions when accessing email services, especially with a focus on using the EZGmail module for Gmail API
  integration.
- **SMS Notification Implementation:** Acquire the knowledge to integrate SMS notification features into Python programs
  using services like Twilio. Understand the setup process for sending text messages from programs, including the
  necessary modules and initial configurations. Explore scenarios where SMS notifications are beneficial, such as
  receiving program status updates while away from the computer. Develop proficiency in writing code to trigger SMS
  notifications based on specific conditions, enhancing the overall functionality and user experience of Python
  programs.
- **Cross-Program Communication via Email:** Learn how Python programs can communicate directly with each other through
  email using SMTP and IMAP protocols. Understand the differences between SMTP and IMAP protocols, and their respective
  roles in sending and retrieving emails. Explore the potential for cross-computer communication by writing programs
  that exchange information via email. Develop skills in searching for, downloading, and parsing emails to extract
  relevant information, expanding the capabilities of Python programs beyond individual systems.

### Weekly Projects
- [Random Chore Assignment Emailer](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/random_chore_assignment_emailer.py)
- [Umbrella Reminder](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/umbrella_reminder.py)
- [Auto Unsubscriber](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/auto_unsubscriber.py)
- [Controlling Your Computer Through Email](./Lesson%2017%20-%20Sending%20Email%20and%20Text%20Messages/controlling_your_computer_through_email.py)

---

## Lesson 18 - Manipulating Images

### Learning Objectives
- **Introduction to Image Processing with Python and Pillow:** Understand the significance of automating image editing
  tasks for efficiency. Learn about the Pillow module, a third-party Python library, and its role in interacting with
  digital image files. Gain knowledge of the functions provided by Pillow for tasks such as cropping, resizing, and
  editing the content of images. Acquire the skills to install the Pillow module using pip and understand the versioning
  considerations.
- **Basic Concepts of Image Representation and Manipulation:** Comprehend the fundamental concepts of digital images,
  including pixels, RGBA values, and x- and y-coordinates. Explore common image formats, such as JPEG and PNG, and
  understand how the pillow module can handle these formats. Learn about the Image object in Pillow, including how it
  stores dimensions and supports methods for image manipulations. Gain proficiency in using methods like crop(), copy(),
  paste(), resize(), rotate(), and transpose() for common image operations.
- **Advanced Image Editing and Drawing with Pillow:** Explore advanced image editing capabilities provided by Pillow,
  including drawing shapes like points, lines, rectangles, ellipses, and polygons. Understand how to draw text onto an
  image with customizable typeface and font size using Pillow's ImageDraw methods. Learn the process of saving edited
  images using the save() method of the Image object. Recognize the cost-effective alternative Python offers for batch
  processing of images, highlighting the capabilities of Python scripts in comparison to expensive applications like
  Photoshop.

### Weekly Projects
- [Extending and Fixing the Chapter Project Programs](./Lesson%2018%20-%20Manipulating%20Images/extending_and_fixing_the_chapter_project_programs.py)
- [Identifying Photo Folders on the Hard Drive](./Lesson%2018%20-%20Manipulating%20Images/identifying_photo_folders_on_the_hard_drive.py)
- [Custom Seating Cards](./Lesson%2018%20-%20Manipulating%20Images/custom_seating_cards.py)

---

## Lesson 19 - Controlling the Keyboard and Mouse with GUI Automation

### Learning Objectives
- **Understanding GUI Automation with Python and PyAutoGUI:** Recognize the significance of GUI automation in automating
  tasks on a computer. Understand the concept of graphical user interface (GUI) automation and its role in controlling
  keyboard and mouse actions programmatically. Learn about PyAutoGUI as a Python module for GUI automation and its
  capabilities in simulating mouse movements, clicks, keyboard inputs, and more. Explore the advantages of GUI
  automation, especially for tasks involving repetitive clicking or form filling.
- **Exploring PyAutoGUI Functions and Features:** Gain proficiency in using PyAutoGUI functions to move the mouse
  cursor, simulate mouse clicks, and execute keyboard inputs. Understand the capabilities of PyAutoGUI in checking
  screen colors and obtaining information about the screen contents. Learn how PyAutoGUI can analyze a screenshot to
  determine coordinates for specific areas on the screen. Explore the limitations and considerations when writing GUI
  automation programs, with a focus on preventing errors and ensuring robustness.
- **Creating Efficient and Repetitive Task Automation with PyAutoGUI:** Develop practical skills in combining PyAutoGUI
  features to automate repetitive tasks on a computer. Understand the hypnotic and satisfying aspects of watching the
  mouse cursor move autonomously and text appear on the screen during automation. Learn best practices for writing GUI
  automation programs that crash quickly in case of bad instructions, ensuring efficient error handling. Explore the
  potential time-saving benefits of using PyAutoGUI to delegate tedious and repetitive work, allowing users to focus on
  more engaging and creative aspects of their responsibilities.

### Weekly Projects
- [Looking Busy](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/looking_busy.py)
- [Using the Clipboard to Read a Text Field](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/using_the_clipboard_to_read_a_text_field.py)
- [Instant Messenger Bot](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/instant_messenger_bot.py)
- [Game-Playing Bot Tutorial](./Lesson%2019%20-%20Controlling%20the%20Keyboard%20and%20Mouse%20with%20GUI%20Automation/game_playing_bot_tutorial.py)
