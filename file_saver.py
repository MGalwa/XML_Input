# Magdalena Galwa
# 26/11/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
    # 1. Different types of records require different data tables
    # 2. New record creates new row in data table
    # 3. Implement “no duplicate” check.

# Import statements
import os  # Provides functions to interact with the operating system (e.g., file operations)

# The FileSaver class handles saving records to the output file
class FileSaver:
    def __init__(self):
        # Path to the output file where records will be saved
        self.output_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\output.txt"

    def save_parameters(self, record):
        # Save a single record to the output file
        # If the file does not exist, create it and add the application header
        if not os.path.exists(self.output_file_path):
            with open(self.output_file_path, "w", encoding="utf-8") as file:
                file.write("News Feed App\n\n")  # Add the application title with extra space

        # Append the record (formatted) to the output file
        with open(self.output_file_path, "a", encoding="utf-8") as file:
            file.write(str(record))  # Use the __str__ method to format the record
        print(f"Record has been successfully saved to '{self.output_file_path}'.")

    def save_input_parameters(self, records):
        # Save multiple validated records to the output file
        # If the file does not exist, create it and add the application header
        if not os.path.exists(self.output_file_path):
            with open(self.output_file_path, "w", encoding="utf-8") as file:
                file.write("News Feed App\n\n")  # Add the application title with extra space

        # Append every record to the file
        with open(self.output_file_path, "a", encoding="utf-8") as file:
            for record in records:
                file.write(str(record))  # Use the __str__ method for formatting
        print(f"All records have been saved to '{self.output_file_path}'.")

    def remove_txt_file(self):
        # Delete the input TXT file after processing
        file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.txt"
        try:
            os.remove(file_path)  # Remove the file from the directory
            print(f"Input TXT file '{file_path}' has been successfully deleted.")
        except Exception as e:  # Handle any errors during removal
            print(f"Error deleting the input file: {e}")

    def remove_json_file(self):
        # Delete the input JSON file after processing
        file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.json"
        try:
            os.remove(file_path)  # Remove the file from the directory
            print(f"Input JSON file '{file_path}' has been successfully deleted.")
        except Exception as e:  # Handle any errors during removal
            print(f"Error deleting the input file: {e}")

    def remove_xml_file(self):
        # Delete the input XML file after processing
        file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.xml"
        try:
            os.remove(file_path)  # Remove the file from the directory
            print(f"Input XML file '{file_path}' has been successfully deleted.")
        except Exception as e:  # Handle any errors during removal
            print(f"Error deleting the input file: {e}")