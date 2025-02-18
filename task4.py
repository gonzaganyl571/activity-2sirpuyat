class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: '{self.title}' by {self.author}, published in {self.year_published}.")

# Creating book objects
book1 = Book("Love story", "Nyl Gonzaga", 2022)
book2 = Book("Love is blind", "Nyl Gonzaga", 2023)
book3 = Book("Happines", "Nyl Gonzaga", 2024)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()