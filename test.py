import csv
import re
import sys
import psycopg2
import argparse
import user_upload


#-------------------------------- TEST CLEANING CSV TEXT ------------------------------------#
def cleanCSV_Test():
    with open("users.csv", 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)  # Create list for the header titles
        clean_header = []
        for i in range(len(header)):
            clean_header.append(header[i].strip())
        print(type(clean_header))
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

        print(type(user_data))
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


#-------------------------------- DATABASE CONNECTION TEST ------------------------------------#
def create_database_table_test():


    db_name = "csv_reader_db"
    db_user = "david"
    db_host = "localhost"
    db_password = ""
    db_port = 5432

    # Connect to PostgreSQL database
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

    #cur = conn.curor()

   # cur.execute("CREATE TABLE users ( name VARCHAR, surname VARCHAR, email VARCHAR )")

   # cur.close()

    conn.close()

create_database_table_test()


def parsArgs():
#------------------------------------ TEST COMMAND LINE ARGUMENTS ----------------------------------------------#
    my_parser = argparse.ArgumentParser(add_help=False)
    my_parser.add_argument('--file', action='store', type=str, required=True)
    my_parser.add_argument('--create_table', help='create table', action='store_const', const=True)
    my_parser.add_argument('--dry_run', help='dry run', action='store_const', const=True)
    my_parser.add_argument('-u', help='username', action='store', type=str, )
    my_parser.add_argument('-p', help='password', action='store', type=str, )
    my_parser.add_argument('-h', help='host', action='store', type=str, )
    my_parser.add_argument('--help', help='help', action='store_const', const=True)

    args = my_parser.parse_args()
    if args.help:
        print('help')

    if args.file:
        # file name users.csv
        file_name = args.file
        print('file')
    else:
        print('File must be provided')

    if args.dry_run:
        # file name users.csv
        file_name = args.file
        user_upload.cleanFile(file_name)
        print('dry_run')
    else:
        print('File must be provided')
