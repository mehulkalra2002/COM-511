# Define the database using lists and tuples
books_database = [
    ("Book Title 1", "Author 1", 2005),
    ("Book Title 2", "Author 2", 2010),
    ("Book Title 3", "Author 3", 2015),
    ("Book Title 4", "Author 4", 2020)
]

# Functions to interact with the database

def display_books():
    """Display all books in the database"""
    print("Books in the database:")
    for book in books_database:
        print(f"Title: {book[0]}, Author: {book[1]}, Publication Year: {book[2]}")

def add_book(title, author, year):
    """Add a new book to the database"""
    new_book = (title, author, year)
    books_database.append(new_book)
    print(f"Book '{title}' added to the database.")

# Example usage:
display_books()

# Add a new book to the database
add_book("New Book", "New Author", 2023)

# Display all books after adding a new book
display_books()
