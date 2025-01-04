# file-error-_-handling
error handling and  file handling in python
Overview

This Python script demonstrates basic file handling operations, including opening, reading, and writing to files. It also showcases error handling for scenarios where a file may not exist.

Features

Opening and Reading a File

Opens an existing file named nyanjui.txt in read mode.

Reads and prints the content of the file.

Creating and Writing to a File

Creates a new file named sawa.txt in write mode.

Writes the string "saw sawa" into the file.

Error Handling

Prompts the user to input a file name.

Attempts to open the specified file.

Catches the FileNotFoundError if the file does not exist and displays an appropriate message.

Ensures a final message of gratitude is always displayed, using the finally block.

How to Run the Code

Make sure Python is installed on your system.

Save the code to a file named file_handling.py.

Create a text file named nyanjui.txt in the same directory and populate it with sample content.

Open a terminal or command prompt and navigate to the directory containing file_handling.py.

Run the script using the command:

python file_handling.py

Follow the prompts as displayed.

Expected Output

The content of nyanjui.txt will be printed.

A new file, sawa.txt, will be created with the content "saw sawa".

Depending on the user input for the file name:

If the file exists, its content will be displayed.

If the file does not exist, the program will show: File does not exist in our database.

The program will always end with the message: thank you for your understanding.

Notes

Ensure that nyanjui.txt exists before running the script to avoid errors.

sawa.txt will be overwritten each time the script is run.

Always verify user input for file names to avoid unintended errors.

Author

Ndung'u Ian Kinyanjui
