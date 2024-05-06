class Menu:
    @staticmethod
    def book_menu():
        print("\nDONE DARNED ENTER THE BOOK MENU!!!!!!!!!!!!!!")
        print("Book Operations:")
        print("     1. Add a new book\n     2. Borrow a book\n     3. Return a book\n     4. Search for a book\n     5. Display all books\n     6. Back to main menu")
        while True:
            try:
                bookchoice = int(input("Please enter a numeric selection. "))
            except ValueError:
                print("Please enter a valid numeric selection.\n")
            else:
                if bookchoice == 1:
                    print("woah")
                if bookchoice == 6:
                    return True         # Return to main menu
                if bookchoice < 1 or bookchoice > 6:
                    print("Please enter a valid numeric selection.\n")

    def user_menu():
        print("\nWOW!!!! THE USER MENU!!!!!!!!!!!!!!")
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
        print("\nAUTHORS????? I BARELY KNOW HERS HAHAHAHAHAHAHEHAGSAGSJDGKASGDGASDFKJS;D")
        print("Author Operations:")
        print("     1. Add a new author\n     2. BView author details\n     3. Display all authors\n     4. Back to main menu")
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