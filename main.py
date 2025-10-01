# Magdalena Galwa
# 26/09/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
    # Define your input format (one or many records)
    # Default folder or user provided file path
    # Remove file if it was successfully processed


# Import statements
import os  # Provides functions to interact with the operating system (e.g., file operations)
from datetime import datetime  # Used for working with dates and times
import json  # Allows JSON file processing (reading and writing)

# The GUI class defines the user interface to interact with the application
class GUI:
    def __init__(self):
        # Show a welcome message and input options for the user
        print("=== News Feed Tool ===")  # Title of the application
        print("Choose how you would like to provide the data:")  # Explain input options
        print("1 - Enter data manually through the console.")  # Option 1: Manual input
        print("2 - Provide data using a TXT input file located at: C:\\Users\\MagdalenaGalwa\\Desktop\\Nauka\\Python\\Python_Projects\\JSON_Input")  # Option 2: TXT file
        print("3 - Provide data using a JSON input file located at: C:\\Users\\MagdalenaGalwa\\Desktop\\Nauka\\Python\\Python_Projects\\JSON_Input")  # Option 3: JSON file

    def get_user_choice_input_type(self):
        # Ask the user how they would like to provide the data (Console, TXT, JSON)
        while True:
            try:
                choice_input_type = int(input("Enter your choice (input type) (1, 2, 3): "))  # Get user input
                if choice_input_type in [1, 2, 3]:  # Validate that the choice is valid
                    return choice_input_type  # Return the user's selection
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")  # Error for invalid input
            except ValueError:
                print("Invalid input. Please enter the number 1, 2, or 3.")  # Handle non-integer input

    def get_user_choice_feed_type(self):
        # Ask the user to choose the type of record (News, Private Ad, or Book Review)
        print("=== News Feed Tool ===")  # Display the application title again
        print("Choose the type of news feed you would like to provide:")  # Options for feed type
        print("1 - News Feed")  # Option 1: News Feed
        print("2 - Private Ad")  # Option 2: Private Ad
        print("3 - Book Review")  # Option 3: Book Review

        while True:
            try:
                choice_feed_type = int(input("Enter your choice (feed type) (1, 2, 3): "))  # Get user's choice
                if choice_feed_type in [1, 2, 3]:  # Validate the user's input
                    return choice_feed_type  # Return the feed type
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")  # Error for invalid choice
            except ValueError:
                print("Invalid input. Please enter the number 1, 2, or 3.")  # Non-integer error handling

    def get_news_feed_params(self):
        # Collect parameters for a News Feed record
        while True:
            text = input("Enter the news text: ").strip()  # Get the main text for the news feed
            if text:  # Ensure the text is not empty
                break
            else:
                print("News text cannot be empty. Please enter valid text.")  # Error for empty input

        while True:
            city = input("Enter the city: ").strip()  # Get the city for the news feed
            if city:  # Ensure the city is not empty
                break
            else:
                print("City cannot be empty. Please enter a valid city.")  # Error for empty input

        return {"text": text, "city": city}  # Return the collected data as a dictionary

    def get_ad_params(self):
        # Collect parameters for a Private Ad
        text = input("Enter the ad text: ")  # Get the main text for the ad
        while True:
            try:
                expire_date = input("Enter the expiration date (format YYYY-MM-DD): ")  # Get the expiration date
                expire_date = datetime.strptime(expire_date, "%Y-%m-%d").date()  # Parse the date
                if expire_date > datetime.now().date():  # Ensure the date is in the future
                    return {"text": text, "expire_date": expire_date}  # Return the text and date
                else:
                    print("The expiration date must be later than today.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")  # Error for invalid date format

    def get_book_review_params(self):
        # Collect parameters for a Book Review
        text = input("Enter the book review text: ")  # Get the review text
        while True:
            try:
                rate = int(input("Rate the book (1-5): "))  # Get the book's rating
                if 1 <= rate <= 5:  # Validate the rating (must be between 1 and 5)
                    return {"text": text, "rate": rate}  # Return the text and rate
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")  # Error for invalid rating
            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 5.")  # Error for non-integer input


