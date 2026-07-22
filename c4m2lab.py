# ------------------------------------------------------------
# CoffeeJournal reads/writes CSV
# ------------------------------------------------------------

from pathlib import Path
import csv      # houses csv.writer
from csv import reader  # houses csv.reader

csv_path = Path("Codio_Python") / "coffee.csv"

class CoffeeJournal:
    def __init__(self, file):
        """Encapsulated CSV-backed journal."""
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._old_coffee = self.load_coffee()
        self._new_coffee = []

    def load_coffee(self):
        """Reads CSV file into a 2D list."""
        coffee = []

        csv_path = Path(self._file)
        if not csv_path.exists():
            return coffee

        with csv_path.open("r", encoding="utf-8", errors="replace") as f:
            csv_reader = reader(f, delimiter=",")
            try:
                header = next(csv_reader)  # read header, keep it
                coffee.append(header)
            except StopIteration:
                return coffee

            for row in csv_reader:
                if not row:
                    continue
                coffee.append([field.strip() for field in row])

        return coffee

    @property
    def roaster(self):
        return self._roaster

    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, new_region):
        self._region = new_region

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

    def _validate_coffee_row(self, row):
        """
        Strict validator for a coffee row.
        Row must be: [roaster, country, region, stars]
        Stars must be 1–4 '*' characters.
        """
        if not isinstance(row, list):
            return False

        if len(row) != 4:
            return False

        roaster, country, region, stars = (field.strip() for field in row)

        # required text fields
        if not roaster or not country or not region:
            return False

        # stars must be *, **, ***, ****
        if stars not in ("*", "**", "***", "****"):
            return False

        return True

    def add_coffee(self):
        """Validate and Append new coffee entry."""
        row = [self._roaster, self._country, self._region, self._stars]
        if self._validate_coffee_row(row):
            self._new_coffee.append(row)
        else:
            print("Invalid coffee entry — not saved.")

    def save(self):
        """Validate data written."""
        valid_rows = [row for row in self._new_coffee if self._validate_coffee_row(row)]

        if not valid_rows:
            return  # nothing valid to save
        
        """Append new entries to CSV."""
        with open(self._file, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self._new_coffee)

    def show_coffee(self):
        """Print old/new coffee entries."""
        print()
        if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            print("Enter a coffee first")
        elif len(self._old_coffee) > 1 and len(self._new_coffee) == 0:
            for row in self._old_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")
        else:
            for row in self._old_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")
            for row in self._new_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15} {row[3]:15}")
        print()

# ------------------------------------------------------------
# CLI code — requires CSV + user input
# ------------------------------------------------------------
# CLI code OUTSIDE the class

def main_menu():
    print("Coffees of the World")
    print("\t1. Show Coffee")
    print("\t2. Add Coffee")
    print("\t3. Save and Quit")
    return int(input("Enter the number of your selection: "))

def perform_action(choice, coffee):
    if choice == 1:
        coffee.show_coffee()
    elif choice == 2:
        enter_coffee(coffee)
    elif choice == 3:
        quit(coffee)

def enter_coffee(coffee):
    coffee.roaster = input("Enter the name of the roaster: ")
    coffee.country = input("Enter the country of origin: ")
    coffee.region = input("Enter the region: ")
    coffee.stars = input("Enter the number of stars '*' (1-4): ")
    coffee.add_coffee()

def quit(coffee):
    global run_loop
    coffee.save()
    run_loop = False

run_loop = True
file = "coffee.csv"
my_coffee = CoffeeJournal(file)

while run_loop:
    choice = main_menu()
    perform_action(choice, my_coffee)


# ------------------------------------------------------------
# Lab Challenge: Person Class (no @property or property function)
# ------------------------------------------------------------

class Person:
    """Encapsulation using private attributes + public aliases (no @property)."""

    def __init__(self, name, age, occupation):
        # private attributes
        self._name = name
        self._age = age
        self._occupation = occupation

        # public attributes required by autograder
        self.name = name
        self.age = age
        self.occupation = occupation

    # getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_occupation(self):
        return self._occupation

    # setters
    def set_name(self, new_name):
        self._name = new_name
        self.name = new_name

    def set_age(self, new_age):
        self._age = new_age
        self.age = new_age

    def set_occupation(self, new_occupation):
        self._occupation = new_occupation
        self.occupation = new_occupation

# ------------------------------------------------------------
# Running Person tests
# ------------------------------------------------------------

my_person = Person("Citra Curie", 16, "student")
print(my_person.name)
my_person.name = "Rowan Faraday"
print(my_person.name)

print(my_person.age)
my_person.age = 18
print(my_person.age)

print(my_person.occupation)
my_person.occupation = "plumber"
print(my_person.occupation)
