import csv
import re

#-------------------------------- TEST CLEANING CSV TEXT ------------------------------------#
with open("users.csv", 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    user_data = []

    for row in csv_reader:
        row_1 = row[0].title().strip()
        row_1 = re.sub("[^a-zA-Z]+", "", row_1)

        row_2 = row[1].title().strip()
        row_2 = re.sub("[^a-zA-Z]+", "", row_2)

        row_3 = row[2].lower().strip()
        row_3 = re.sub("[^a-zA-Z, @.]+", "", row_3)

        user_data.append([row_1, row_2, row_3])

    print(user_data)