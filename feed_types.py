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