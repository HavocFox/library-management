class Author:
    all_authors = {}
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getter methods for private attributes
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    # Add an author (Based on input from Operations) ------------------------
    @classmethod
    def add_author(self, name1, bio1):

        if name1 in self.all_authors:
            print("This author is already in the database.\n")
            return
        else:
            pass
        new_auth = Author(name1, bio1)       # Create a new Author object
        self.all_authors[name1] = new_auth                      # Add the Author to the dictionary with name as key

        #print("Author added successfully! /n")

    # Display author details ------------------------------------------------------
    def auth_details():
        auth_choice = input("What author do you want to view the details of? ")
        if auth_choice in Author.all_authors:
            cur_auth = Author.all_authors[auth_choice]
            print(f"Name: {cur_auth.get_name()}\nBiography: {cur_auth.get_biography()}\n")
        else:
            print("That author has no details in our database.\n")


    # Display all authors ------------------------------------------------------
    def display_authors():
        print("\nDisplaying all authors:")
        if Author.all_authors:
            for name, auth in Author.all_authors.items():
                print(f"Name: {auth.get_name()}\nBiography: {auth.get_biography()}\n")
        else:
            print("There aren't any authors in the database.\n")