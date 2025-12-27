# Magdalena Galwa
# 26/11/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
    # 1. Different types of records require different data tables
    # 2. New record creates new row in data table
    # 3. Implement “no duplicate” check.

#Imported files
import gui

# The User class manages user input and selections
class User:
    def __init__(self):
        self.gui = gui.GUI()  # Initialize the GUI for user interaction
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
            print(r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.txt")
            print("After filling the file, you can process it.")  # Instruct the user to fill the file
        elif self.choice_input_type == 2:  # TXT file input
            print("\nA default input file will be created in:")  # Inform the user about the file path
            print(r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\DB_Input\input.txt")
            print("After filling the file, you can process it.")  # Instruct the user to fill the file
