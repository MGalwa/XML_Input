# Magdalena Galwa
# 15/10/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
    # Define your input format (one or many records)
    # Default folder or user provided file path
    # Remove file if it was successfully processed

from datetime import datetime

# Imported files
import user
import feed_types
import file_processor
import file_saver
import json_file
import xml_file

# Main execution logic for the program
if __name__ == "__main__":
    user = user.User()  # Create a User object to handle user input and choices
    file_saver = file_saver.FileSaver()  # Create a FileSaver object for handling file operations

    try:
        if user.choice_input_type == 1:  # Input data from the console
            # Based on the user's feed type choice, create the appropriate record and save it
            if user.choice_feed_type == 1:  # News Feed
                record = feed_types.News(user.data["text"], user.data["city"])
            elif user.choice_feed_type == 2:  # Private Ad
                record = feed_types.AdPrivate(user.data["text"], user.data["expire_date"])
            elif user.choice_feed_type == 3:  # Book Review
                record = feed_types.BookReview(user.data["text"], user.data["rate"])
            else:
                print("Invalid choice. Exiting.")  # Exit if an invalid choice is somehow entered
                exit()
            # Save the record to the output file
            file_saver.save_parameters(record)

        elif user.choice_input_type == 2:  # Input data from TXT file
            processor = file_processor.FileProcessor()  # Initialize FileProcessor for handling input files
            processor.create_input_file(user.choice_feed_type)  # Create a TXT file for input data

            while True:
                # Prompt the user to process the TXT file or exit
                print("\nType '1' to process the TXT input file after filling it.")
                print("Type '2' to exit the application.")
                user_action = input("Your choice: ").strip()

                if user_action == "1":  # Process the TXT file
                    records = processor.read_and_validate_records(user.choice_feed_type)  # Read and validate records
                    if records:  # If valid records were read
                        file_saver.save_input_parameters(records)  # Save them to the output file
                        file_saver.remove_txt_file()  # Delete the TXT file after processing
                        print("Processing completed. Exiting the application.")  # Notify completion
                        break  # Exit the loop
                    else:
                        print("No valid records found. Please fix the TXT input file.")  # Notify validation failure
                elif user_action == "2":  # Exit the program
                    print("Exiting application.")
                    break
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Handle invalid user input

        elif user.choice_input_type == 3:  # Input data from JSON file
            JSprocessor = json_file.JsonProcessor()  # Initialize JsonProcessor for JSON file handling
            JSprocessor.initialize_json_file(user.choice_feed_type)  # Create a JSON file for input data

            while True:
                # Prompt the user to process the JSON file or exit
                print("\nType '1' to process the input JSON file after filling it.")
                print("Type '2' to exit the application.")
                user_action = input("Your choice: ").strip()

                if user_action == "1":  # Process the JSON file
                    records = JSprocessor.read_and_validate_records_json(user.choice_feed_type)  # Read and validate records
                    if records:  # If valid records were read
                        file_saver.save_input_parameters(records)  # Save them to the output file
                        file_saver.remove_json_file()  # Delete the JSON file after processing
                        print("Processing completed. Exiting the application.")  # Notify completion
                        break  # Exit the loop
                    else:
                        print("No valid records found. Please fix the input JSON file.")  # Notify about validation failure
                elif user_action == "2":  # Exit the program
                    print("Exiting application.")
                    break
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Handle invalid user input

        elif user.choice_input_type == 4:  # Input data from XML file
            XMLprocessor = xml_file.XMLProcessor()  # Initialize XMLProcessor for XML: file handling
            XMLprocessor.initialize_xml_file(user.choice_feed_type)  # Create a XML file for input data

            while True:
                # Prompt the user to process the XML file or exit
                print("\nType '1' to process the input XML file after filling it.")
                print("Type '2' to exit the application.")
                user_action = input("Your choice: ").strip()

                if user_action == "1":  # Process the XML file
                    records = XMLprocessor.read_and_validate_records_xml(user.choice_feed_type)  # Read and validate records
                    if records:  # If valid records were read
                        file_saver.save_input_parameters(records)  # Save them to the output file
                        file_saver.remove_xml_file()  # Delete the XML file after processing
                        print("Processing completed. Exiting the application.")  # Notify completion
                        break  # Exit the loop
                    else:
                        print("No valid records found. Please fix the input XML file.")  # Notify about validation failure
                elif user_action == "2":  # Exit the program
                    print("Exiting application.")
                    break
                else:
                    print("Invalid input. Please enter '1' or '2'.")  # Handle invalid user input

    except Exception as e:
        # Catch all unexpected exceptions and print the error message
        print(f"An error occurred: {e}")