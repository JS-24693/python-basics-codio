# Demonstrate mutability using instance methods instead of external functions

# Player class with methods
class Player:
    """Simple Player class"""
    def __init__(self, health=100, score=0, level=1):
        self.health = health
        self.score = score
        self.level = level

    def print_player(self):
        """Print status of the player"""
        if self.health <= 0:
            print(f"This player is dead. They died on level {self.level} with a score of {self.score}")
        else:
            print(f"This player has {self.health} health, a score of {self.score}, and is on level {self.level}")

    def change_health(self, amount):
        """Modify health by amount"""
        self.health += amount

    def change_level(self):
        """Increase level by one"""
        self.level += 1

    def change_score(self, amount):
        """Modify score by amount"""
        self.score += amount


# Demonstration
mario = Player()
mario.print_player()
mario.change_health(-10)
mario.change_level()
mario.change_score(25)
mario.print_player()


# Meal class with methods
class Meal:
    """Class to represent a meal"""
    def __init__(self):
        self.drinks = []
        self.appetizers = []
        self.main_course = []
        self.desserts = []

    def add_drink(self, d):
        """Add drink to meal"""
        self.drinks.append(d)

    def add_appetizer(self, a):
        """Add appetizer to meal"""
        self.appetizers.append(a)

    def add_course(self, c):
        """Add main course to meal"""
        self.main_course.append(c)

    def add_dessert(self, d):
        """Add dessert to meal"""
        self.desserts.append(d)

    def course_name(self, position):
        """Return correct course label"""
        if position == 0:
            return "drinks were"
        elif position == 1:
            return "appetizers were"
        elif position == 2:
            return "main course was"
        elif position == 3:
            return "dessert was"

    def print_meal(self):
        """Print meal contents"""
        courses = [self.drinks, self.appetizers, self.main_course, self.desserts]

        for position in range(4):
            course = courses[position]

            # No items
            if len(course) == 0:
                print(f"No {self.course_name(position)} served with the meal.")

            # One item
            elif len(course) == 1:
                print(f"{course[0].capitalize()} was served with the meal.")

            # Two items
            elif len(course) == 2:
                print(f"{course[0].capitalize()} and {course[1]} were served with the meal.")

            # Many items
            else:
                for item in course:
                    if course.index(item) == 0:
                        print(f"{item.capitalize()}, ", end="")
                    elif item == course[-1]:
                        print(f"and {item} ", end="")
                    else:
                        print(f"{item}, ", end="")
                print("were served with the meal.")


# Demonstration
dinner = Meal()
dinner2 = Meal()
dinner3 = Meal()
dinner4= Meal()
dinner5 = Meal()
dinner.add_drink("white wine")
dinner.add_appetizer("tapenade")
dinner.add_appetizer("antipasto")
dinner.add_course("cauliflower bolognese")
dinner.add_course("butternut squash soup")
dinner.add_course("kale salad")
dinner.add_dessert("chocolate cake")
dinner.print_meal() # White wine was served with the meal.
                    # Tapenade and antipasto were served with the meal.
                    # Cauliflower bolognese, butternut squash soup, and kale salad were served with the meal.
                    # Chocolate cake was served with the meal.
dinner2.add_appetizer("cheese tray")
dinner2.add_course("grilled chicken")
dinner2.add_course("grilled vege medley")
dinner2.add_dessert("creme brulee")
dinner2.print_meal() # No drinks were served with the meal.
                     # Cheese tray was served with the meal.
                     # Grilled chicken and grilled vege medley were served with the meal.
                     # Creme brulee was served with the meal.
dinner3.print_meal() # No drinks were served with the meal.
                     # No appetizers were served with the meal.
                     # No main course was served with the meal.
                     # No dessert was served with the meal.
dinner4.add_drink("coffee")
dinner4.print_meal() # Coffee was served with the meal.
                     # No appetizers were served with the meal.
                     # No main course was served with the meal.
                     # No dessert was served with the meal.
dinner5.add_drink("water")
dinner5.add_drink("coffee")
dinner5.print_meal() # Water and coffee were served with the meal.
                     # No appetizers were served with the meal.
                     # No main course was served with the meal.
                     # No dessert was served with the meal.                   