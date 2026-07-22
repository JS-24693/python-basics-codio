# Class Phone
class Phone:
    """Component class representing a cellphone."""
    def __init__(self, name, color, storage):
        self.name = name
        self.color = color
        self.storage = storage
    
    def __str__(self):
        """Human-friendly string used by print() and str()."""
        return f"A {self.color} {self.name} with {self.storage}GB of storage."

# Class Laptop
class Laptop:
    """Component class representing a laptop."""
    def __init__(self, name, size, storage):
        self.name = name
        self.size = size
        self.storage = storage
    
    def __str__(self):
        """Human-friendly string used by print() and str()."""
        return f"A {self.size}\" {self.name} with {self.storage}GB of storage."