"""
advtopics.py and advtopics2.py

Compact, self-contained examples for:
- importing classes from modules
- creating and manipulating a list of objects
- composition (component vs composite)
- __str__ and __repr__ behavior
Each example is minimal and runnable.
"""

# Importing advtopics module

# -------------------------
# Example 1 — class in a module style (Employee)
# -------------------------

from asyncio.sslproto import AppProtocolState

import advtopics  # import python file without the .py

emp = advtopics.Employee("Marcia", "VP of Sales")
emp.display() # Employee: Marcia
              # Title: VP of Sales

# Another way to import 
from advtopics import Employee, greeting

emp = Employee("Marcia", "VP of Sales")

emp.display()

greeting()

# -------------------------
# Example 2 — list of objects (App)
# -------------------------

# Provide the List generic for type hints like `list[App]`
from typing import List

# load App class from advtopics.py
from advtopics import App

# find local CSV file
from pathlib import Path

# CSV loader (explicit encoding, strip fields, defensive)
from csv import reader

def load_apps_from_csv(csv_path: Path) -> List[App]:
    """
    Read a CSV file with header (name, description, category) and return a list of App objects.
    The CSV reader returns each row as a list of strings; unpack into name, description, category.
    """
    apps: List[App] = []
    if not csv_path.exists():
        return apps
    with csv_path.open("r", encoding="utf-8", errors="replace") as csv_file:
        csv_reader = reader(csv_file, delimiter=",")
        # skip header row if present
        try:
            next(csv_reader) # skip header
        except StopIteration:
            return apps
        # If header looks like data (no commas), the first row will still be consumed.
        for row in csv_reader:
            if not row:
                continue
            # defensive unpacking: ignore malformed rows
            if len(row) < 3:
                continue
            name, description, category = (field.strip() for field in row[:3])
            apps.append(App(name, description, category))
    return apps
    
# Caller prints once (single responsibility)
if __name__ == "__main__":
    csv_path = Path("apps.csv")
    apps = load_apps_from_csv(csv_path)
    for app in apps:
        app.display()
    # optional: print only social media apps
    for app in apps:
        if app.category == "social media":
            app.display()
