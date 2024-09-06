"""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

from library_item import LibraryItem  # Correct import statement

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # 1. Create an instance of the LibraryItem class with valid inputs
    try:
        valid_item = LibraryItem(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
        print("Valid LibraryItem created successfully.")
    except Exception as e:
        print(f"An error occurred while creating a valid LibraryItem: {e}")

    # 2. Print each of the attributes of the LibraryItem instance
    try:
        print(f"Title: {valid_item.get_title()}")
        print(f"Author: {valid_item.get_author()}")
        print(f"Genre: {valid_item.get_genre()}")
    except Exception as e:
        print(f"An error occurred while accessing attributes of the LibraryItem: {e}")

    # 3. Create an instance of the LibraryItem class with invalid inputs
    try:
        invalid_item = LibraryItem(title="Invalid Item", author="Unknown", genre="")
    except Exception as e:
        print(f"An error occurred while creating a LibraryItem with invalid inputs: {e}")

if __name__ == "__main__":
    main()
