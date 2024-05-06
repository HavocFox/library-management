class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.available = True

    # Getter and setter for availability
    def is_available(self):
        return self.available

    def set_availability(self, status):
        self.available = status