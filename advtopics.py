"""
advtopics.py and advtopics2.py

Compact, self-contained examples for:
- importing classes from modules
- creating and manipulating a list of objects
- composition (component vs composite)
- __str__ and __repr__ behavior
Each example is minimal and runnable.
"""

# -------------------------
# Example 1 — class in a module style (Employee)
# -------------------------

# Employee class definition

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def display(self):
        print(f'Employee: {self.name}')
        print(f'Title: {self.title}')

def greeting():
    print('Hello from the "advtopics" module')

# advtopics2.py imports this data


# -------------------------
# Example 2 — App class for a list of objects
# -------------------------
# App
class App:
    """Represents a smartphone app with name, description and category."""
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def display(self):
        """Print a short description of the app."""
        print(f"{self.name} ({self.category}): {self.description}")


# -------------------------
# Example 3 — composition (Car has an Engine)
# -------------------------
class Engine:
    """Component class representing an engine."""
    def __init__(self, configuration: str, displacement: float, horsepower: int, torque: int) -> None:
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def info(self) -> None:
        """Print engine details (component responsibility)."""
        print(f"Engine: {self.configuration}, {self.displacement}L, {self.horsepower} HP, {self.torque} lb-ft")

    def ignite(self) -> None:
        """Simulate starting the engine."""
        print("Vroom, vroom!")


class Car:
    """Composite class that 'has an' Engine (composition)."""
    def __init__(self, make: str, model: str, year: int, engine: Engine) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def describe(self) -> None:
        """Print a short description of the car."""
        print(f"{self.year} {self.make} {self.model}")

    def start(self) -> None:
        """Start the car by delegating to the engine."""
        self.engine.ignite()

# Test cases
my_engine = Engine("V8", 5.8, 326, 344)
my_car = Car("De Tomaso", "Pantera", 1979, my_engine)

my_car.describe()         # Car description
my_car.engine.info()      # Engine details (no AttributeError)
my_car.engine.ignite()    # Engine start
my_car.start()            # Car start delegates to engine

# -------------------------
# Example 4 — __str__ and __repr__ (Dog)
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

dogs = []
dogs.append(Dog("Rocky", "Pomeranian"))
dogs.append(Dog("Bullwinkle", "Labrador Retriever"))
print(dogs[0:1])
# printing a single object uses __str__
print(dogs[0])

# printing a list uses __repr__ for each element
print(dogs)
