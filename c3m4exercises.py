# Mutability Exercise 1
# Transform function to instance method
class CelestialBody:
  """Represents a celestial body"""
  def __init__(self, name, diameter, distance, moons):
    self.name = name
    self.diameter = diameter
    self.distance = distance
    self.moons = moons

# transform plain function to an instance method
#  def compared_to_earth(body):
#    """Determines the size of a celestial
#    body relative to Earth using diameter"""
#    earth = 12756.3
#    relative_size = body.diameter / earth
#    return relative_size
    
# planet = CelestialBody("Jupiter", 142984, 778360000, 79)
# print(compared_to_earth(planet))

# instance method: uses self and operates on this object's attributes
  def compared_to_earth(self):
    """Determines the size of this celestial
    body relative to Earth using diameter"""
    earth = 12756.3
    relative_size = self.diameter / earth
    return relative_size

# Mercury
planetM = CelestialBody("Mercury", 4879, 57900000, 0)

# Venus
planetV = CelestialBody("Venus", 12104, 108200000, 0)

# Mars
planetMa = CelestialBody("Mars", 6779, 227900000, 2)

# Jupiter
planetJ = CelestialBody("Jupiter", 142984, 778360000, 79)

# Uranus
planetU = CelestialBody("Uranus", 51118, 2871000000, 27)

# Neptune
planetN = CelestialBody("Neptune", 49528, 4495000000, 14)

print(planetM.compared_to_earth())
print(planetV.compared_to_earth())
print(planetMa.compared_to_earth())
print(planetJ.compared_to_earth())
print(planetU.compared_to_earth())
print(planetN.compared_to_earth())

# Mutability Exercise 2
# Add @staticmethod

class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
      self.name = name
      self.diameter = diameter
      self.distance = distance
      self.moons = moons
    
    @staticmethod
    def closer_to_sun(body1, body2):
        """Return the name of the celestial body closer to the sun."""
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name
    
mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)

print(CelestialBody.closer_to_sun(mercury, venus))

# Mutability Exercise 3
# Create a factory method called make_earth

class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    @classmethod
    def make_earth(cls):
        """Factory method for Earth"""
        return cls("Earth", 12756.3, 149600000, 1)

# Demonstration
my_planet = CelestialBody.make_earth()
print(my_planet.name)       # Earth
print(my_planet.distance)   # 149600000
print(my_planet.diameter)   # 12756.3
print(my_planet.moons)      # 1
    
# Mutability Exercise 4
# Create class Library and instance methods to add, borrow, and return books
class Library:
    """List of available books and list of books on loan"""
    def __init__(self):
        self.available = []
        self.on_loan = []

    def add_books(self, books):
        """Add each book title to available books"""
        for book in books:
            self.available.append(book)

    def borrow_book(self, book):
        """Remove book from available list 
        and add to on_loan list"""
        if book in self.available:
            self.available.remove(book)
            self.on_loan.append(book)

    def return_book(self, book):
        """Remove book from on_loan and add to available"""
        if book in self.on_loan:
            self.on_loan.remove(book)
            self.available.append(book)

#    def borrow_book(self, book):
#        """Remove book from available list 
#        and add to on_loan list"""
#        self.available.remove(book)
#        self.on_loan.append(book)

#    def return_book(self, book):
#        """Remove book from on_loan and add to available"""
#        self.on_loan.remove(book)
#        self.available.append(book)

# Demonstration
my_library = Library()

my_library.add_books([
    "Four Seasons",
    "Say Nothing",
    "Milkman",
    "Harry Potter and the Order of the Phoenix"
])
print(my_library.available)
# ["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"]

my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)
# ["Four Seasons", "Milkman"]
# ["Harry Potter and the Order of the Phoenix", "Say Nothing"]

my_library.return_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)
# ["Four Seasons", "Milkman", "Say Nothing"]
# ["Harry Potter and the Order of the Phoenix"]

# Mutability Exercise 5
# Solve Subway boarding, disembarking, advancing, distance, fare changes, and calculating fares
class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

    def board(self, n):
        """Add passengers and calculate fares."""
        self.passengers += n
        self.total_fares += n * Subway.fare

    def disembark(self, n):
        """Remove passengers but never below zero."""
        self.passengers = max(0, self.passengers - n)

    def advance(self):
        """Move subway one stop; reverse direction at ends."""
        idx = self.stops.index(self.current_stop)

        if self.direction == "south":
            if idx == len(self.stops) - 1:      # at Kendall
                self.direction = "north"
                self.current_stop = self.stops[idx - 1]
            else:
                self.current_stop = self.stops[idx + 1]
        else:  # direction == "north"
            if idx == 0:                        # at Alewife
                self.direction = "south"
                self.current_stop = self.stops[idx + 1]
            else:
                self.current_stop = self.stops[idx - 1]

    def distance(self, stop):
        """Return positive number of stops between current and target."""
        return abs(self.stops.index(self.current_stop) - self.stops.index(stop))

    @classmethod
    def change_fare(cls, new_fare):
        """Change fare for all Subway instances."""
        cls.fare = new_fare

# Demonstration: Boarding
s = Subway()
s.passengers = 220
s.board(45)
print(s.passengers)
# 265

# Demonstration: Total fares
s = Subway()
s.board(100)
print(s.total_fares)
# 240.0

# Demonstration: Disembarking
s = Subway()
s.passengers = 113
s.disembark(23)
print(s.passengers)
# 90

# Demonstration: Advancing
s = Subway()
s.current_stop = "Kendall"
s.direction = "south"
s.advance()
print(s.current_stop, s.direction)
# Central north

s.current_stop = "Porter"
s.direction = "south"
s.advance()
print(s.current_stop, s.direction)
# Harvard south

# Demonstration: Distance
s = Subway()
s.current_stop = "Davis"
print(s.distance("Central"))
# 3

# Demonstration: Changing fare
# Change fare for the entire class
Subway.change_fare(2.75)

# Demonstration
s1 = Subway()
s2 = Subway()

print(s1.fare)   # 2.75
print(s2.fare)   # 2.75
print(Subway.fare)  # 2.75

