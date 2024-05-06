

class Menu:
    @staticmethod
    def book_menu():
        print("\n----------------------------------------------------------")
        while True:
            print("Book Operations:")
            print("     1. Add a new book\n     2. Borrow a book\n     3. Return a book\n     4. Search for a book\n     5. Display all books\n     6. Back to main menu")
            try:
                bookchoice = int(input("Please enter a numeric selection. "))
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:
                if bookchoice == 1:
                    print("\nYou have chosen to add a book.")
                    Operations.add_book()
                if bookchoice == 2:
                    print("\nYou have chosen to borrow a book.")
                    Book.borrow_book()
                if bookchoice == 3:
                    print("\nYou have chosen to return a book.")
                    Book.return_book()
                if bookchoice == 4:
                    print("\nYou have chosen to search for a book.")
                    Book.search_book()
                if bookchoice == 5:
                    print("\nYou have chosen to display all books.")
                    Book.display_book()
                if bookchoice == 6:
                    return True         # Return to main menu
                if bookchoice < 1 or bookchoice > 6:
                    print("Please enter a valid numeric selection.\n")

    def user_menu():
        print("\n----------------------------------------------------------")
        print("User Operations:")
        print("     1. Add a new user\n     2. View user details\n     3. Display all users\n     4. Back to main menu")
        while True:
            try:
                userchoice = int(input("Please enter a numeric selection. "))
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:
                if userchoice == 1:
                    print("woah")
                if userchoice == 4:
                    return True         # Return to main menu
                if userchoice < 1 or userchoice > 4:
                    print("Please enter a valid numeric selection.\n")

    def author_menu():
        print("\n----------------------------------------------------------")
        print("Author Operations:")
        print("     1. Add a new author\n     2. View author details\n     3. Display all authors\n     4. Back to main menu")
        while True:
            try:
                authchoice = int(input("Please enter a numeric selection. "))
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:
                if authchoice == 1:
                    print("woah")
                if authchoice == 4:
                    return True         # Return to main menu
                if authchoice < 1 or authchoice > 4:
                    print("Please enter a valid numeric selection.\n")

    def main_menu():
        while True:
            print("\nMain Menu: \n     1. Book Operations\n     2. User Operations\n     3. Author Operations\n     4. Quit")
            try:
                mainchoice = int(input("Please enter a numeric selection. "))
            except ValueError:
                print("That is not a valid numeric selection.\n")
            else:
                if mainchoice == 1:
                    Menu.book_menu()
                if mainchoice == 2:
                    Menu.user_menu()
                if mainchoice == 3:
                    Menu.author_menu()
                if mainchoice == 4:
                    break
                if mainchoice < 1 or mainchoice > 4:
                    print("Please enter a valid numeric selection.\n")

from operations import Operations
from book import Book