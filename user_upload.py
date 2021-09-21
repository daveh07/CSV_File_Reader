# ----------------------------------------- CSV READER SCRIPT ----------------------------------------------#
# 21/09/2021 - DAVID HILL
# PYTHON VERSION: 3.9
# ----------------------------------------------------------------------------------------------------------#
# Import packages and libraries
import argparse
import csv
import re

#import psycopg2

# Command line arguments
my_parser = argparse.ArgumentParser(add_help=False)
my_parser.add_argument('--file', action='store', type=str, required=True)
my_parser.add_argument('--create_table', help='create table', action='store_const', const=True)
my_parser.add_argument('--dry_run', help='dry run', action='store_const', const=True)
my_parser.add_argument('-u', help='username', action='store', type=str, )
my_parser.add_argument('-p', help='password', action='store', type=str, )
my_parser.add_argument('-h', help='host', action='store', type=str, )
my_parser.add_argument('--help', help='help', action='store_const', const=True)

# Create Command line Instances
args = my_parser.parse_args()


# Function for help command line argument
def helpFunc(hfile_name=str):
    hfile_name = fname

    print("""
    #========================================================================================================#
                                           CSV READER APPLICATION - CLI
                                                  version: 1.0
                                                    21/09/201
    #========================================================================================================#

    Please select from command list below:
    For a description of the command line directives, please type type '--help' into the command line.

    |--- FILE COMMANDS ---|
    --file [filename.csv]   "This is the name of the CSV to be parsed"
    --dry_run               "This will be used with the --file directive to run the script but not insert into 
                             the DB. All other functions will be executed, but the database won't be altered"
    --help                  "Description of command line directive details"

    |--------------------------------------- PostgreSQL Commands --------------------------------------------|
    --create_table  "This will cause the PostgreSQL users table to be built (No further action will be taken)"
    -u – PostgreSQL username
    -p – PostgreSQL password
    -h – PostgreSQL host

    #========================================================================================================#
    """)


# Function to clean the CSV file from whitespaces, tabs, special characters & validate legal email addresses
def cleanFile(file_name=str):
    file_name = fname

    with open(file_name, 'r') as csvfile:                    # Open CSV file
        csvreader = csv.reader(csvfile, delimiter=',')       # Read file using Pythons csv.reader module
        header = next(csvreader)                             # Create list for the header titles
        clean_header = []
        for i in range(len(header)):
            clean_header.append(header[i].strip())

        user_data = []                                       # Create empty list to fill with CSV row data

        # Regex for validating an Email
        regex_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'    ### TO BE REVIEWED

        # Iterate through rows in CSV readable file
        for row in csvreader:

            row_1 = row[0].title().strip()                   # Title first letter of name & remove whitespaces
            row_1 = re.sub("[^a-zA-Z'-]+", "", row_1)        # Remove any special characters by Regex

            row_2 = row[1].title().strip()                   # Title first letter of surname & remove whitespaces
            row_2 = re.sub("[^a-zA-Z'-]+", "", row_2)        # Remove any special characters by Regex

            row_3 = row[2].lower().strip()                   # Lower case letters of email & remove whitespaces

            # Validate email fields
            if re.fullmatch(regex_email, row[2]):
                row_3 = row_3
            else:
                row_3 = "Invalid Email"

            user_data.append([row_1, row_2, row_3])          # Append cleaned rows to empty user_data list

        return clean_header, user_data


if args.help:                                                # Help command line directive
    fname = args.file
    helpFunc(fname)

if args.file:                                                # File command line directive & conditionals
    fname = args.file
    if fname.endswith(".csv"):
        print(f"csv file name = '" + str(fname) + "' - File has been parsed")
    else:
        print("Error loading csv file. Check correct file format")
else:
    print('File must be provided')
    exit()

if args.create_table:                                        # Create Database Table command line & conditionals
    fname = args.file
    cleanFile(fname)
    if args.u and args.p and args.h:
        print("create table")
    else:
        print('Must provide username etc')

if args.dry_run:                                             # Dry run command line directive to clean & print file
    # process_csv(True)
    dry_run_fname = args.file
    read_csv = cleanFile(dry_run_fname)
    print(read_csv)
else:
    pass

# Function to connect to PostgreSQL database and create user table
class database_table():
    def __init__(self):
        super(database_table, self).__init__()

    def create_db_table(self, csv_file=""):
        db_name = ""
        db_user = ""
        db_host = ""
        db_password = ""

        # Connect to PostgreSQL database
        #conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)

       # cur = conn.curor()

       # cur.execute("CREATE TABLE users ( name VARCHAR, surname VARCHAR, email VARCHAR )")

      #  cur.close()

      #  conn.close()

