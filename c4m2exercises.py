# Class with encapsulated attributes
class Country:
    """Country class with name, capital, population, and continent."""
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent
    
#test case
my_country = Country('France', 'Paris', 67081000, 'Europe')
print(my_country._name)       # France
print(my_country._capital)    # Paris
print(my_country._population) # 67081000
print(my_country._continent)  # Europe


# Name Mangling
class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

# Test case
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# These produce AttributeError (expected)
# print(my_artist.__name)
# print(my_artist.__medium)
# print(my_artist.__style)
# print(my_artist.__famous_artwork)

# These succeed because of name‑mangling
print(my_artist._Artist__name)    # Bill Watterson
print(my_artist._Artist__medium)  # ink and paper
print(my_artist._Artist__style)   # cartoons
print(my_artist._Artist__famous_artwork) # Calvin and Hobbes


# BankAccount Class (no @property or property function)
class BankAccount:
    """Encapsulation using private attributes + public aliases 
    (no property decorator or property function)."""

    def __init__(self, checking=0, savings=0):
        # private attributes
        self._checking = checking
        self._savings = savings

        # public attributes required  
        self.checking = checking
        self.savings = savings

    # getters
    def get_checking(self):
        return self._checking

    def get_savings(self):
        return self._savings

    # setters
    def set_checking(self, new_checking):
        self._checking = new_checking
        self.checking = new_checking

    def set_savings(self, new_savings):
        self._savings = new_savings
        self.savings = new_savings

# Running BankAccount tests
my_account = BankAccount(0, 0)

my_account.set_checking(523.48)
print(my_account.get_checking())

my_account.set_savings(386.15)
print(my_account.get_savings())


# Class with encapsulated attributes using property function
class Dancer:
    """Implements getters/setters using property()."""
    def __init__(self, name, nationality, style):
        self._name = name
        self._nationality = nationality
        self._style = style

    # getter methods
    def get_name(self):
        return self._name

    def get_nationality(self):
        return self._nationality
    
    def get_style(self):
        return self._style

    # setter methods
    def set_name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    def set_nationality(self, new_nationality):
        if type(new_nationality) != str:
            raise TypeError("Names must be expressed as a string")
        self._nationality = new_nationality
    
    def set_style(self, new_style):
        if type(new_style) != str:
            raise TypeError("Names must be expressed as a string")
        self._style = new_style

    # property objects
    name = property(get_name, set_name)
    nationality = property(get_nationality, set_nationality)
    style = property(get_style, set_style)

# Test case:
my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)    # Savion Glover
print(my_dancer.nationality) # American
print(my_dancer.style)   # tap
my_dancer.name = "Anna Pavlova"
my_dancer.nationality = "Russian"
my_dancer.style = "ballet"
print(my_dancer.name)  # Anna Pavlova
print(my_dancer.nationality) # Russian
print(my_dancer.style) # ballet


# Class with encapsulated attributes using property decorator
class Cyclist:
    """Uses @property and validation for name, nationality, and nickname."""
    def __init__(self, name, nationality, nickname):
        self._name = name 
        self._nationality = nationality
        self._nickname = nickname

    # getter
    @property
    def name(self):
        return self._name

    # setter with type validation
    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    # getter
    @property
    def nationality(self):
        return self._nationality

    # setter with type validation
    @nationality.setter
    def nationality(self, new_nationality):
        if type(new_nationality) != str:
            raise TypeError("Nationality must be expressed as a string")
        self._nationality = new_nationality
    
    # getter
    @property
    def nickname(self):
        return self._nickname

    # setter with type validation
    @nickname.setter
    def nickname(self, new_nickname):
        if type(new_nickname) != str:
            raise TypeError("Nickname must be expressed as a string")
        self._nickname = new_nickname

# Test cases
my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")
print(my_cyclist.name)        # Greg LeMond
print(my_cyclist.nationality) # American
print(my_cyclist.nickname)    # Le Monstre

my_cyclist.name = "Eddy Merckx"        # N/A
my_cyclist.nationality = "Belgian"     # N/A
my_cyclist.nickname = "The Cannibal"   # N/A

print(my_cyclist.name)        # Eddy Merckx
print(my_cyclist.nationality) # Belgian
print(my_cyclist.nickname)    # The Cannibal
