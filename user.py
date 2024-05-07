class User:
    all_users = {}
    current_user = "default"
    first_user = True
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    # Add a user (Based on input from Operations) ------------------------
    @classmethod
    def add_user(self, name1, userid1):

        if name1 in self.all_users:
            user_switch = input("This user already exists. Would you like to switch to this user? Y or N. ").upper()
            if user_switch == 'Y':
                print(f"User switched to {name1}.\n")
                User.current_user = name1
                return
        new_user = User(name = name1, library_id = userid1)  # Create a new Book object
        self.all_users[name1] = new_user  # Add the book to the dictionary with title as key

        print("User added successfully!\n")
        if User.first_user == True:                     # Checking if this is the first logged in User - AKA, don't ask to switch if there's no one to switch to
            User.first_user = False                     # Now we can switch if this is called again
            return
        else:
            switchchoice = input("Would you like to switch to this user? Y or N. ").upper()
            if switchchoice == 'Y':
                print(f"User switched to {name1}.\n")
                User.current_user = name1

                return
            else:
                return

    # Display user details ------------------------------------------------------
    def user_details():
        print("Viewing details of current user:")
        if User.current_user in User.all_users:
            curuser = User.all_users[User.current_user]
            print(f"Name: {curuser.name}, Library ID: {curuser.library_id} \nBooks borrowed:")
            if curuser.borrowed_books:
                for book in curuser.borrowed_books:
                    print(book)
            else:
                print("None borrowed")
        else:
           print("Current user does not exist.")


    # Search for a book ------------------------------------------------------
    def display_users():
        print("\nDisplaying all users:")
        if User.all_users:
            for name, user in User.all_users.items():
                print(f"Name: {name}, Library ID: {user.library_id}\nBooks borrowed:")
                if user.borrowed_books:
                    for book in user.borrowed_books:
                        print(book)
                else:
                    print("None borrowed")
                print()  # Add an empty line between users for better readability
        else:
            print("There aren't any users.\n")  # Realistically this would never trigger, though

