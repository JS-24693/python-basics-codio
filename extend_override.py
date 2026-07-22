# Parent class
class Person:
    """Basic person with name, age, and occupation."""
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def say_age(self):
        print(f"I am {self.age} years old.")


# Child class extending and overriding Person
class Superhero(Person):
    """Child class that extends Person with secret identity and nemesis."""

    # Extending __init__ by adding new attributes
    # The init method is extended when the attribute secret_identity is added.
    def __init__(self, name, age, occupation, secret_identity, nemesis):
        super().__init__(name, age, occupation)  # call parent __init__
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    # New method: extending class with additional functionality
    # Create the method reveal_secret_identity.
    def reveal_secret_identity(self):
        print(f"My real name is {self.secret_identity}.")

    # New method: say_nemesis
    # “My nemesis is Doc Octopus.”
    def say_nemesis(self):
        print(f"My nemesis is {self.nemesis}.")

    # Overriding say_hello
    # Overriding a method means to change the contents.
    def say_hello(self):
        print(f"I am {self.name}, and criminals fear me.")

    # Overriding say_age
    def say_age(self):
        print("Young or old, I will triumph over evil.")

    # Accessing original parent methods using super()
    # super() gives a child class access to the original methods.
    def old_say_hello(self):
        super().say_hello()

    def old_say_age(self):
        super().say_age()


# Demonstration
hero = Superhero("Spider-Man", 17, "student", "Peter Parker", "Doc Octopus")

# Extended attributes
print(hero.secret_identity)
print(hero.nemesis)

# Extended methods
hero.reveal_secret_identity()
hero.say_nemesis()

# Overridden methods
hero.say_hello()
hero.say_age()

# Accessing original parent methods
hero.old_say_hello()
hero.old_say_age()
