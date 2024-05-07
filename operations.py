
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
                if len(isbn) not in (10, 13) or not isbn.isdigit():
                    print("Please enter a valid ISBN.")
                else:
                    break

        genre = input("Please enter the book's genre. ")
        while True:
                pubdate = input("Please enter the book's publication date (YYYY-MM-DD). ")
                if not re.match(r"\d{4}-\d{2}-\d{2}$", pubdate):
                    print("Please enter a valid date in the format YYYY-MM-DD.")
                else:
                     break

        print("Adding book... \n")
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


        print("Adding user... \n")
        User.add_user(name, userid)

    # Refer to user.py for display users and display current user details.

    #--------------------------------------------------------------
    # AUTHOR OPERATIONS ----------------------------------------------
    # Add an author:
    def add_author():
        name = input("Please enter the author's name. ")
        authorbio = input("Please enter the author's biography. ")


        print("Adding author... \n")
        Author.add_author(name, authorbio)

    # Refer to author.py for display authors and display author details.

from menu import Menu
from book import Book
from author import Author
from user import User