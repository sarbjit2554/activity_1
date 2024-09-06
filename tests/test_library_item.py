"""
Description: Unit tests for the LibraryItem class.
Author: Sarbjit Singh
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_item.py
"""

import unittest
from library_item.library_item import LibraryItem  
from genre.genre import Genre  






class TestLibraryItem(unittest.TestCase):
    
    def test_init_with_valid_data(self):
        """Test initializing with valid title, author, and genre."""
        item = LibraryItem("Sample Title", "Sample Author", Genre.FICTION)
        self.assertEqual(item._LibraryItem__title, "Sample Title")
        self.assertEqual(item._LibraryItem__author, "Sample Author")
        self.assertEqual(item._LibraryItem__genre, Genre.FICTION)

    def test_init_blank_title_raises_exception(self):
        """Test that a blank title raises a ValueError."""
        with self.assertRaises(ValueError):
            LibraryItem("", "Sample Author", Genre.FICTION)

    def test_init_blank_author_raises_exception(self):
        """Test that a blank author raises a ValueError."""
        with self.assertRaises(ValueError):
            LibraryItem("Sample Title", "", Genre.FICTION)

    def test_init_invalid_genre_raises_exception(self):
        """Test that an invalid genre raises a ValueError."""
        with self.assertRaises(ValueError):
            LibraryItem("Sample Title", "Sample Author", "Invalid Genre")
    
    def test_title_property(self):
        """Test title property getter and setter."""
        item = LibraryItem("Sample Title", "Sample Author", Genre.FICTION)
        self.assertEqual(item.title, "Sample Title")
        item.title = "New Title"
        self.assertEqual(item.title, "New Title")

    def test_author_property(self):
        """Test author property getter and setter."""
        item = LibraryItem("Sample Title", "Sample Author", Genre.FICTION)
        self.assertEqual(item.author, "Sample Author")
        item.author = "New Author"
        self.assertEqual(item.author, "New Author")

    def test_genre_property(self):
        """Test genre property getter and setter."""
        item = LibraryItem("Sample Title", "Sample Author", Genre.FICTION)
        self.assertEqual(item.genre, Genre.FICTION)
        item.genre = Genre.NONFICTION
        self.assertEqual(item.genre, Genre.NONFICTION)

if __name__ == '__main__':
    unittest.main()

