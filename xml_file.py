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
import xml.etree.ElementTree as ET  # Allows XML file processing (reading and writing)

# The XMLProcessor class handles reading, validating, and converting data from XML files
class XMLProcessor:
    def __init__(self):
        # Define the path to the XML input file
        self.xml_file_path = r"C:\Users\MagdalenaGalwa\Desktop\Nauka\Python\Python_Projects\XML_Input\input.xml"

        # Define default XML structures for all record types

        # Create default structure for News
        root_news = ET.Element("records")
        child1_news = ET.SubElement(root_news, "record", text="Example: Today it's sunny!", city="Gliwice")
        child2_news = ET.SubElement(root_news, "record", text="Example: Today it's rainy!", city="Katowice")
        self.default_xml_structure_news = ET.ElementTree(root_news)

        # Create default structure for Private Ad
        root_private_ad = ET.Element("records")
        child1_private_ad = ET.SubElement(root_private_ad, "record", text="Example: I'm selling a bike!", date="2025-12-12")
        child2_private_ad = ET.SubElement(root_private_ad, "record", text="Example: I'm selling a cat!", date="2025-12-15")
        self.default_xml_structure_private_ad = ET.ElementTree(root_private_ad)

        # Create default structure for Book Review
        root_book_review = ET.Element("records")
        child1_book_review = ET.SubElement(root_book_review, "record", text="Harry Potter is amazing!", rate="5")
        child2_book_review = ET.SubElement(root_book_review, "record", text="LOTR is the best book!", rate="4")
        self.default_xml_structure_book_review = ET.ElementTree(root_book_review)

    def initialize_xml_file(self, choice_feed_type):
        # Create a default XML file if it doesn't already exist
        if not os.path.exists(self.xml_file_path):
            if choice_feed_type == 1:
                self.default_xml_structure_news.write(self.xml_file_path, encoding='utf-8', xml_declaration=True)
            elif choice_feed_type == 2:
                self.default_xml_structure_private_ad.write(self.xml_file_path, encoding='utf-8', xml_declaration=True)
            elif choice_feed_type == 3:
                self.default_xml_structure_book_review.write(self.xml_file_path, encoding='utf-8', xml_declaration=True)
            print(f"Created a new XML file: {self.xml_file_path}\n")  # Notify the user
        else:
            print(f"XML file already exists at: {self.xml_file_path}\n")  # Notify if the file already exists

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

    def read_and_validate_records_xml(self, choice_feed_type):
        # Check if the XML file exists
        if not os.path.exists(self.xml_file_path):
            print("XML file not found. Please ensure the file exists.")
            return None

        try:
            # Parse the XML file
            tree = ET.parse(self.xml_file_path)
            # Get the root element
            root = tree.getroot()
        except ET.ParseError as e:
            # Handle invalid XML format
            print(f"Invalid XML file format: {e}")
            return None

        records = []  # List to store validated and converted objects

        # Check if the root element is <records>
        if root.tag != "records":
            print("Invalid XML structure. Root element should be <records>.")
            return None

        # Iterate over each <record> element
        for record_elem in root.findall("record"):
            try:
                # Get the 'text' attribute
                text = record_elem.get("text")
                if not text:
                    # Handle missing 'text' attribute
                    raise ValueError("Missing 'text' attribute in record.")

                if choice_feed_type == 1:  # News
                    # Get the 'city' attribute
                    city = record_elem.get("city")
                    if not city:
                        # Handle missing 'city' attribute
                        raise ValueError("Missing 'city' attribute for News record.")
                    # Normalize text and city
                    norm_text = self.normalize_text(text)  # Normalize the text field
                    norm_city = self.normalize_text(city, capitalize_all_words=True)  # Normalize the city field
                    # Create a News object and add to the list
                    records.append(feed_types.News(norm_text, norm_city))

                elif choice_feed_type == 2:  # Private Ad
                    # Get the 'date' attribute
                    date_str = record_elem.get("date")
                    if not date_str:
                        # Handle missing 'date' attribute
                        raise ValueError("Missing 'date' attribute for Private Ad record.")
                    # Parse the expiration date
                    expire_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    # Check if the expiration date is in the future
                    if expire_date <= datetime.now().date():
                        raise ValueError("Expiration date must be in the future.")
                    # Normalize text
                    norm_text = self.normalize_text(text)  # Normalize the text field
                    # Create an AdPrivate object and add to the list
                    records.append(feed_types.AdPrivate(norm_text, expire_date))

                elif choice_feed_type == 3:  # Book Review
                    # Get the 'rate' attribute
                    rate_str = record_elem.get("rate")
                    if not rate_str:
                        # Handle missing 'rate' attribute
                        raise ValueError("Missing 'rate' attribute for Book Review record.")
                    # Convert the rate to integer
                    rate = int(rate_str)
                    # Check if the rate is between 1 and 5
                    if rate < 1 or rate > 5:
                        raise ValueError("Rate must be between 1 and 5.")
                    # Normalize text
                    norm_text = self.normalize_text(text)  # Normalize the text field
                    # Create a BookReview object and add to the list
                    records.append(feed_types.BookReview(norm_text, rate))

            except Exception as e:
                # Handle errors during record processing
                print(f"Error processing record: {ET.tostring(record_elem, encoding='unicode')}. Error: {e}")
                return None

        # Return the list of validated and converted records
        return records