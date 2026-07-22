# Demonstrates encapsulation using getters, setters, property decorators,
# property() function, and data validation.

# ------------------------------------------------------------
# Getter/Setter Methods (non‑Pythonic style)
# ------------------------------------------------------------

class Phone:
    """Encapsulated attributes using explicit getter/setter methods."""
    def __init__(self, model, storage, megapixels):
        self._model = model
        self._storage = storage
        self._megapixels = megapixels

    # getters
    def get_model(self):
        return self._model

    def get_storage(self):
        return self._storage

    def get_megapixels(self):
        return self._megapixels

    # setters
    def set_model(self, new_model):
        self._model = new_model

    def set_storage(self, new_storage):
        self._storage = new_storage

    def set_megapixels(self, new_megapixels):
        self._megapixels = new_megapixels


# ------------------------------------------------------------
# Property Decorator (Pythonic style)
# ------------------------------------------------------------

class Person:
    """Uses @property and validation for name and age."""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    # setter with type validation
    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    # getter
    @property
    def age(self):
        return self._age

    # setter with value validation
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age must be a positive number.")
        self._age = new_age

c = Person("Calvin", 6)
print(c.name)
print(c.age)
c.name = "Hobbes"
print(c.name) # Hobbes
# c.name = 5
# print(c.name) # TypeError: Names must be expressed as a string
# c.age = -1
# print(c.age)  # ValueError: Age must be a positive number.

# ------------------------------------------------------------
# Property Function (alternative Pythonic style)
# ------------------------------------------------------------

class Person2:
    """Implements getters/setters using property() instead of decorators."""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # setter methods
    def set_name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age must be a positive number.")
        self._age = new_age

    # property objects
    name = property(get_name, set_name)
    age = property(get_age, set_age)

# Test case:
c = Person("Calvin", 6)
print(c.name)
print(c.age)
c.name = "Hobbes"
print(c.name)
