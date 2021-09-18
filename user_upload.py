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
        file = open("users.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        print(header)

        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)

        file.close()


# Create class instances to read file:
read = csv_reader()
read.readFile()