import csv
import re
import sys


#-------------------------------- TEST CLEANING CSV TEXT ------------------------------------#
def cleanCSV_Test():
    with open("users.csv", 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)  # Create list for the header titles
        clean_header = []
        for i in range(len(header)):
            clean_header.append(header[i].strip())
        print(clean_header)

        user_data = []
        # for validating an Email
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        for row in csv_reader:
            row_1 = row[0].title().strip()
            row_1 = re.sub("[^a-zA-Z]+", "", row_1)

            row_2 = row[1].title().strip()
            row_2 = re.sub("[^a-zA-Z]+", "", row_2)

            row_3 = row[2].lower()

            user_data.append([row_1, row_2, row_3])

        print(user_data)

# -------------------------------- TEST CLEANING VALIDATING EMAIL ------------------------------------#
def emailValidationTest():
    with open("users.csv", 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)  # Create list for the header titles
        print(header)

        count = 0
        user_data_email_test = []
        # for validating an Email
        regex_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$' #### COME BACK AND REVIEW

        for row in csv_reader:
            count = count + 1

            row_1_ve = row[0].title().strip()
            row_1_ve = re.sub("[^a-zA-Z]+", "", row_1_ve)

            row_2_ve = row[1].title().strip()
            row_2_ve = re.sub("[^a-zA-Z]+", "", row_2_ve)

            row_3_ve = row[2].lower()

            # Check if email is valid
            if re.fullmatch(regex_email, row[2]):
                row_3_ve = row_3_ve
            else:
                row_3_ve = "Invalid Email"

            if count > 500:
                break

            user_data_email_test.append([row_1_ve, row_2_ve, row_3_ve])

        print(user_data_email_test)


cleanCSV_Test()
emailValidationTest()
