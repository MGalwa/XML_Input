# Magdalena Galwa
# 26/11/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
    # 1. Different types of records require different data tables
    # 2. New record creates new row in data table
    # 3. Implement “no duplicate” check.

# Imported files
import feed_types

# Import statements
import os  # Provides functions to interact with the operating system (e.g., file operations)
from datetime import datetime  # Used for working with dates and times
import json  # Allows JSON file processing (reading and writing)

# The JsonProcessor class handles reading, validating, and converting data from JSON files
class JsonProcessor:
    def __init__(self):
        # Define the path to the JSON input file
        self.json_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.json"

        # Define default JSON structures for all record types
        self.default_json_structure_news = {
            "records": [
                {"text": "Example: Today it's sunny!", "city": "Gliwice"},  # Placeholder for News
                {"text": "Example: Today it's rainy!", "city": "Katowice"}  # Additional example
            ]
        }
        self.default_json_structure_private_ad = {
            "records": [
                {"text": "Example: I'm selling a bike!", "date": "2025-12-12"},  # Placeholder for Private Ad
                {"text": "Example: I'm selling a cat!", "date": "2025-12-15"}  # Additional example
            ]
        }
        self.default_json_structure_book_review = {
            "records": [
                {"text": "Harry Potter is amazing!", "rate": 5},  # Placeholder for Book Review
                {"text": "LOTR is the best book!", "rate": 4}  # Additional example
            ]
        }

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

    def initialize_json_file(self, choice_feed_type):
        # Create a default JSON file if it doesn't already exist
        if not os.path.exists(self.json_file_path):
            with open(self.json_file_path, "w", encoding="utf-8") as file:
                if choice_feed_type == 1:  # News
                    json.dump(self.default_json_structure_news, file, indent=4)  # Write default News structure
                elif choice_feed_type == 2:  # Private Ad
                    json.dump(self.default_json_structure_private_ad, file, indent=4)  # Write default Private Ad structure
                elif choice_feed_type == 3:  # Book Review
                    json.dump(self.default_json_structure_book_review, file, indent=4)  # Write default Book Review structure
                print(f"Created a new JSON file: {self.json_file_path}\n")  # Notify the user
        else:
            print(f"JSON file already exists at: {self.json_file_path}\n")  # Notify if the file already exists

    def read_and_validate_records_json(self, choice_feed_type):
        # Read and validate data from the JSON file
        records = []  # List to store validated and converted objects

        if not os.path.exists(self.json_file_path):
            print("JSON file not found. Please ensure the file exists.")  # Error if JSON file is missing
            return None

        with open(self.json_file_path, "r", encoding="utf-8") as file:
            try:
                json_data = json.load(file)  # Load and parse the JSON file
            except json.JSONDecodeError as e:
                print(f"Invalid JSON file format: {e}")  # Handle invalid JSON format
                return None

        if not json_data.get("records"):  # Check if the "records" key exists and contains data
            print("JSON file is empty. Please provide valid records.")
            return None

        # Convert each record into the appropriate object type
        for record in json_data["records"]:
            try:
                if choice_feed_type == 1:  # News
                    text = self.normalize_text(record["text"])  # Normalize the text field
                    city = self.normalize_text(record["city"], capitalize_all_words=True)  # Normalize the city field
                    records.append(feed_types.News(text, city))  # Convert to a News object
                elif choice_feed_type == 2:  # Private Ad
                    text = self.normalize_text(record["text"])  # Normalize the text field
                    expire_date = datetime.strptime(record["date"],
 "%Y-%m-%d").date()  # Parse the expiration date
                    if expire_date <= datetime.now().date():  # Verify the date is in the future
                        raise ValueError("Expiration date must be in the future.")
                    records.append(feed_types.AdPrivate(text, expire_date))  # Convert to an AdPrivate object
                elif choice_feed_type == 3:  # Book Review
                    text = self.normalize_text(record["text"])  # Normalize the text field
                    rate = int(record["rate"])  # Parse the rate
                    if rate < 1 or rate > 5:  # Ensure the rate is between 1 and 5
                        raise ValueError("Rate must be between 1 and 5.")
                    records.append(feed_types.BookReview(text, rate))  # Convert to a BookReview object
            except Exception as e:
                print(f"Error processing record: {record}. Error: {e}")  # Handle parsing or validation errors
                return None

        return records  # Return the list of validated and converted records