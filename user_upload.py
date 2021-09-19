#----------------------------------------- CSV READER SCRIPT ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
#----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import csv
import re
import sys


# CSV reader class that accepts a CSV file input from the user and reads the data in the CSV file.
class csv_reader:
    def __init__(self):
        super().__init__()

    # Function to clean the CSV file from whitespaces, tabs, special characters & validate legal email addresses
    def cleanFile(self):


        fname = input("Input name of csv file you want to open in format 'example.csv': ")

        if fname.endswith(".csv"):
            print(f"csv file name = " + str(fname))
        else:
            print("Error loading csv file. Check correct file format")

        with open(fname, 'r') as csvfile:                                                          # Open CSV file
            csvreader = csv.reader(csvfile, delimiter=',')                                         # Read file using Pythons csv.reader module
            header = next(csvreader)                                                               # Create list for the header titles
            clean_header = []
            for i in range(len(header)):
                clean_header.append(header[i].strip())
            # clean_header = [header[0].strip(), header[1].strip(), header[2].strip()]
            #print(clean_header)

            count = 0
            user_data = []                                                                         # Create empty list to fill with CSV row data

            # Regex for validating an Email
            regex_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$' ### TO BE REVIEWED

            for row in csvreader:                                                                  # Iterate through rows in CSV readable file
                count = count + 1

                row_1 = row[0].title().strip()                                                     # Title first letter of name & remove whitespaces
                row_1 = re.sub("[^a-zA-Z'-]+", "", row_1)                                            # Remove any special characters by Regex

                row_2 = row[1].title().strip()                                                     # Title first letter of surname & remove whitespaces
                row_2 = re.sub("[^a-zA-Z'-]+", "", row_2)                                            # Remove any special characters by Regex

                row_3 = row[2].lower().strip()

                if re.fullmatch(regex_email, row[2]):
                    row_3 = row_3
                else:
                    row_3 = "Invalid Email"

                user_data.append([row_1, row_2, row_3])                                            # Append cleaned rows to empty user_data list

                if count > 500:                                                                    # Condition to stop iterations after 500 entries
                    break                                                                          # to prevent too many entries to be processed at a time

            return clean_header, user_data                                                                      # Print rows to see correct rows are appended


# USER CLI INPUTS
def userCommandLine():
    introduction_text = """
    #========================================================================================================#
                                           CSV READER APPLICATION - CLI
                                                  version: 1.0
                                                    21/09/201
    #========================================================================================================#

    Please select from command list below:
    For a description of the command line directives, please type type '--help' into the command line.

    |--- FILE COMMANDS ---|
    -- file [csv file name]
    --dry_run
    --help

    |--- PostgreSQL Commands ---|
    --create_table
    -u – PostgreSQL username
    -p – PostgreSQL password
    -h – PostgreSQL host
    
    #========================================================================================================#
    """

    print(introduction_text)
    # print(command_directives)

    initial_input = input("Enter a command: ")
    if initial_input == "--help":
        print("""
        #========================================================================================================#
                                             CSV READER APPLICATION - CLI
                                           HELP - COMMAND LINE DESCRIPTIONS
        #========================================================================================================#
        
        -- file [csv file name] - This is the name of the CSV to be parsed
        --dry_run -  This will be used with the (--file) directive in case we want to run the script but not insert 
                     into the DB. All other functions will be executed, but the database won't be altered
    
        |--- PostgreSQL Commands ---|
        --create_table - This will create the users database table from the csv and store to the PostgreSQL database
        -u – PostgreSQL username 
        -p – PostgreSQL password
        -h – PostgreSQL host
        
        #========================================================================================================#
        """)
    elif initial_input == "--dry_run":
        read = csv_reader()
        print(read.cleanFile())
    elif initial_input == "--file":
        read = csv_reader()
        read.cleanFile()
    else:
        pass


# Create class instances to read and clean file:
userCommandLine()






