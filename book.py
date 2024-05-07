class Book:
    all_books = {}
    def __init__(self, title, author, isbn, genre, pubdate):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.pubdate = pubdate
        self.avail = True

    # Getter for availability -------------------------------------------
    def is_available(self):
        return self.avail

   # Setter for availability --------------------------------------------
    def set_availability(self, status):
        self.avail = status


   # Add a book (Based on input from Operations) ------------------------
    @classmethod
    def add_book(self, title1, author1, isbn1, genre1, pubdate1):

        if title1 in self.all_books:
            print("Book with the same title already exists!\n")
            return
        new_book = Book(title = title1, author = author1, isbn = isbn1, genre = genre1, pubdate = pubdate1)  # Create a new Book object
        self.all_books[title1] = new_book  # Add the book to the dictionary with title as key

        if User.first_user == False:
            print("Book added successfully!\n")

    # Borrow a book ------------------------------------------------------
    def borrow_book():
        print("Which book would you like to borrow? ")
        book_title = input("Please enter its title: ")

        if book_title in Book.all_books:
            book = Book.all_books[book_title]
            if book.is_available():
                book.set_availability(False)  # Mark the book as borrowed
                User.all_users[User.current_user].borrowed_books.append(book_title)  # Append the title of the book to the list of borrowed books
                print(f"{book_title} has been borrowed.\n")
            else:
                print(f"{book_title} has already been borrowed.\n")
        else:
            print(f"'{book_title}' is not in the library.\n")

    # Return a book ------------------------------------------------------
    def return_book():
        print("Which book would you like to return? ")
        book_title = input("Please enter its title: ")

        if book_title in Book.all_books:
            book = Book.all_books[book_title]
            if not book.is_available():
                if book_title in User.all_users[User.current_user].borrowed_books:          # Did the current user actually borrow this book?
                    book.set_availability(True)                             # Mark the book as returned.
                    User.all_users[User.current_user].borrowed_books.remove(book)           # Remove the book object from the list of borrowed books
                    print(f"{book_title} has been returned.\n")
                else:
                    print("Another user borrowed this book. To return it, please switch to that user. ")
            else:
                print(f"{book_title} has already been returned.\n")
        else:
            print(f"'{book_title}' is not in the library.\n")

    # Search for a book ------------------------------------------------------
    def search_book():
        book_title = input("Please enter the title of the book you'd like to search for: ")

        if Book.all_books:
            print("Found it! Here's its info: ")
            if book_title in Book.all_books:
                    book = Book.all_books[book_title]
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Publication Date: {book.pubdate}, Is it available? {book.is_available()}\n")
        else:
            print(f"'{book_title}' is not in the library.\n")

    # Search for a book ------------------------------------------------------
    def display_book():
        print("\nDisplaying all books: ")
        if Book.all_books:
            for title, book in Book.all_books.items():
                print(f"Title: {title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Publication Date: {book.pubdate}, Is it available? {book.is_available()}\n")
        else:
            print("There aren't any books in the library.\n")

from user import User