# ------------------------------------------------------------
# Exercise 1: Local Scope
# Variables declared inside a function exist only in that function.
# ------------------------------------------------------------

def function_1():
    my_var = "Hello"          # local variable
    print(my_var)             # accessible here

def function_2():
    print(my_var)             # ERROR: my_var not defined in this scope

function_1()                 # does not output due to error
# function_2()               # would raise NameError

# ------------------------------------------------------------
# Exercise 2: More Local Scope
# Each function has its own independent local scope.
# ------------------------------------------------------------

def function_1():
    my_var = "Hello"          # local to function_1
    print(my_var)

def function_2():
    my_var = "Bonjour"        # local to function_2
    print(my_var)

function_1()
function_2()

# Adding a third independent scope
def function_3():
    my_var = "Hola"           # local to function_3
    print(my_var)

function_3()

# ------------------------------------------------------------
# Exercise 3: Global Scope (Referencing)
# Global variables can be read inside functions.
# ------------------------------------------------------------

greeting = "Hello"            # global variable

def say_hello():
    """Print a greeting"""
    print(greeting)           # reads global variable

say_hello()

# ------------------------------------------------------------
# Exercise 4: Attempting to Modify Global Without global Keyword
# Assignment inside a function creates a new local variable.
# ------------------------------------------------------------

greeting = "Hello"

def say_hello():
    """Attempt to modify global greeting"""
    greeting = "Bonjour"      # creates a new local variable
    print(greeting)           # prints local version

say_hello()                   # Bonjour
print(greeting)               # Hello - still "Hello" globally

# ------------------------------------------------------------
# Exercise 5: Modifying Global Using global Keyword
# global allows modification of the global variable.
# ------------------------------------------------------------

greeting = "Hello"

def say_hello():
    """Modify global greeting"""
    global greeting           # declare intention to modify global
    greeting = "Bonjour"      # modifies global variable
    print(greeting)

say_hello()                   # Bonjour
print(greeting)               # Bonjour - global variable now "Bonjour"

# ------------------------------------------------------------
# Exercise 6: Global vs Local Scope Collision
# Local variable overrides global variable inside the function.
# ------------------------------------------------------------

my_var = "global scope"       # global variable

def print_scope():
    """Demonstrate local vs global precedence"""
    my_var = "local scope"    # local variable shadows global
    print(my_var)             # prints local version

print_scope()                 # local scope
print(my_var)                 # global scope - prints global version

# ------------------------------------------------------------
# Exercise 7: global Keyword Overrides Local Precedence
# Using global makes the global variable take precedence.
# ------------------------------------------------------------

my_var = "global scope"

def print_scope():
    """Modify global variable instead of creating local"""
    global my_var
    my_var = "local scope"    # modifies global variable
    print(my_var)

print_scope()
print(my_var)                 # both print "local scope"

# ------------------------------------------------------------
# Exercise 8: Passing a Parameter Named my_var
# Parameter creates a new local variable that shadows global.
# ------------------------------------------------------------

my_var = "global scope"

def print_scope(my_var):
    """Parameter shadows global variable"""
    my_var = "local scope"    # modifies parameter, not global
    print(my_var)

print_scope(my_var)           # prints local version
print(my_var)                 # global remains unchanged

# ------------------------------------------------------------
# Exercise 9: Modifying Global Variable with change_var Function
# Define and call a function that modifies a global variable.
# ------------------------------------------------------------

# my_var starts as a global variable
my_var = 0  # declare global variable

def change_var():
    """Modify the global my_var variable"""
    global my_var               # allow modification of global
    my_var += 1                 # increment global variable by 1
    print(my_var)               # prints updated value

change_var()                    # 1
print(my_var)                   # 1 -> matches change_var()

