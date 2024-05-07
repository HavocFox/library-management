class Author:
    all_authors = {}
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    # Add an author (Based on input from Operations) ------------------------
    @classmethod
    def add_author(self, name1, bio1):

        if name1 in self.all_authors:
            print("This author is already in the database.\n")
            return
        else:
            pass
        new_auth = Author(name = name1, biography = bio1)       # Create a new Author object
        self.all_authors[name1] = new_auth                      # Add the Author to the dictionary with name as key

        print("Author added successfully! /n")

    # Display author details ------------------------------------------------------
    def auth_details():
        authchoice = input("What author do you want to view the details of? ")
        if authchoice in Author.all_authors:
            curauth = Author.all_authors[authchoice]
            print(f"Name: {curauth.name}, Biography: {curauth.biography} \n")
        else:
           print("That author has no details in our database.\n")


    # Display all authors ------------------------------------------------------
    def display_authors():
        print("\nDisplaying all authors:")
        if Author.all_authors:
            for name, auth in Author.all_authors.items():
                print(f"Name: {name}\nBiography: {auth.biography}\n")
        else:
            print("There aren't any authors in the database.\n")