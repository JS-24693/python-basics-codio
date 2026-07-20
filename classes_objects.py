# Built‑in String Object
s = "I am a string"
print(type(s))      # <class 'str'>
print(dir(str))     # dir(str) shows all attributes and methods of the string class,
# including dunder methods (__add__, __len__, __getitem__, etc.)
# and regular string methods (upper, lower, split, replace, startswith, etc.)

print(s.__add__("!"))    # I am a string!
print(s.__sizeof__())    # 62
print(s.startswith("I")) # True

# Minimal Class Definition
class Actor:
    pass

print(Actor)   # <class '__main__.Actor'>

helen = Actor()
print(type(helen)) # <class '__main__.Actor'>

# Instantiate Object + Add Attributes
class Actor:
    pass

helen = Actor()
helen.first_name = "Helen"
helen.last_name = "Mirren"

print(helen.first_name, helen.last_name)    # Helen Mirren
print(helen.first_name.upper(), helen.last_name.lower()) # HELEN mirren

helen.total_films = 80
helen.notable_films = ["The Queen", "The Madness of King George", "Gosford Park"]

print(helen)    # <__main__.Actor object at 0x730103337550>

# Constructor __init__ Without Parameters
class Actor:
    """Define the actor class"""
    def __init__(self):
        self.first_name = "Helen"
        self.last_name = "Mirren"
        self.birthday = "July 26"
        self.total_films = 80
        self.oscar_nominations = 4
        self.oscar_wins = 1

helen = Actor()
print(helen.first_name, helen.last_name)
print("{} {}'s birthday is {}.".format(helen.first_name, helen.last_name, helen.birthday))
print("{} {} won an oscar {}% of the time.".format(helen.first_name, helen.last_name, helen.oscar_wins / helen.oscar_nominations))

# Constructor With Parameters
class Actor:
    """Define the actor class"""
    def __init__(self, first_name, last_name, birthday, total_films,
                 oscar_nominations, oscar_wins):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.total_films = total_films
        self.oscar_nominations = oscar_nominations
        self.oscar_wins = oscar_wins

helen = Actor("Helen", "Mirren", "July 26", 80, 4, 1)
tom = Actor("Tom", "Hanks", "July 9", 76, 5, 2)
denzel = Actor("Denzel", "Washington", "December 28", 47, 8, 2)

print(helen.first_name, helen.last_name)
print(tom.first_name, tom.last_name)
print(denzel.first_name, denzel.last_name)

# Constructor With Default Parameters
class Actor:
    """Define the actor class"""
    def __init__(self, first_name, last_name, birthday="January 1",
                 total_films=10, oscar_nominations=0, oscar_wins=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.total_films = total_films
        self.oscar_nominations = oscar_nominations
        self.oscar_wins = oscar_wins

helen = Actor("Helen", "Mirren", "July 26", 80, 4, 1)
dwayne = Actor("Dwayne", "Johnson", "July 9", 34)

print(f"{helen.first_name} won {helen.oscar_wins} oscar(s).")
print(f"{dwayne.first_name} won {dwayne.oscar_wins} oscar(s).")

# Class Attribute
class Actor:
    """Define the actor class"""
    union = "Screen Actors Guild"

    def __init__(self, first_name, last_name, birthday, total_films,
                 oscar_nominations, oscar_wins):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.total_films = total_films
        self.oscar_nominations = oscar_nominations
        self.oscar_wins = oscar_wins

helen = Actor("Helen", "Mirren", "July 26", 80, 4, 1)
dwayne = Actor("Dwayne", "Johnson", "July 9", 34, 0, 0)

print(f"{helen.first_name} {helen.last_name} is a member of the {helen.union}.")
print(f"{dwayne.first_name} {dwayne.last_name} is a member of the {dwayne.union}.")

# Shallow Copy
class ComicBookCharacter:
    pass

a = ComicBookCharacter()
a.name = "Calvin"
a.age = 6
a.type = "human"

b = a  # shallow copy
a.name = "Hobbes"

print(a.name)
print(b.name)

# Deep Copy
import copy

class ComicBookCharacter:
    pass

a = ComicBookCharacter()
a.name = "Calvin"
a.age = 6
a.type = "human"

b = copy.deepcopy(a)  # deep copy
a.name = "Hobbes"

print(a.name)   # Hobbes
print(b.name)   # Calvin

# Extra practice: # Dog class declaration and object instantiation
class Dog:
    pass

fido = Dog()          # instantiate object
fido.breed = "poodle" # add attribute
