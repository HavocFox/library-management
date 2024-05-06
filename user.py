class User:
    all_users = {}
    current_user = "default"
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
                self.current_user = name1
                print(f"User switched to {name1}.\n")
                return
        new_user = User(name = name1, userid = userid1)  # Create a new Book object
        self.all_users[name1] = new_user  # Add the book to the dictionary with title as key

        print("User added successfully!\n")