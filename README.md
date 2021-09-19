# CSV FILE READER - CLI APPLICATION
A command line application that parses csv files, cleans fields from whitespaces & special characters, validates email address and stores a user table to PostgreSQL

### REPL - View Live CLI Application Demo:
Refer to link below to run the code from Repl.it CLI
"link to be added soon"

### Setup
Clone the repository:

> https://github.com/daveh07/CSV_File_Reader.git

> Py Version: Python 3.9

> Create a virtual environment and run user_upload.py script

> Enter a command from the list

|--- FILE COMMANDS ---|
-- file - Creates a string input for the csv file name to be parsed. The output will parse and clean the csv file. An error will occur for wrong file types
--dry_run - Creates a string input for the csv file name to be parsed. The output will parse and clean the csv file and show the csv data output but will not 
            store to the PostgreSQL database
--help   - This will show descriptions of the what the CLI commands on the application interface

|--- PostgreSQL Commands ---|
--create_table -             Creates a string input for the csv file name to be parsed. The output will parse and clean the csv file and show the csv data output 
                             and will create and store a user table to PostgreSQL database. Invalid emails will not be store and errors will be shown for invalid
                             email addresses
-u – PostgreSQL username
-p – PostgreSQL password
-h – PostgreSQL host

### NOTE:
Please feel free to add any contributions! 

### What I Learned
<li>Parsing and cleaning csv file data</li>
<li>Using Regex to validate email addresses</li>
<li>Using open source PostgreSQL data base</li>
<li>Creating lists of user data to store to PostgreSQL database table</li>
<li>Input various commands into CLI and use conditional statements to run the certain functions to the appropriate command directive</li>
