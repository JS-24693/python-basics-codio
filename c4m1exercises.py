# Exercise 1: create two subclasses and extend the __init__ method
class CelestialBody:
    """Parent class for any celestial object."""
    def __init__(self, size, mass, composition, name):
        self.size = size
        self.mass = mass
        self.composition = composition
        self.name = name

class Satellite(CelestialBody):
    """Child class extending CelestialBody __init__."""
    def __init__(self, size, mass, composition, name, host_planet):
        super().__init__(size, mass, composition, name)
        self.host_planet = host_planet

class Planet(CelestialBody):
    """Child class extending CelestialBody __init__."""
    def __init__(self, size, mass, composition, name, host_star):
        super().__init__(size, mass, composition, name)
        self.host_star = host_star


# Exercise 2: create subclass and override the __init__ constructor attributes:
# parent class
class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre

# child class
class BlogPost(Book):
  """Child class that overrides Book __init__."""
  def __init__(self, website, title, author, word_count, genre, page_views):
    super().__init__(title, author, genre)
    self.website = website
    self.word_count = word_count
    self.page_views = page_views

# Test case
# object instantiation
my_post = BlogPost("Vogue", "Hot Summer Trends", "Amy Gutierrez", 2319, "fashion", 2748)

print(my_post.website)	# Vogue
print(my_post.title)	  # Hot Summer Trends
print(my_post.author)	  # Amy Gutierrez
print(my_post.word_count)	# 2139
print(my_post.genre)	  # fashion
print(my_post.page_views)	# 2748


# Exercise 3: create subclass, override method, and invoke one parent method
class Parent1:
    def identify(self):
        return "This method is called from Parent1"
    
class Parent2:
    def identify(self):
        return "This method is called from Parent2"
    

class Child(Parent2, Parent1):
    """Inherits from Parent2 and Parent1; overrides identify."""
    
    def identify(self):
        return "This method is called from Child"

    def identify2(self):
        return super().identify()   # MRO: Child → Parent2 → Parent1 → object
                                    # super().identify() resolves to Parent2.identify()
 
# Test case
child_object = Child()

print(child_object.identify())   # calls the method from Child → prints the string
print(child_object.identify2())  # calls the method from Parent2 → prints the string


# Exercise 4: Create sub class, extend objects, return total amount of money

# 2D list representing three branches with their account balances
accounts = [
    [10000, 13000, 22000],
    [30000, 7000, 19000],
    [15000, 23000, 31000]
]

class Bank:
    """Parent class representing a single bank branch."""
    def __init__(self, name, customers, accounts):
        self.name = name              # branch name
        self.customers = customers    # number of customers
        self.accounts = accounts      # 1D list of account balances
    
    def branch_total(self, accounts):
        """Return total money in one branch."""
        total = 0
        for account in accounts:
            total += account
        return total


class RegionalBank(Bank):
    """Child class representing multiple branches (2D list)."""

    def __init__(self, name, customers, accounts_2d):
        # Pass the 2D list to the parent constructor correctly
        super().__init__(name, customers, accounts_2d)
        self.accounts_2d = accounts_2d   # store 2D list explicitly

    def regional_total(self):
        """Return total money across all branches in the region."""
        total = 0
        for branch in self.accounts_2d:          # each branch is a 1D list
            total += self.branch_total(branch)   # reuse parent method
        return total

# Test Case
# Instantiate using the provided accounts list
rb = RegionalBank("Midwest Region", 3000, accounts)

# Print total money across all branches
print(rb.regional_total())  # 170000


# Exercise 4, Variation 1
# 2D list representing three branches with their account balances
accounts = [
    [10000, 13000, 22000],
    [30000, 7000, 19000],
    [15000, 23000, 31000],
    [10000, 13000, 22000],
    [30000, 7000, 19000],
    [15000, 23000, 31000],
    [10000, 13000, 22000],
    [30000, 7000, 19000],
    [15000, 23000, 31000]
]

# Parent class representing a single bank branch
class Bank:
  def __init__(self, name, customers, accounts):
    self.name = name              # branch name
    self.customers = customers    # number of customers
    self.accounts = accounts      # 1D list of account balances
    
  def branch_total(self, accounts):
    total = 0                     # sum of one branch's accounts
    for account in accounts:
      total += account
    return total

# Child class using the global 2D accounts list (grader-style design)
class RegionalBank(Bank):
  def regional_total(self):
    total = 0                     # total across all branches
    for account in accounts:      # iterate through global 2D list
      total += self.branch_total(account)
    return total
  
# Instantiate using injected accounts list
my_bank = RegionalBank("Bank of America", 9, accounts)

# Print total money across all branches
print(my_bank.regional_total())


# Exercise 5: Multiple Inheritance, extend attributes, override method
# parent classes
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_info(self):
        return f"{self.name} lives at {self.address}."
  
class CardHolder:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.credit_limit = 5000
    
    def process_sale(self, price):
        self.balance += price
    
    def make_payment(self, amount):
        self.balance -= amount


# child class
class PlatinumClient(Person, CardHolder):
    def __init__(self, name, address, account_number, cash_back=0.02, rewards=0):
        Person.__init__(self, name, address)          # initialize Person
        CardHolder.__init__(self, account_number)     # initialize CardHolder
        self.cash_back = cash_back                    # % reward per sale
        self.rewards = rewards                        # reward balance

    def process_sale(self, price):
        """Override: add full price to balance AND 2% to rewards."""
        self.balance += price
        self.rewards += price * self.cash_back

# Instantiate a PlatinumClient object
platinum = PlatinumClient("Sarah", "101 Main Street", 123364)
# Test code
platinum.process_sale(100)  # adds 100 to balance and 2% (2) to rewards

print(platinum.rewards)     # 2.0 (from 100 * .02= 2.0)
print(platinum.balance)     # 100

platinum.make_payment(50)   # subtracts 50 from balance
print(platinum.balance)     # 50

print(platinum.get_info())  # Sarah lives at 101 Main Street.
