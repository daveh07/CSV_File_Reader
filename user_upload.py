#----------------------------------------- CSV READER SCRIPT ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
#----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import csv
import re


# Create CSV reader class that accepts a CSV file input from the user and reads the data in the CSV file.
class csv_reader:
    def __init__(self):
        super().__init__()

    def cleanFile(self):
        with open("users.csv", 'r', encoding='utf-8-sig') as csvfile:     # Open CSV file
            csvreader = csv.reader(csvfile, delimiter=',')                # Read file using Pythons csv.reader module
            header = next(csvreader)                                      # Create list for the header titles
            print(header)

            count = 0
            user_data = []                                        # Create empty list to fill with CSV row data

            for row in csvreader:                                 # Iterate through rows in CSV readable file
                count = count + 1

                row_1 = row[0].title().strip()                    # Title first letter of name & remove whitespaces
                row_1 = re.sub("[^a-zA-Z]+", "", row_1)           # Remove any special characters by Regex

                row_2 = row[1].title().strip()                    # Title first letter of surname & remove whitespaces
                row_2 = re.sub("[^a-zA-Z]+", "", row_2)           # Remove any special characters by Regex

                row_3 = row[2].lower().strip()
                row_3 = re.sub("[^a-zA-Z, @.]+", "", row_3)       # Remove any special characters for email

                user_data.append([row_1, row_2, row_3])           # Append cleaned rows to empty user_data list

                if count > 500:                                   # Condition to stop iterations after 500 entries
                    break                                         # to prevent too many entries to be processed at a time

            return user_data                                      # Print rows to see correct rows are appended

# Create class instances to read file:
read = csv_reader()
print(read.cleanFile())