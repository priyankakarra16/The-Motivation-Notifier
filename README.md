# The-Motivation-Notifier
Daily Motivation Notifier: A fundamental Python project demonstrating file I/O and randomization logic to provide instant, stress-relieving motivational quotes directly in the terminal.

#Daily Motivation Notifier
Overview of the Project
The Daily Motivation Notifier is a minimalist Command-Line Interface (CLI) application built in Python 3. It addresses the need for instantaneous, stress-relieving positive reinforcement by reading quotes from a local data file (quotes.txt) and delivering a fresh, random message on demand via a simple menu. It serves as a strong demonstration of core Python capabilities, including file handling and error robustness.

#Features
Random Quote Generation (FR02): Selects and displays a new motivational quote randomly upon request.
Simple Menu Interface (FR04): Easy-to-use numbered menu for quick quote retrieval or program exit.
Robust File Handling (FR05): Checks for and handles errors gracefully if the quotes.txt file is missing or empty.
Zero Dependencies: Built entirely using native Python features (e.g., os, random, file I/O).

#Technologies/Tools Used
Component
Technology/Concept Used
Language
Python 3.x
Data Source
Local Text File (quotes.txt)
Randomization
Python's random module
Environment
Command-Line Interface (CLI)

#Steps to Install & Run the Project
Prerequisites
You only need Python 3 installed on your system.
Installation and Execution
Clone Files: Download the daily_notifier.py and quotes.txt files to the same directory.
Execute: Run the script from your terminal:
python daily_notifier.py
Usage: Select option 1 to generate a new quote or option 2 to exit.

#Instructions for Testing
Test the application using the following scenarios:
Normal Flow: Select option 1 multiple times to confirm new, random quotes are displayed (FR02).
Missing File Test: Delete or rename quotes.txt and run the script. It must display the [FILE ERROR] and the hardcoded fallback message (FR05).
Reliability Test: Enter invalid input (e.g., 5 or text) at the menu prompt. The program must return to the menu without crashing.
Exit: Select option 2 to confirm clean program termination.
