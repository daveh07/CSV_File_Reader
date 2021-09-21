# CSV FILE READER - CLI APPLICATION
A command line application that parses csv files, cleans fields from whitespaces & special characters, validates email address and stores a user table to PostgreSQL

### REPL - View Live CLI Application Demo:
Refer to link below to run the code from Repl.it CLI
https://replit.com/@daveh87/CSVFileReaderApp?embed=1#main.py

### Setup
Clone the repository:

> https://github.com/daveh07/CSV_File_Reader.git

> Py Version: Python 3.9

> Create a virtual environment.

> pip3 install psycopg2-binary

> To run application, open shell and run in Terminal/Command Line:
> --file [csv file name]

>eg):

> python3 user_input.py --file users.csv --help

> This will return the help menu and list commands

### DATABASE PARAMETERS
Username = david
Host = localhost
Password = ""

### NOTE:
Please feel free to add any contributions! 

### What I Learned
<li>Parsing and cleaning csv file data</li>
<li>Using Regex to validate email addresses</li>
<li>Using open source PostgreSQL data base</li>
<li>Creating lists of user data to store to PostgreSQL database table</li>
<li>Parsed arguments to create Command Line directives using argparse package</li>
