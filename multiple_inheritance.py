# Parent class 1
class Dinosaur:
    """Represents dinosaur physical attributes."""
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight


# Parent class 2
class Carnivore:
    """Represents carnivore dietary attributes."""
    def __init__(self, diet):
        self.diet = diet


# Child class using multiple inheritance
# Multiple inheritance is when there are more than one parent class.
class Tyrannosaurus(Dinosaur, Carnivore):
    """Inherits from Dinosaur and Carnivore."""
    pass

tiny = Tyrannosaurus(12, 14)
print(tiny.size)

class Tyrannosaurus(Carnivore, Dinosaur):
    """Inherits from Carnivore and Dinosaur."""
    pass
tiny = Tyrannosaurus("whatever it wants")
print(tiny.diet)


# Access attributes from all parent classes
class Tyrannosaurus(Dinosaur, Carnivore):
    """Inherits from Dinosaur and Carnivore."""

    # Overriding __init__ to call both parent constructors
    # Instead of super(), use the name of the class. Use self with parent classes.
    def __init__(self, size, weight, diet):
        Dinosaur.__init__(self, size, weight)
        Carnivore.__init__(self, diet)

# Demonstration: full attribute access
tiny = Tyrannosaurus(12, 14, "whatever it wants")
print(tiny.size)    # from Dinosaur
print(tiny.weight)  # from Dinosaur
print(tiny.diet)    # from Carnivore


# Multiple inheritance hierarchy demonstration 1
class A:
  pass

class B:
  pass

class C:
  pass

class D(A, B):
  pass

obj= D()
print(isinstance(obj, D)) # True
print(isinstance(obj, A)) # True
print(isinstance(obj, B)) # True
print(isinstance(obj, C)) # False
print(issubclass(D, A))   # True
print(issubclass(D, B))   # True
print(issubclass(D, C))   # False

# Multiple inheritance hierarchy demonstration 2
class A:
    def hello(self):
        print("Hello from class A")

class B:
    def hello(self):
        print("Hello from class B")

# Child class inheriting from A and B
class C(A, B):
    """Demonstrates MRO and method overriding."""
    def hello(self):
        print("Hello from class C")
        super().hello()      # MRO determines which parent is used
        B.hello(self)        # Explicit call to second parent


# Demonstration of MRO
obj = C()
obj.hello() # Hello from class C
            # Hello from class A
            # Hello from class B

# Print(C.mro()) 
print(C.mro())  # Shows method resolution order
                # [<class '__main__.C'>, 
                # <class '__main__.A'>, 
                # <class '__main__.B'>, 
                # <class 'object'>]


# Demonstration of isinstance and issubclass
class D(A, B):
    pass

obj2 = D()
print(isinstance(obj2, D))  # True
print(isinstance(obj2, A))  # True
print(isinstance(obj2, B))  # True
print(isinstance(obj2, C))  # False

print(issubclass(D, A))     # True
print(issubclass(D, B))     # True
print(issubclass(D, C))     # False
