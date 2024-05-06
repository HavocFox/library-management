
from book import Book
from user import User
from author import Author
from menu import Menu





# MAIN CODE ------------------------------------
Book.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic", "1960-07-11")
Book.add_book("1984", "George Orwell", "9780451524935", "Science Fiction", "1949-06-08")
Book.add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", "Coming-of-Age", "1951-07-16")
Book.add_book("Pride and Prejudice", "Jane Austen", "9780141439518", "Romance", "1813-01-28")
Book.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427", "Fantasy", "1997-06-26")

# Ask user if they want a base library. Remove these added books later

print("Welcome to the Library Management System! ")
Menu.main_menu()


#invalid isbn on the digit side makes it print twice
# track the current user, so probably prompt to add the user before doing anything
# need to make sure users are for SURE tracking how many books they borrowed - i hope the class objects are forming correctly.
# author operations should be simple. I 'm assuming the author database is just a separate thing for the books and is specifically for containing author details
                # EX. even if an author has a book in the library that doesnt mean we know anyting about them...

                # Unrelated, but we didn't do the ECommerce thing yet.