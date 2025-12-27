# Magdalena Galwa
# 26/11/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
    # 1. Different types of records require different data tables
    # 2. New record creates new row in data table
    # 3. Implement “no duplicate” check.

# Import statements
from datetime import datetime  # Used for working with dates and times

# The GUI class defines the user interface to interact with the application
class GUI:
    def __init__(self):
        # Show a welcome message and input options for the user
        print("=== News Feed Tool ===")  # Title of the application
        print("Choose how you would like to provide the data:")  # Explain input options
        print("1 - Enter data manually through the console.")  # Option 1: Manual input
        print(r"2 - Provide data using a TXT input file located at: C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input")  # Option 2: TXT file
        print(r"3 - Provide data using a JSON input file located at: C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input")  # Option 3: JSON file
        print(r"4 - Provide data using an XML input file located at: C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input")  # Option 4: XML file
        print(r"5 - Provide data using Database connection.")  # Option 5: Database connection

    def get_user_choice_input_type(self):
        # Ask the user how they would like to provide the data (Console, TXT, JSON)
        while True:
            try:
                choice_input_type = int(input("Enter your choice (input type) (1, 2, 3, 4, 5): "))  # Get user input
                if choice_input_type in [1, 2, 3, 4, 5]:  # Validate that the choice is valid
                    return choice_input_type  # Return the user's selection
                else:
                    print("Invalid choice. Please select 1, 2, 3, 4 or 5.")  # Error for invalid input
            except ValueError:
                print("Invalid input. Please enter the number 1, 2, 3, 4 or 5")  # Handle non-integer input

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
