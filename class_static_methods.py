# Demonstrate class methods, static methods, and factory methods

# -----------------------------
# Class Method Example
# -----------------------------
class NFLteam:
    """Define the NFL team class"""
    salary_cap = 198200000  # class attribute

    def __init__(self, city, name):
        self.city = city
        self.name = name

    @classmethod                                 # decorator
    def change_salary_cap(cls, new_cap):         # cls as parameter
        """Modify class attribute salary_cap"""
        cls.salary_cap = new_cap


# Demonstration
team_1 = NFLteam("Cincinnati", "Bengals")
team_2 = NFLteam("New England", "Patriots")

NFLteam.change_salary_cap(199000000)  # class-level change
print(team_1.salary_cap, team_2.salary_cap)

# Variation 1: Class Method cannot affect instance variables

class NFLteam:
    """Define the NFL team class"""
    salary_cap = 198200000  # class attribute shared by all teams

    def __init__(self, city, name):
        # instance attributes (unique per team)
        self.city = city
        self.name = name

    @classmethod
    def change_city(self, new_city):
        # ERROR: class methods receive 'cls', not an instance
        # This assigns 'new_city' to a CLASS attribute named 'city'
        # It does NOT modify the instance variable self.city
        self.city = new_city

# Create instance
team = NFLteam("Dallas", "Cowboys")

# Call class method
team.change_city("Portland")

# Instance variable is unchanged because class methods cannot modify instance data
print(team.city)    # Dallas

# -----------------------------
# Factory Method Example
# -----------------------------
class Pizza:
    """Pizza class with a list of toppings"""
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def make_margherita(cls):
        """Factory method for Margherita pizza"""
        return cls(["tomato sauce", "mozzarella", "basil"])

    @classmethod
    def make_veggie(cls):
        """Factory method for veggie pizza"""
        return cls(["tomato sauce", "mozzarella", "mushroom", "bell pepper"])

    @classmethod
    def make_three_cheese(cls):
        """Factory method for three-cheese pizza"""
        return cls(["tomato sauce", "mozzarella", "fontina", "parmesan"])


# Demonstration
p1 = Pizza.make_margherita()
p2 = Pizza.make_veggie()
p3 = Pizza.make_three_cheese()
print(p1.toppings, p2.toppings, p3.toppings)


# -----------------------------
# Static Method Example
# -----------------------------
class Rectangle:
    """Rectangle class"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area"""
        return self.length * self.width

    @staticmethod
    def combined_area(r1, r2):
        """Calculate combined area of two rectangles"""
        return r1.area() + r2.area()


# Demonstration
rect_1 = Rectangle(12, 27)
rect_2 = Rectangle(9, 3)

combined = Rectangle.combined_area(rect_1, rect_2)
print(combined)

# Static method also callable from an instance
print(rect_1.combined_area(rect_1, rect_2)) # 351
                                            # 351
