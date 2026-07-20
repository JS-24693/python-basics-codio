# Demonstrate mutability and functions that modify object attributes

# Simple player class

class Player:
  """Simple player class"""
  def __init__(self, health=100, score=0, level=1):
    self.health = health
    self.score = score
    self.level = level
    
player1 = Player()
print(f"This player has {player1.health} health, a score of {player1.score}, and is on level {player1.level}.")
player1.health -= 10
player1.score += 25
player1.level += 1
print(f"This player has {player1.health} health, a score of {player1.score}, and is on level {player1.level}.")

# Level-up Function to update object
def level_up(player):
   player.level += 1
   player.health -= 15
   player.score += 50

level_up(player1)
print(f"This player has {player1.health} health, a score of {player1.score}, and is on level {player1.level}.")
      
# Player class with mutable attributes
# class Player:
#    """Simple player class"""
#    def __init__(self, health=100, score=0, level=1):
#        self.health = health
#        self.score = score
#        self.level = level

# Function to print player status
def print_player(p):
    """Print the status of a player"""
    if p.health <= 0:
        print(f"This player is dead. They died on level {p.level} with a score of {p.score}")
    else:
        print(f"This player has {p.health} health, a score of {p.score}, and is on level {p.level}")

# Demonstration of player status options
player1 = Player()     # create object
print_player(player1)  # This player has 100 health, a score of 0, and is on level 1.
player1.health = 0
player1.score += 25
player1.level += 1
print_player(player1)  # This player is dead. They died on level 2 with a score of 25.

# Function to change health (mutates object)
def change_health(p, amount):
    """Change a player's health"""
    p.health += amount

# Function to change level (mutates object)
def change_level(p):
    """Increase a player's level"""
    p.level += 1

# Demonstration of mutability
player1 = Player()          # create object
print_player(player1)       # initial status

change_health(player1, -50) # lose health
change_level(player1)       # level up
print_player(player1)       # updated status

change_health(player1, -50) # health reaches zero
print_player(player1)       # dead status
