# Encapsulation convention for attributes
class Phone:
  def __init__(self, model, storage, megapixels, carrier):
    self._model = model         # _ before attribute or method to show private
    self._storage = storage
    self._megapixels = megapixels
    self._carrier = carrier 
    
my_phone = Phone("iPhone", 256, 12, "AT&T")
print(my_phone.__dict__)       # dictionary attribute to store attributes by class
                               # {'_model': 'iPhone', '_storage': 256, 
                               # '_megapixels': 12, '_carrier': 'AT&T'}

# Encapsulation within method
class PrivateClass:
    def __init__(self):
        self._private_attribute = "I am a private attribute"
  
    def _private_method(self):
        return "I am a private method" 
    
obj = PrivateClass()
print(obj._private_method()) # I am a private method

# Two underscores trigger name‑mangling: __private_attribute becomes
# _PrivateClass__private_attribute internally. Direct access fails, so
# a public helper method is required to return the private value.
class PrivateClass:
    def __init__(self):
        self.__private_attribute = "I am a private attribute"
    
    def helper_method(self):
        # Accesses the mangled name internally
        return self.__private_attribute

obj = PrivateClass()
print(obj.helper_method())  # I am a private attribute


# Two underscores also mangle method names: __private_method becomes
# _PrivateClass__private_method. External calls fail, so a public
# helper method must invoke the private method internally.
class PrivateClass:
    def __init__(self):
        self.__private_attribute = "I am a private attribute"
    
    def __private_method(self):
        return "I am a private method"
  
    def helper_method(self):
        # Calls the mangled private method internally
        return self.__private_method()

obj = PrivateClass()
print(obj.helper_method())  # I am a private method


# Encapsulation Example 
class BankAccount:
    """Encapsulated account with private balance and owner."""

    def __init__(self, owner, balance):
        self._owner = owner          # private attribute
        self._balance = balance      # private attribute

    def get_owner(self):
        """Return account owner."""
        return self._owner

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def set_balance(self, amount):
        """Update balance with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        """Increase balance safely."""
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        """Decrease balance safely."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

# Example usage 
acct = BankAccount("Sarah", 100)
acct.deposit(50)
print(acct.get_balance())  # 150
