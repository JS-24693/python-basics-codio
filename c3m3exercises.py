# Define class PracticeClass without a constructor or attributes
class PracticeClass:
    pass

print(PracticeClass)   # <class '__main__.PracticeClass'>

# Define class Cat with constructor without parameters and attributes

# Constructor __init__ Without Parameters
class Cat:                    
    """Define the cat class"""  # docstring for def
    def __init__(self):         # create fixed attributes
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"

kiwi = Cat()                     # instantiate object
print(kiwi.name, kiwi.breed)     # verify attributes

# Define class SuperHero with constructor with parameters and attributes

# Constructor __init__ With Parameters
class SuperHero:                    
    """Define the Super Hero class"""  # docstring for def
    def __init__(self, name, secret_identity, powers=[
        "superhuman strength", 
        "superhuman speed", 
        "superhuman reflexes", 
        "superhuman durability", 
        "healing factor", 
        "spider-sense alert", 
        "heightened senses", 
        "wallcrawling"
    ]):  
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers

peter = SuperHero("Spiderman", "Peter Parker", [
    "superhuman strength", 
    "superhuman speed", 
    "superhuman reflexes", 
    "superhuman durability", 
    "healing factor", 
    "spider-sense alert", 
    "heightened senses", 
    "wallcrawling"
]) 

print(peter.name, peter.secret_identity, peter.powers)     # verify attributes

# Observation class with default precipitation
class Observation:
    """Record Antarctic observational data"""
    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = float(temperature)
        self.elevation = float(elevation)
        self.penguins = int(penguins)
        self.precipitation = float(precipitation)

# test object
obs = Observation("October 26, 2019", -47, 329.4, 3)
print(obs.date, obs.temperature, obs.elevation, obs.penguins, obs.precipitation)

# BigCat class with class attribute
class BigCat:
    genus = "panthera"                 # class attribute shared by all BigCat objects

    def __init__(self, species, common_name, habitat):
        self.species = species         # e.g. "tigris"
        self.common_name = common_name # e.g. "tiger"
        self.habitat = habitat         # e.g. ["asia"]

# test object
tiger = BigCat("tigris", "tiger", ["asia"])
print(tiger.genus, tiger.species, tiger.common_name, tiger.habitat)
