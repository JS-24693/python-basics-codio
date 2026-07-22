# -------------------------
# Exercise 1: import Phone and Laptop classes found in c4m4exertech.py file
# -------------------------

import c4m4exertech

my_phone = c4m4exertech.Phone("Pixel 5", "sage", 128)
my_laptop = c4m4exertech.Laptop("MacBook Pro", 15, 256)

print(my_phone) # A sage Pixel 5 with 128GB of storage.
print(my_laptop) # 15-inch MacBook Pro with 256GB of storage.


# -------------------------
# Exercise 2: extend Class for __str__ and __repr__ dunder methods
# -------------------------

class Band:
    def __init__(self, name, genre, members):
        self.name = name
        self.genre = genre
        self.members = members

    # Python's dunder method name for print() output
    def __str__(self):   
        """Human-friendly string used by print() and str()."""                                       
        return f"{self.name} is a {self.genre} band."       
    # Python's dunder method name for repr() output
    def __repr__(self):
        """Unambiguous representation useful for debugging and lists."""                                          
        return f"Band({self.name}, {self.genre}, {self.members})"  

# Instantiate values 
dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])
# Call the methods
print(dead) # calls __str__  → The Grateful Dead is a rock'n roll band.
print(repr(dead)) # calls __repr__ → Band(The Grateful Dead, rock'n roll, 
                  #                  ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])


# -------------------------
# Exercise 3: Create Dog class and add object values
# -------------------------

class Dog:
    """Demonstrate __str__ (human readable) and __repr__ (developer readable)."""
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed

    def __str__(self) -> str:
        """Human-friendly string used by print() and str()."""
        return f"{self.name} is a {self.breed}"

    def __repr__(self) -> str:
        """Unambiguous representation useful for debugging and lists."""
        return f"Dog({self.name!r}, {self.breed!r})"

dogs = [
    Dog("Marceline", "German Shepherd"),      
    Dog("Cajun",     "Belgian Malinois"),
    Dog("Daisy",     "Border Collie"),
    Dog("Rocky",     "Golden Retriever"),
    Dog("Bella",     "Irish Setter")
]
dogs.append(Dog("Fido", "Mixed Unknown"))

# printing a single object uses __str__
print(dogs[0]) # Marceline is a German Shepherd

# printing a list uses __repr__ for each element
print(repr(dogs)) # [Dog('Marceline', 'German Shepherd'), 
                  # Dog('Cajun', 'Belgian Malinois'), 
                  # Dog('Daisy', 'Border Collie'), 
                  # Dog('Rocky', 'Golden Retriever'), 
                  # Dog('Bella', 'Irish Setter')
                  # Dog('Fido', 'Mixed Unknown')]
print(dogs[0:6]) # prints the same 


# -------------------------
# Exercise 4 — composition (Library has a Book)
# -------------------------
class Book:
    """Component class representing a book."""
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __repr__(self):
        """Returns a precise object definition."""
        return f'Book({self.title}, {self.author}, {self.genre})'

class Library:
    def __init__(self):
        self.books = []
        self.fiction = []
        self.nonfiction = []
    
    def add_book(self, book):
        '''Takes a Book object and adds it to self.books'''
        self.books.append(book)
    
    def search_title(self, title):
        '''Takes a string and returns a Boolean'''
        has_book = False
        for book in self.books:
            if title.lower() == book.title.lower():
                has_book = True
        return has_book
  
    def search_author(self, author):
        '''Takes a string and returns a list of Book objects'''
        author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                author_books.append(book)
        return author_books
    
    def sort_books(self):
        '''Helper method for sort_fiction and sort_nonfiction'''
        self.fiction = self.sort_fiction()
        self.nonfiction = self.sort_nonfiction()
    
    def sort_fiction(self):
        '''Return list of Book objects where the genre is fiction'''
        fiction_books = []
        for book in self.books:
            if book.genre.lower() == 'fiction':
                fiction_books.append(book)
        return fiction_books
    
    def sort_nonfiction(self):
        '''Return list of Book objects where the genre is nonfiction'''
        nonfiction_books = []
        for book in self.books:
            if book.genre.lower() == 'nonfiction':
                nonfiction_books.append(book)
        return nonfiction_books

# Test cases
# Instantiate values
library = Library()
book1 = Book('Three Musketeers', 'Alexandre Dumas', 'fiction')
book2 = Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')
book3 = Book('Educated', 'Tara Westover', 'nonfiction')

# Add and sort books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.sort_books()

# Output
print(library.books) # [Book('Three Musketeers', 'Alexandre Dumas', 'fiction'), 
                     # Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction'), 
                     # Book('Educated', 'Tara Westover', 'nonfiction')]
print(library.fiction) # [Book('Three Musketeers', 'Alexandre Dumas', 'fiction'), 
                       # Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')]
print(library.nonfiction) # [Book('Educated', 'Tara Westover', 'nonfiction')]
print(library.search_author('Alexandre Dumas')) # [Book('Three Musketeers', 'Alexandre Dumas', 'fiction'), 
                                                # Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')]
print(library.search_author('Herman Melville')) # []
print(library.search_title('Educated')) # True
print(library.search_title('Moby Dick')) # False


# -------------------------
# Example 5 — composition (Shopping Cart has an Item)
# -------------------------
"""
item.py

Component class representing a single item in a shopping cart.
"""


class Item:
    """Represents a purchasable item with name, price, quantity, and subtotal."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = 0
#        self.calculate_subtotal()

    def calculate_subtotal(self):
        """Assigns the total value of the items to the subtotal attribute."""
        self.subtotal = self.price * self.quantity

    def get_subtotal(self):
        """Returns the subtotal attribute."""
        return self.subtotal

    def __repr__(self):
        """Returns a precise object definition."""
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})"

"""
shopping_cart.py

Composite class representing an online shopping cart.
"""


class ShoppingCart:
    """Holds a list of Item objects and tracks the running total."""

    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        """Add an item to the shopping cart and recalculate total."""
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        """Assigns the total value of the shopping cart to the total attribute."""
#        self.total = sum(item.get_subtotal() for item in self.items)
        self.total = 0
        for item in self.items:
            item.calculate_subtotal()
            self.total += item.get_subtotal()
    
    def get_total(self):
        """Returns the total value of the shopping cart."""
        return self.total

    def get_num_items(self):
        """Returns the number of different items in the shopping cart."""
        return len(self.items)

    def get_items(self):
        """Returns a list of all of the items in the cart."""
        return self.items

    def __str__(self):
        """Returns a human-readable string."""
        return f"The cart has {self.get_num_items()} items for a total of ${self.get_total()}"

# ------------------------------------------------------------
# Instantiate objects for test execution
# ------------------------------------------------------------

# If Item and ShoppingCart were defined in separate modules:
# from item import Item
# from shopping_cart import ShoppingCart

# Create Item instances (name, price, quantity)
item1 = Item('milk', 1.5, 1)
item2 = Item('apple', 5, 0.75)
item3 = Item('bread', 2, 2.25)

# Create ShoppingCart composite
cart = ShoppingCart()

# Add items to cart (recalculates total each time)
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

# ------------------------------------------------------------
# Test Cases — verify required behaviors
# ------------------------------------------------------------

print(cart.get_total())      # expected: 9.75
print(cart.get_num_items())  # expected: 3
print(cart)                  # expected: "The cart has 3 items for a total of $9.75"

# List representation uses __repr__ for each Item
print(cart.get_items())      # expected: [Item(milk, 1.5, 1, 1.5), Item(apple, 5, 0.75, 3.75), Item(bread, 2, 2.25, 4.5)]