#----------------------------------------- MODULE TESTS ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
#----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import csv


# TEST NI
def test_ReadFile():
    with open("users.csv", 'r') as csvfile:  # Open file
        csvreader = csv.reader(csvfile)  # Read file using Pythons csv.reader module
        header = next(csvreader)  #

        rows = []
        for row in csvreader:
            rows.append(row)
        print("Total no. of rows: %d" % (csvreader.line_num))
        csvfile.close()


test_ReadFile()
