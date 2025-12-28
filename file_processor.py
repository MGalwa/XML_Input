# Magdalena Galwa
# 15/10/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
    # Define your input format (one or many records)
    # Default folder or user provided file path
    # Remove file if it was successfully processed


# Imported files
import feed_types

# Import statements
import os  # Provides functions to interact with the operating system (e.g., file operations)
from datetime import datetime  # Used for working with dates and times

# The FileProcessor class handles reading and validating data from TXT files
class FileProcessor:
    def __init__(self):
        # Paths to the input and output files
        self.input_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\XML_Input\input.txt"
        self.output_file_path = "output.txt"  # Path to the main output file

    def create_input_file(self, choice):
        # Create an input TXT file with an example based on the user's category choice
        examples = {
            1: "Today it's raining. Take your umbrella.;Gliwice",  # Example for News
            2: "I want to sell a bike;2026-02-02",  # Example for Private Ad
            3: "This book is amazing. Excellent storytelling.;5"  # Example for Book Review
        }

        # Check if the directory for the file exists, and create it if not
        input_dir = os.path.dirname(self.input_file_path)  # Get the directory path
        os.makedirs(input_dir, exist_ok=True)  # Ensure the directory exists

        # If the file does not already exist, create it and add an example
        if not os.path.exists(self.input_file_path):
            with open(self.input_file_path, "w", encoding="utf-8") as file:
                file.write("# Add your records here.\n")  # Add a comment at the top of the file
                file.write(f"# Example for this category: {examples[choice]}\n")  # Add an example based on the chosen type
                print(f"Input file '{self.input_file_path}' has been created. Please fill it with data.")

    def normalize_text(self, text, capitalize_all_words=False):
        # Normalize the input text (convert to lowercase, capitalize appropriately)
        normalized_text = text.lower()  # Convert to lowercase
        result = ""  # Initialize an empty string for the normalized text
        capitalize_next = True  # Flag for capitalization

        # Process each character in the text
        for i, char in enumerate(normalized_text):
            if capitalize_next and char.isalpha():  # Capitalize the next alphabetic character
                result += char.upper()
                capitalize_next = False  # Reset the flag
            else:
                result += char  # Add the character unchanged

            # Capitalize after punctuation marks
            if char in [".", "!", "?"]:  # Check for end-of-sentence punctuation
                capitalize_next = True  # Prepare to capitalize the next character

            # Capitalize after spaces (if requested)
            elif capitalize_all_words and char == " ":
                capitalize_next = True

        return result  # Return the normalized text

    def read_and_validate_records(self, choice):
        # Read and validate records from the input TXT file based on the user's choice
        records = []  # List to hold validated records

        # Check if the input file exists
        if not os.path.exists(self.input_file_path):
            print("Input file not found. Please ensure the file exists.")
            return None

        # Read non-empty lines and skip commented lines
        with open(self.input_file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines() if line.strip() and not line.startswith("#")]

        # Ensure the file contains valid data
        if not lines:
            print("Input file is empty. Please provide valid records.")
            return None

        # Process each line in the file
        for line in lines:
            try:
                parts = line.split(";")  # Split the line using `;` as a delimiter
                if choice == 1 and len(parts) == 2:  # News category
                    text = self.normalize_text(parts[0])  # Normalize the text
                    city = self.normalize_text(parts[1], capitalize_all_words=True)  # Normalize the city
                    records.append(feed_types.News(text, city))  # Create a News object
                elif choice == 2 and len(parts) == 2:  # Private Ad category
                    text = self.normalize_text(parts[0])  # Normalize the text
                    expire_date = datetime.strptime(parts[1], "%Y-%m-%d").date()  # Parse the expiration date
                    if expire_date <= datetime.now().date():
                        raise ValueError("Expiration date must be a future date.")  # Validate the expiration date
                    records.append(feed_types.AdPrivate(text, expire_date))  # Create an AdPrivate object
                elif choice == 3 and len(parts) == 2:  # Book Review category
                    text = self.normalize_text(parts[0])  # Normalize the text
                    rate = int(parts[1])  # Convert the rating to an integer
                    if rate < 1 or rate > 5:  # Validate the rating range
                        raise ValueError("Rate must be between 1 and 5.")
                    records.append(feed_types.BookReview(text, rate))  # Create a BookReview object
                else:
                    raise ValueError("Invalid format or missing fields.")  # Handle incorrect formats
            except Exception as e:
                print(f"Error processing line '{line}': {e}")
                return None

        return records  # Return the list of validated records