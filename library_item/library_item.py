"""
    Description: A class to manage LibraryItem objects.
    Author: Sarbjit Singh
    Date: {Date}
"""
from genre.genre import Genre  # Import the Genre enumeration

class LibraryItem:
    """
        Brief description of the class: Represents an item in a library with a title, author, and genre.

        Attributes:
        title (str): The title of the library item.
        author (str): The author of the library item.
        genre (Genre): The Genre of the library item.
     """

    def __init__(self, title, author, genre):
        """
           Initializes a new LibraryItem with the given title, author, and genre.

           Args:
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The genre of the library item, must be a valid Genre.

          Raises:
            ValueError: If title or author is blank, or if genre is not a valid Genre.
        """
        # Strip leading and trailing spaces from title and author
        title = title.strip()
        author = author.strip()
        
        # Validate title
        if len(title) == 0:
            raise ValueError("Title cannot be blank.")
        
        # Validate author
        if len(author) == 0:
            raise ValueError("Author cannot be blank.")
        
        # Validate genre
        if genre not in Genre:
            raise ValueError("Invalid Genre.")
        
        # Initialize attributes
        self._title = title
        self._author = author
        self._genre = genre

    @property
    def title(self):
        """
         Gets the title of the library item.

         Returns:
            str: The title of the library item.
        """
        return self._title

    @title.setter
    def title(self, value):
        """
         Sets the title of the library item.

         Args:
            value (str): The new title for the library item.

         Raises:
            ValueError: If value is blank.
        """
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Title cannot be blank.")
        self._title = value

    @property
    def author(self):
        """
         Gets the author of the library item.

         Returns:
            str: The author of the library item.
        """
        return self._author

    @author.setter
    def author(self, value):
        """
         Sets the author of the library item.

         Args:
            value (str): The new author for the library item.

         Raises:
            ValueError: If value is blank.
        """
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Author cannot be blank.")
        self._author = value

    @property
    def genre(self):
        """
         Gets the genre of the library item.

         Returns:
            Genre: The genre of the library item.
        """
        return self._genre

    @genre.setter
    def genre(self, value):
        """
         Sets the genre of the library item.

         Args:
            value (Genre): The new genre for the library item.

         Raises:
            ValueError: If value is not a valid Genre.
        """
        if value not in Genre:
            raise ValueError("Invalid Genre.")
        self._genre = value