# The User class manages user input and selections
class User:
    def __init__(self):
        self.gui = GUI()  # Initialize the GUI for user interaction
        self.choice_input_type = self.gui.get_user_choice_input_type()  # Get the input type (console, TXT, JSON)
        self.choice_feed_type = self.gui.get_user_choice_feed_type()  # Get the feed type (News, Private Ad, Book Review)
        self.data = self.get_user_data()  # Store the user's data based on their choices

    def get_user_data(self):
        # Call the appropriate method to collect data based on input and feed type
        if self.choice_input_type == 1:  # Console input
            if self.choice_feed_type == 1:  # News Feed
                return self.gui.get_news_feed_params()  # Collect parameters for News Feed
            elif self.choice_feed_type == 2:  # Private Ad
                return self.gui.get_ad_params()  # Collect parameters for Private Ad
            elif self.choice_feed_type == 3:  # Book Review
                return self.gui.get_book_review_params()  # Collect parameters for Book Review
        elif self.choice_input_type == 2:  # TXT file input
            print("\nA default input file will be created in:")  # Inform the user about the file path
            print(r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\NewsFeed_InputFile\input.txt")
            print("After filling the file, you can process it.")  # Instruct the user to fill the file


# The News class represents a single News Feed record
class News:
    def __init__(self, text, city):
        self.text = text  # The main text of the news
        self.city = city  # The city where the news takes place
        self.timestamp = datetime.now().strftime("%d/%m/%Y")  # Automatically add the current date

    def __str__(self):
        # Return a well-formatted string representation of the news record
        return (
            "News ------------------------\n"
            f"{self.text}\n"  # Include the news text
            f"{self.city}\n"  # Include the city
            f"Published on: {self.timestamp}\n\n"  # Include the publication date with spacing
        )


# The AdPrivate class represents a single Private Ad record
class AdPrivate:
    def __init__(self, text, expire_date):
        self.text = text  # The main text of the private ad
        self.expire_date = expire_date  # Expiration date for the ad

    def __str__(self):
        # Calculate days remaining until the expiration date
        days_left = (self.expire_date - datetime.now().date()).days
        # Return a well-formatted string representation of the private ad record
        return (
            "Private Ad ------------------------\n"
            f"{self.text}\n"  # Include the private ad text
            f"Actual until: {self.expire_date}, {days_left} days left\n\n"  # Include expiration date and days left
        )


# The BookReview class represents a single Book Review record
class BookReview:
    def __init__(self, text, rate):
        self.text = text  # The main text of the book review
        self.rate = rate  # Rating given to the book
        self.publication_date = datetime.now().strftime("%d/%m/%Y")  # Automatically add current date

    def __str__(self):
        # Return a well-formatted string representation of the book review record
        return (
            "Book Review ------------------------\n"
            f"{self.text}\n"  # Include the book review text
            f"Rate: {self.rate}/5\n"  # Include the rating
            f"Published on: {self.publication_date}\n\n"  # Include the publication date with spacing
        )


# The FileSaver class handles saving records to the output file
class FileSaver:
    def __init__(self):
        # Path to the output file where records will be saved
        self.output_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\JSON_Input\output.txt"

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
        file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\JSON_Input\input.txt"
        try:
            os.remove(file_path)  # Remove the file from the directory
            print(f"Input TXT file '{file_path}' has been successfully deleted.")
        except Exception as e:  # Handle any errors during removal
            print(f"Error deleting the input file: {e}")

    def remove_json_file(self):
        # Delete the input JSON file after processing
        file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\JSON_Input\input.json"
        try:
            os.remove(file_path)  # Remove the file from the directory
            print(f"Input JSON file '{file_path}' has been successfully deleted.")
        except Exception as e:  # Handle any errors during removal
            print(f"Error deleting the input file: {e}")


# The FileProcessor class handles reading and validating data from TXT files
class FileProcessor:
    def __init__(self):
        # Paths to the input and output files
        self.input_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\JSON_Input\input.txt"
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
                    records.append(News(text, city))  # Create a News object
                elif choice == 2 and len(parts) == 2:  # Private Ad category
                    text = self.normalize_text(parts[0])  # Normalize the text
                    expire_date = datetime.strptime(parts[1], "%Y-%m-%d").date()  # Parse the expiration date
                    if expire_date <= datetime.now().date():
                        raise ValueError("Expiration date must be a future date.")  # Validate the expiration date
                    records.append(AdPrivate(text, expire_date))  # Create an AdPrivate object
                elif choice == 3 and len(parts) == 2:  # Book Review category
                    text = self.normalize_text(parts[0])  # Normalize the text
                    rate = int(parts[1])  # Convert the rating to an integer
                    if rate < 1 or rate > 5:  # Validate the rating range
                        raise ValueError("Rate must be between 1 and 5.")
                    records.append(BookReview(text, rate))  # Create a BookReview object
                else:
                    raise ValueError("Invalid format or missing fields.")  # Handle incorrect formats
            except Exception as e:
                print(f"Error processing line '{line}': {e}")
                return None

        return records  # Return the list of validated records


# The JsonProcessor class handles reading, validating, and converting data from JSON files
class JsonProcessor:
    def __init__(self):
        # Define the path to the JSON input file
        self.json_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\JSON_Input\input.json"

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
                    text = record["text"]  # Extract the text field
                    city = record["city"]  # Extract the city field
                    records.append(News(text, city))  # Convert to a News object
                elif choice_feed_type == 2:  # Private Ad
                    text = record["text"]  # Extract the text field
                    expire_date = datetime.strptime(record["date"], "%Y-%m-%d").date()  # Parse the expiration date
                    if expire_date <= datetime.now().date():  # Verify the date is in the future
                        raise ValueError("Expiration date must be in the future.")
                    records.append(AdPrivate(text, expire_date))  # Convert to an AdPrivate object
                elif choice_feed_type == 3:  # Book Review
                    text = record["text"]  # Extract the text field
                    rate = int(record["rate"])  # Parse the rate
                    if rate < 1 or rate > 5:  # Ensure the rate is between 1 and 5
                        raise ValueError("Rate must be between 1 and 5.")
                    records.append(BookReview(text, rate))  # Convert to a BookReview object
            except Exception as e:
                print(f"Error processing record: {record}. Error: {e}")  # Handle parsing or validation errors
                return None

        return records  # Return the list of validated and converted records


# Main execution logic for the program
if __name__ == "__main__":
    user = User()  # Create a User object to handle user input and choices
    file_saver = FileSaver()  # Create a FileSaver object for handling file operations

    try:
        if user.choice_input_type == 1:  # Input data from the console
            # Based on the user's feed type choice, create the appropriate record and save it
            if user.choice_feed_type == 1:  # News Feed
                record = News(user.data["text"], user.data["city"])
            elif user.choice_feed_type == 2:  # Private Ad
                record = AdPrivate(user.data["text"], user.data["expire_date"])
            elif user.choice_feed_type == 3:  # Book Review
                record = BookReview(user.data["text"], user.data["rate"])
            else:
                print("Invalid choice. Exiting.")  # Exit if an invalid choice is somehow entered
                exit()
            # Save the record to the output file
            file_saver.save_parameters(record)

        elif user.choice_input_type == 2:  # Input data from TXT file
            processor = FileProcessor()  # Initialize FileProcessor for handling input files
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
            JSprocessor = JsonProcessor()  # Initialize JsonProcessor for JSON file handling
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

    except Exception as e:
        # Catch all unexpected exceptions and print the error message
        print(f"An error occurred: {e}")