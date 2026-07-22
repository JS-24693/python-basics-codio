# ------------------------------------------------------------
# Operator Polymorphism
# ------------------------------------------------------------

# Same operator (+) works differently depending on type
a = 5
b = 10
print(a + b)          # integer addition 15

c = '5'
d = '10'
print(c + d)          # string concatenation 510


# ------------------------------------------------------------
# Method Overriding (polymorphism through inheritance)
# ------------------------------------------------------------

class Alpha:
    def show(self):
        print("I am from class Alpha")

    def hello(self):
        print("Hello from Alpha")


class Bravo(Alpha):
    def show(self):
        print("I am from class Bravo")

    def hello(self):
        print("Hello from Bravo")


test_object = Alpha()
test_object.show()     # Alpha version
test_object.hello()    # Alpha version

test_object = Bravo()
test_object.show()     # Bravo version
test_object.hello()    # Bravo version


# ------------------------------------------------------------
# Method Overloading (Python style using default parameters)
# ------------------------------------------------------------

class TestClass:
    def sum(self, a=None, b=None, c=None, d=None, e=None):
        """Simulates method overloading by using None as a placeholder
        and returning the sum of all non‑None parameters."""
        # five parameters
        if a is not None and b is not None and c is not None and d is not None and e is not None:
            return a + b + c + d + e
        # four parameters
        if a is not None and b is not None and c is not None and d is not None:
            return a + b + c + d
        # three parameters
        if a is not None and b is not None and c is not None:
            return a + b + c
        # two parameters
        elif a is not None and b is not None:
            return a + b
        # one parameter
        elif a is not None:
            return a
        # no parameters
        else:
            return 0


obj = TestClass()
print(obj.sum())          # 0
print(obj.sum(1))         # 1
print(obj.sum(1, 2))      # 3
print(obj.sum(1, 2, 3))   # 6
print(obj.sum(1, 2, 3, 4))   # 10
print(obj.sum(1, 2, 3, 4, 5))   # 15


# ------------------------------------------------------------
# Operator Overloading
# ------------------------------------------------------------

# Multiplication Operator Overloading used with num and str objects
my_string = "polymorphism "
num1 = 3
num2 = 5
print(num1 * num2)      # 15
print(my_string * num1) # polymorphism polymorphism polymorphism


# Operator Overloading for User-Defined Classes
class FinancialAccount:
    def __init__(self, amount):
        self.account = amount

    def __add__(self, other):
        return self.account + other.account

    def __eq__(self, other):
        return self.account == other.account

    def __truediv__(self, other):
        return self.account / other.account

    def __floordiv__(self, other):
        return self.account // other.account


class BankAccount(FinancialAccount):
    pass


class InvestmentAccount(FinancialAccount):
    pass


my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)

print(my_banking + my_investments)     # overloaded +   1250
print(my_banking == my_investments)    # overloaded ==  False
print(my_investments / my_banking)     # overloaded /   1.5
print(my_investments // my_banking)    # overloaded //  1


# ------------------------------------------------------------
# Duck Typing
# ------------------------------------------------------------

import random

class BaseballPlayer:
    def hit(self):
        """Return type of hit based on random bases."""
        total_bases = random.randint(1, 4)
        if total_bases == 1:
            return "single"
        elif total_bases == 2:
            return "double"
        elif total_bases == 3:
            return "triple"
        else:
            return "home run"


class Song:
    def __init__(self, title, ranking):
        self.title = title
        self.ranking = ranking

    def hit(self):
        """Song is a hit if ranking <= 40."""
        if self.ranking <= 40:
            return f"{self.title} is a hit song"
        else:
            return f"{self.title} is not a hit song"


class Boxer:
    def hit(self):
        return "jab"


def print_hit(obj):
    """Duck typing: call hit() if available, handle errors."""
    try:
        print(obj.hit())
    except AttributeError as e:
        print(e)


my_player = BaseballPlayer()
my_song = Song("Hey Jude", 12)
my_boxer = Boxer()

print_hit(my_player)
print_hit(my_song)
print_hit(my_boxer)


# ------------------------------------------------------------
# Duck Typing Example with fly()
# ------------------------------------------------------------

class Bird:
    def fly(self):
        return "I am flapping my wings"


class Car:
    def drive(self):
        return "My wheels are turning"


def print_fly(obj):
    """Duck typing for fly() with error handling."""
    try:
        print(obj.fly())
    except AttributeError as e:
        print(e)


my_bird = Bird()
my_car = Car()

print_fly(my_bird)   # "I am flapping my wings"
print_fly(my_car)    # 'Car' object has no attribute 'fly'
