#!/usr/bin/env python3
"""
c4m3lab.py

Interactive contact manager demonstrating polymorphism and operator overloading,
plus a Chef comparison challenge.

Run: python3 c4m3lab.py
"""

# --- Chef challenge implementation ---

class Chef:
    """
    Simple Chef class for the challenge.

    Attributes:
      - name: chef's full name
      - cuisine: string describing cuisine(s)
      - michelin_stars: integer number of Michelin stars
    """

    def __init__(self, name: str, cuisine: str, michelin_stars: int) -> None:
        self.name = name
        self.cuisine = cuisine
        self.michelin_stars = int(michelin_stars)

    # Overload greater-than so chefs can be compared by stars
    def __gt__(self, other: "Chef") -> bool:
        return self.michelin_stars > other.michelin_stars

    # Overload less-than for completeness
    def __lt__(self, other: "Chef") -> bool:
        return self.michelin_stars < other.michelin_stars

    def compare(self, other: "Chef") -> str:
        """
        Return a sentence that names the chef with more Michelin stars.
        The result is the same regardless of which object calls compare.
        """
        # Use the overloaded operators to determine ordering
        if self > other:
            winner, loser = self, other
        elif self < other:
            winner, loser = other, self
        else:
            # Tie case: return a clear tie message
            return f"{self.name} and {other.name} have the same number of Michelin stars"

        return f"{winner.name} has more Michelin stars than {loser.name}"

## Test case
def _chef_demo() -> None:
    """Demonstrate the Chef.compare behavior."""
    print("--- Chef compare demo ---")
    marco = Chef("Marco Pierre White", "French, British", 3)
    rene = Chef("Rene Redzepi", "Nordic", 2)

    # Both calls should produce the same human-readable sentence
    print("marco.compare(rene) ->", marco.compare(rene))
    print("rene.compare(marco) ->", rene.compare(marco))

_chef_demo()


# --- Interactive contact manager demonstrating polymorphism and operator overloading ---

from typing import List, Optional


class Information:
    """
    Stores contact information for a single person.
    Prompts the user for fields when instantiated.
    """

    def __init__(self) -> None:
        # Prompt the user for contact details
        self.first_name: str = input("Enter their first name: ").strip()
        self.last_name: str = input("Enter their last name: ").strip()
        self.personal_phone: str = input("Enter their personal phone number: ").strip()
        self.personal_email: str = input("Enter their personal email address: ").strip()
        self.work_phone: str = input("Enter their work phone number: ").strip()
        self.work_email: str = input("Enter their work email address: ").strip()
        self.title: str = input("Enter their work title: ").strip()

    def display_info(self) -> None:
        """
        Print the stored contact information in a readable format.
        """
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Personal phone number: {self.personal_phone}")
        print(f"Personal email address: {self.personal_email}")
        print(f"Work title: {self.title}")
        print(f"Work phone number: {self.work_phone}")
        print(f"Work email address: {self.work_email}")


class Contacts:
    """
    Manages the contact list and the interactive views.

    Views:
      - 'list' : show list of contacts and prompt for action
      - 'info' : show details for a selected contact and allow navigation
      - 'add'  : add a new contact
      - 'quit' : exit the program
    """

    def __init__(self) -> None:
        # Start in list view per lab instructions
        self.view: str = "list"
        # The list of Information objects
        self.contact_list: List[Information] = []
        # Last user choice (string)
        self.choice: Optional[str] = None
        # Index of currently selected contact (when in 'info' view)
        self.index: Optional[int] = None

    def display(self) -> None:
        """
        Main loop: dispatch to the appropriate view until the user quits.
        """
        while True:
            if self.view == "list":
                self.show_list()
            elif self.view == "info":
                self.show_info()
            elif self.view == "add":
                print()
                self.add_contact()
            elif self.view == "quit":
                print("\nClosing the contact list. . . \n")
                break
            else:
                # Defensive: unknown view -> go to list
                self.view = "list"

    def show_list(self) -> None:
        """
        Display the list of contacts. If empty, prompt to add or quit.
        Otherwise show numbered list and prompt for selection/add/quit.
        """
        print()
        if len(self.contact_list) == 0:
            # No contacts yet: offer to add or quit
            self.choice = input("(A)dd a new contact \n(Q)uit \n> ").lower().strip()
        else:
            for index, contact in enumerate(self.contact_list):
                print(f"{index + 1}) {contact.first_name} {contact.last_name}")
            self.choice = input("\n(#) Select a name \n(A)dd a new contact \n(Q)uit \n> ").lower().strip()
        self.handle_choice()

    def show_info(self) -> None:
        """
        Display the information for the currently selected contact and
        offer navigation: Contact List (c), Previous (p), Next (n), Quit (q).
        """
        # Safety: ensure index is valid
        if self.index is None or not (0 <= self.index < len(self.contact_list)):
            # If invalid, return to list
            print("\nInvalid contact selection. Returning to list.")
            self.view = "list"
            return

        # Display the selected contact's info
        self.contact_list[self.index].display_info()

        # Prompt for navigation choices
        self.choice = input("\n(C)ontact List \n(P)revious contact \n(N)ext contact \n(Q)uit \n> ").lower().strip()
        self.handle_choice()

    def __add__(self, new_contact: Information) -> "Contacts":
        """
        Overload the + operator to append a new Information object to the contact list.
        Returns self to allow chaining if desired.
        """
        self.contact_list.append(new_contact)
        return self

    def add_contact(self) -> None:
        """
        Create a new Information object (prompts user) and add it to the list
        using the overloaded + operator. Then return to list view.
        """
        # Instantiate Information which prompts the user for fields
        self + Information()
        # After adding, go back to list view
        self.view = "list"

    def handle_choice(self) -> None:
        """
        Interpret the user's choice and update view/index accordingly.
        Handles:
          - q : quit (from any view)
          - a : add (only from list view)
          - numeric selection : select contact (only from list view)
          - c : return to list (only from info view)
          - n : next contact (only from info view) with wrapping
          - p : previous contact (only from info view) with wrapping
        """
        if not self.choice:
            return

        # Quit from any view
        if self.choice == "q":
            self.view = "quit"
            return

        # Add new contact (only from list view)
        if self.choice == "a" and self.view == "list":
            self.view = "add"
            return

        # Numeric selection (only from list view)
        if self.choice.isnumeric() and self.view == "list":
            index = int(self.choice) - 1  # convert to 0-based
            if 0 <= index < len(self.contact_list):
                self.index = index
                self.view = "info"
            else:
                print("\nNumber out of range. Please try again.")
            return

        # From info view: return to list
        if self.choice == "c" and self.view == "info":
            self.view = "list"
            return

        # From info view: next contact (wrap to 0 if at end)
        if self.choice == "n" and self.view == "info":
            if self.index is None:
                self.index = 0
            else:
                self.index = self.index + 1 if (self.index + 1) < len(self.contact_list) else 0
            # stay in info view
            self.view = "info"
            return

        # From info view: previous contact (wrap to last if at start)
        if self.choice == "p" and self.view == "info":
            if self.index is None:
                self.index = 0
            else:
                self.index = self.index - 1 if (self.index - 1) >= 0 else (len(self.contact_list) - 1)
            # stay in info view
            self.view = "info"
            return

        # If we reach here, the input was not recognized for the current view
        print("\nUnrecognized choice for the current view. Please try again.")

contacts = Contacts()
contacts.display()
print(len(contacts.contact_list))
