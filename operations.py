
import re

# This module is used for operations that take input or are more complicated to run inside the respective classes.

class Operations:
# BOOK OPERATIONS ----------------------------------------------
    # Add a book:
    def add_book():
        title = input("Please enter the book's title. ")
        author = input("Please enter the book's author. ")
        while True:
                isbn = input("Please enter the book's ISBN. ")
                if len(isbn) != 10 and len(isbn) != 13:
                    print("Please enter a valid ISBN.")
                if isbn.isdigit():
                    if len(isbn) == 10 or len(isbn) == 13:
                        break
                else:
                    print("Please enter a valid ISBN.")

        genre = input("Please enter the book's genre. ")
        while True:
                pubdate = input("Please enter the book's publication date (YYYY-MM-DD). ")
                if not re.match(r"\d{4}-\d{2}-\d{2}$", pubdate):
                    print("Please enter a valid date in the format YYYY-MM-DD.")
                else:
                     break

        print("Adding book... ")
        Book.add_book(title, author, isbn, genre, pubdate)

    # Borrow a book: > Refer to book.py.
    # Return a book: > Refer to book.py.
    # Search for a book: > Refer to book.py.
    # Display books: > Refer to book.py.

    #--------------------------------------------------------------
    # USER OPERATIONS ----------------------------------------------
    # Add a user:
    def add_user():
        name = input("Please enter the user's name. ")
        userid = input("Please enter the user's library ID. ")


        print("Adding book... ")
        User.add_user(name, userid)

    # Borrow a book: > Refer to book.py.
    # Return a book: > Refer to book.py.
    # Search for a book: > Refer to book.py.
    # Display books: > Refer to book.py.

from menu import Menu
from book import Book
from author import Author
from user import User