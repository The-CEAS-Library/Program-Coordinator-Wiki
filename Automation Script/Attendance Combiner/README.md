# Read Me

This program is designed to combine and analyze CSV files containing attendee information. The user can choose to either combine the documents or check attendance. The program prompts the user for input regarding what to combine, including sign-up attendees, workshop attendance, or Zoom attendance.

## Requirements

This program requires Python 3.x and the pandas library.

## Usage

1. Run the program by executing the Python script.
2. The program will prompt the user to enter whether they want to combine documents (1) or check attendance (2).
3. Next, the user must specify what to combine (sign up attendees, workshop attendance, or Zoom attendance).
4. The program will then loop through all CSV files in the current directory, reading in the data and combining it with the existing data.
5. Depending on the user's choice, the program will then remove duplicates based on the specified column, drop specified columns, remove anyone who has 'Cancelled' in the Status column (for sign-up attendees), remove the instructor from the data (for Zoom attendance), sort the data by the FirstName column, and write the combined data to an Excel file called "finalize.xlsx".

## Note

This program is not intended to modify the original CSV files, and the user should make sure to back up the original files before running this program.

The provided CSV files serve as a demonstration of the process of merging five attendance lists from a Python Workshop Series into a single file named "finalized.xlsx".
