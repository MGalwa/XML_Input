# Magdalena Galwa
# 26/11/2025
# Description:
# Homework:
#   Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
#   1. Different types of records require different data tables
#   2. New record creates new row in data table
#   3. Implement “no duplicate” check.

from datetime import datetime  # Import datetime for date handling

import db_connection  # Import database connection module
import user  # Import user input handling module
import feed_types  # Import feed types module
import file_processor  # Import file processor module
import file_saver  # Import file saver module
import json_file  # Import JSON file handler
import xml_file  # Import XML file handler

if __name__ == "__main__":  # Main program entry point
    user_obj = user.User()  # Create a User object to handle user input and choices
    file_saver_obj = file_saver.FileSaver()  # Create a FileSaver object for handling file operations

    try:  # Start try-except block to catch unexpected errors
        if user_obj.choice_input_type == 1:  # If input is from the console
            if user_obj.choice_feed_type == 1:  # If News Feed
                record = feed_types.News(user_obj.data["text"], user_obj.data["city"])  # Create News record
            elif user_obj.choice_feed_type == 2:  # If Private Ad
                record = feed_types.AdPrivate(user_obj.data["text"], user_obj.data["expire_date"])  # Create Private Ad record
            elif user_obj.choice_feed_type == 3:  # If Book Review
                record = feed_types.BookReview(user_obj.data["text"], user_obj.data["rate"])  # Create Book Review record
            else:
                print("Invalid choice. Exiting.")  # Print error and exit if invalid choice
                exit()
            file_saver_obj.save_parameters(record)  # Save the record to file

        elif user_obj.choice_input_type == 2:  # If input is from TXT file
            processor = file_processor.FileProcessor()  # Create FileProcessor object
            processor.initialize_txt_file(user_obj.choice_feed_type)  # Initialize TXT file for input
            while True:  # Loop for user action
                print("\nType '1' to process the TXT input file after filling it.")  # Prompt user
                print("Type '2' to exit the application.")  # Prompt user
                user_action = input("Your choice: ").strip()  # Get user action
                if user_action == "1":  # If user wants to process file
                    records = processor.read_and_validate_records(user_obj.choice_feed_type)  # Read and validate records
                    if records:  # If records are valid
                        file_saver_obj.save_input_parameters(records)  # Save records
                        file_saver_obj.remove_txt_file()  # Remove TXT file
                        print("Processing completed. Exiting the application.")  # Notify user
                        break  # Exit loop
                    else:
                        print("No valid records found. Please fix the TXT input file.")  # Notify user of error
                elif user_action == "2":  # If user wants to exit
                    print("Exiting application.")  # Notify user
                    break  # Exit loop
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Notify user of invalid input

        elif user_obj.choice_input_type == 3:  # If input is from JSON file
            JSprocessor = json_file.JsonProcessor()  # Create JsonProcessor object
            JSprocessor.initialize_json_file(user_obj.choice_feed_type)  # Initialize JSON file for input
            while True:  # Loop for user action
                print("\nType '1' to process the input JSON file after filling it.")  # Prompt user
                print("Type '2' to exit the application.")  # Prompt user
                user_action = input("Your choice: ").strip()  # Get user action
                if user_action == "1":  # If user wants to process file
                    records = JSprocessor.read_and_validate_records_json(user_obj.choice_feed_type)  # Read and validate records
                    if records:  # If records are valid
                        file_saver_obj.save_input_parameters(records)  # Save records
                        file_saver_obj.remove_json_file()  # Remove JSON file
                        print("Processing completed. Exiting the application.")  # Notify user
                        break  # Exit loop
                    else:
                        print("No valid records found. Please fix the input JSON file.")  # Notify user of error
                elif user_action == "2":  # If user wants to exit
                    print("Exiting application.")  # Notify user
                    break  # Exit loop
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Notify user of invalid input

        elif user_obj.choice_input_type == 4:  # If input is from XML file
            XMLprocessor = xml_file.XMLProcessor()  # Create XMLProcessor object
            XMLprocessor.initialize_xml_file(user_obj.choice_feed_type)  # Initialize XML file for input
            while True:  # Loop for user action
                print("\nType '1' to process the input XML file after filling it.")  # Prompt user
                print("Type '2' to exit the application.")  # Prompt user
                user_action = input("Your choice: ").strip()  # Get user action
                if user_action == "1":  # If user wants to process file
                    records = XMLprocessor.read_and_validate_records_xml(user_obj.choice_feed_type)  # Read and validate records
                    if records:  # If records are valid
                        file_saver_obj.save_input_parameters(records)  # Save records
                        file_saver_obj.remove_xml_file()  # Remove XML file
                        print("Processing completed. Exiting the application.")  # Notify user
                        break  # Exit loop
                    else:
                        print("No valid records found. Please fix the input XML file.")  # Notify user of error
                elif user_action == "2":  # If user wants to exit
                    print("Exiting application.")  # Notify user
                    break  # Exit loop
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Notify user of invalid input

        elif user_obj.choice_input_type == 5:  # If input is for Database
            DB = db_connection.DBConnection('Feed.db')  # Create DB connection

            # NEWS FEED
            if user_obj.choice_feed_type == 1:  # If News Feed
                DB.create_table('Feed_News')  # Ensure table exists
                text = input("Enter news text: ")  # Get news text from user
                city = input("Enter city: ")  # Get city from user
                publish_date = datetime.today().strftime("%Y-%m-%d")  # Set publish date to today
                data = {"text": text, "city": city, "publish_date": publish_date}  # Prepare data dict

                if DB.is_duplicate('Feed_News', data):  # Check if record already exists
                    print("Duplicate record detected. This news will not be added.")  # Inform about duplicate
                else:
                    DB.insert_row('Feed_News', data)  # Insert new record
                print("\nCurrent contents of Feed_News table:")  # Show table contents
                DB.select_all('Feed_News')  # Display all records in table

            # PRIVATE AD
            elif user_obj.choice_feed_type == 2:  # If Private Ad
                DB.create_table('Feed_Private_Ad')  # Ensure table exists
                text = input("Enter ad text: ")  # Get ad text from user
                while True:  # Loop until valid date is entered
                    expire_date_input = input("Enter expiration date (DD/MM/YYYY): ")  # Get expiration date
                    try:
                        expire_date_dt = datetime.strptime(expire_date_input, "%d/%m/%Y")  # Parse date
                        today_dt = datetime.today()  # Get today's date
                        if expire_date_dt.date() < today_dt.date():  # Check if expiration date is before today
                            print("Expiration date cannot be earlier than today! Please enter a valid date.")  # Notify user
                            continue  # Ask again
                        expire_date = expire_date_dt.strftime("%Y-%m-%d")  # Format date for DB
                        break  # Exit loop if date is valid
                    except ValueError:
                        print("Invalid date format! Please enter the date as DD/MM/YYYY (e.g., 22/10/2025).")  # Notify user of format error
                data = {"text": text, "expire_date": expire_date}  # Prepare data dict

                if DB.is_duplicate('Feed_Private_Ad', data):  # Check if record already exists
                    print("Duplicate record detected. This ad will not be added.")  # Inform about duplicate
                else:
                    DB.insert_row('Feed_Private_Ad', data)  # Insert new record
                print("\nCurrent contents of Feed_Private_Ad table:")  # Show table contents
                DB.select_all('Feed_Private_Ad')  # Display all records in table

            # BOOK REVIEW
            elif user_obj.choice_feed_type == 3:  # If Book Review
                DB.create_table('Feed_Book_Review')  # Ensure table exists
                text = input("Enter book review: ")  # Get review text from user
                rate = int(input("Enter rating (e.g., 3): "))  # Get rating from user
                publish_date = datetime.today().strftime("%Y-%m-%d")  # Set publish date to today
                data = {"text": text, "rate": rate, "publish_date": publish_date}  # Prepare data dict

                if DB.is_duplicate('Feed_Book_Review', data):  # Check if record already exists
                    print("Duplicate record detected. This review will not be added.")  # Inform about duplicate
                else:
                    DB.insert_row('Feed_Book_Review', data)  # Insert new record
                print("\nCurrent contents of Feed_Book_Review table:")  # Show table contents
                DB.select_all('Feed_Book_Review')  # Display all records in table

            else:
                print("Invalid choice. Exiting.")  # Handle invalid feed type
                exit()
            DB.close()  # Close DB connection

    except Exception as e:  # Catch all unexpected exceptions
        print(f"An error occurred: {e}")  # Print error message