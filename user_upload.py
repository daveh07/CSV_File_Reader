#----------------------------------------- CSV READER SCRIPT ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
#----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import csv
import re
import sys


# Create CSV reader class that accepts a CSV file input from the user and reads the data in the CSV file.
class csv_reader:
    def __init__(self):
        super().__init__()

    # Function to clean the CSV file from whitespaces, tabs, special characters & validate legal email addresses
    def cleanFile(self):

        fname = input(str("File name in of csv file you would like to open: (in format 'example.csv'): "))

        with open(fname, 'r') as csvfile:                           # Open CSV file
            csvreader = csv.reader(csvfile, delimiter=',')                # Read file using Pythons csv.reader module
            header = next(csvreader)                                      # Create list for the header titles
            clean_header = [header[0].strip(), header[1].strip(), header[2].strip()]      # Clean Header text
            print(clean_header)

            count = 0
            user_data = []                                        # Create empty list to fill with CSV row data

            # Regex for validating an Email
            regex_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$' ### TO BE REVIEWED

            for row in csvreader:                                 # Iterate through rows in CSV readable file
                count = count + 1

                row_1 = row[0].title().strip()                    # Title first letter of name & remove whitespaces
                row_1 = re.sub("[^a-zA-Z]+", "", row_1)           # Remove any special characters by Regex

                row_2 = row[1].title().strip()                    # Title first letter of surname & remove whitespaces
                row_2 = re.sub("[^a-zA-Z]+", "", row_2)           # Remove any special characters by Regex

                row_3 = row[2].lower().strip()

                if re.fullmatch(regex_email, row[2]):
                    row_3 = row_3
                else:
                    row_3 = "Invalid Email"

                user_data.append([row_1, row_2, row_3])           # Append cleaned rows to empty user_data list

                if count > 500:                                   # Condition to stop iterations after 500 entries
                    break                                         # to prevent too many entries to be processed at a time

            return user_data                                      # Print rows to see correct rows are appended


# Create class instances to read and clean file:
read = csv_reader()
print(read.cleanFile())
