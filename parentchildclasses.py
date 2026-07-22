# Parent class
class Person:
    """Represents a basic person with name, age, and occupation."""
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def say_age(self):
        print(f"I am {self.age} years old.")


# Child class inheriting from Person
class Superhero(Person):
  pass

hero = Superhero("Jessica Jones", 29, "private investigator")
print(hero.name)        # Jessica Jones
print(hero.occupation)  # private investigator
print(hero.age)         # 29
hero.say_hello()        # Hello, my name is Jessica Jones.
hero.say_age()          # I am 29 years old.


# Help aids in understanding what is being inherited
print(help(Superhero))

# builtins.object: all Python classes automatically inherit from the base object type.
# Using help(Person) shows the inheritance chain (Method Resolution Order), including builtins.object.
print(help(Person))


# Extends Person with superhero behavior.
class Superhero(Person):
    """Child class that extends Person with superhero behavior."""

    # Using super() to call the parent __init__
    def __init__(self, name, age, occupation, secret_identity, nemesis):
        super().__init__(name, age, occupation)
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    # Override say_hello but still call parent version
    def say_hello(self):
        super().say_hello()

    # Override say_age using super()
    def say_age(self):
        super().say_age()

    # New method unique to child class
    def say_two_things(self):
        super().say_hello()
        super().say_age()

    # New method unique to child class
    def reveal_secret_identity(self):
        print(f"My secret identity is {self.secret_identity}.")


# Demonstration of inheritance
hero = Superhero("Jessica Jones", 29, "Private Investigator",
                 "Jewel", "Kilgrave")

hero.say_hello()          # inherited + overridden
hero.say_age()            # inherited + overridden
hero.say_two_things()     # child-only method
hero.reveal_secret_identity()  # child-only method

print(hero.name)          # inherited attribute
print(hero.occupation)    # inherited attribute


# Demonstration of isinstance
print(isinstance(hero, Superhero))  # True
print(isinstance(hero, Person))     # True (child → parent)
print(isinstance(hero, object))     # True (all classes inherit object)


# Demonstration of issubclass
print(issubclass(Superhero, Person))  # True
print(issubclass(Person, Superhero))  # False
print(issubclass(Superhero, object))  # True

# Demonstration 2: isinstance and issubclass
class ClassA:
  pass
    
class ClassB(ClassA):
  pass

class ClassC:
  pass

class ClassD(ClassC):
  pass

object_a = ClassA()
object_b = ClassB()
object_c = ClassC()
object_d = ClassD()

# isinstance takes an object and a class name
print(isinstance(object_b, ClassA)) # True 
print(isinstance(object_d, ClassC)) # True
print(isinstance(object_b, ClassC)) # False
print(isinstance(object_d, ClassA)) # False
print(isinstance(object_a, ClassA)) # True
print(isinstance(object_a, object)) # True (all classes inherit object)

# issubclass takes a class and a class name
print(issubclass(ClassB, ClassA)) # True
print(issubclass(ClassD, ClassC)) # True
print(issubclass(ClassD, ClassA)) # False
print(issubclass(ClassA, ClassB)) # False
print(issubclass(object, ClassA)) # False
