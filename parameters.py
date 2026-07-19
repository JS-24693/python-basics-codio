# ------------------------------------------------------------
# Exercise 1: Passing Parameters
# Demonstrates defining a function with parameters and calling it.
# ------------------------------------------------------------

def addition(num1, num2):
    """Prints the sum of two numbers"""
    print(num1 + num2)

addition(5, 7)  # positional parameters

# variation 1: define function and print color sentences
# each argument supplies one color example

def color_sentences(white, red, green):
    """Print three color statements"""
    print("{} are white. {} are red. {} is green."
          .format(white, red, green))

# call function with three string arguments
color_sentences("Clouds", "Firetrucks", "Grass")

# ------------------------------------------------------------
# Exercise 2: Parameter Order
# Shows how positional order determines parameter assignment.
# ------------------------------------------------------------

def add_sub(num1, num2, num3):
    """Add first two parameters, subtract the third, print result"""
    print(num1 + num2 - num3)

add_sub(5, 10, 15)  # order matters

# ------------------------------------------------------------
# Exercise 3: Named Parameters
# Demonstrates assigning values by parameter name.
# ------------------------------------------------------------

def subtract(num1, num2):
    """Subtract the second parameter from the first"""
    print(num1 - num2)

subtract(5, 2)               # positional. Output: 3
subtract(2, 5)               # positional reversed. Output: -3
subtract(num2=2, num1=5)     # named parameters. Output: 3

# ------------------------------------------------------------
# Exercise 4: Parameter Data Types
# Shows parameters can be ints, floats, strings, booleans, lists, etc.
# ------------------------------------------------------------

def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each parameter"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))

parameter_types(1, 5.9, "Beatles", False)
# Output: The type of 1 is <class 'int'>
#         The type of 5.9 is <class 'float'>
#         The type of Beatles is <class 'str'>
#         The type of False is <class 'bool'>

# ------------------------------------------------------------
# Exercise 5: Checking Parameter Types (try/except)
# Demonstrates catching errors when wrong types are passed.
# ------------------------------------------------------------

# def addition(num1, num2):
#    """Add the two parameters together"""
#    print(num1 + num2)
    
# addition(5, "cat")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Variation 1: try/except to catch errors
def addition_safe(num1, num2):
    """Add two parameters; catch any error"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")

addition_safe(5, "cat")  # triggers error handling

# ------------------------------------------------------------
# Exercise 6: Type-Specific Error Handling
# Uses TypeError to provide clearer feedback.
# ------------------------------------------------------------

def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any errors"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")
    
addition(5, "cat") # Output: There is an error in your code.

# Variation 2: try/except to catch errors
def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any errors"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")
    
addition(5, 3) # Output: 8

# Variation 3: if TypeError, explain the problem
def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any type errors"""
    try:
        print(num1 + num2)
    except TypeError:
        print("Please pass the function two numbers")
    
addition(5, "cat")  # Please plass the function two numbers

# Variation 4: if ZeroDivisionError, explain the problem
def division(num1, num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("Division by zero is not allowed")

division(3, 4)

# ------------------------------------------------------------
# Exercise 7: Optional Parameters
# Shows default parameter behavior and override.
# ------------------------------------------------------------

def add_if_true(num1, num2, bool=True):
    """Print sum only if bool is True"""
    # default bool=True → addition runs unless caller overrides
    if bool:
        print(num1 + num2)
    else:
        print("No addition, bool is false")

add_if_true(5, 7)        # uses default True → prints 12
add_if_true(5, 7, False) # overrides default → prints message


# ------------------------------------------------------------
# Exercise 8: Variable-Length Parameter Lists (*args)
# Allows any number of parameters.
# ------------------------------------------------------------

def calc_sum(*nums):
    """Calculate and print the sum of all parameters"""
    total = 0
    for num in nums:
        total += num
    print(total)

calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # many parameters
calc_sum(4)                              # single parameter
calc_sum()                               # no parameters (prints 0)
