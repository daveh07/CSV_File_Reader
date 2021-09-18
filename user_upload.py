#----------------------------------------- CSV READER SCRIPT ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
#----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import csv


# Create CSV reader class that accepts a CSV file input from the user and reads the data in the CSV file.
class csv_reader:
    def __init__(self):
        super().__init__()

    def readFile(self):
        with open("users.csv", 'r') as csvfile:          # Open CSV file
            csvreader = csv.reader(csvfile)              # Read file using Pythons csv.reader module
            header = next(csvreader)                     # Create list for the header titles
            print(header)                                # Print header list

            rows = []                                    # Create empty list to fill with CSV row data
            for row in csvreader:                        # Iterate through rows in CSV readable file
                rows.append(row)                         # Append rows to rows list
            print(rows)                                  # Print rows to see correct rows are appended

# Method to iterate through the name and last names in the CSV file and capitalize names
    def titleNames(self):
        pass


# Create class instances to read file:
read = csv_reader()
read.readFile()